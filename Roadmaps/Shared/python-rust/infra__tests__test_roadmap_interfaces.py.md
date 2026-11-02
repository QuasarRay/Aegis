# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 150. Inventory digest: `0300722c4e622c4ce151d9b8bf1701c81ace64e2d97953c29519497c47d1975a`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_interfaces.py::module::root::Module

Source: `infra/tests/test_roadmap_interfaces.py:1`; AST `56b3ed10acde15ed7e45e1e81ae96ed8890fa6a1383086a34f52aaaefc2e38ab`.

Rust module: `infra::tests::test_roadmap_interfaces`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, __file__, __name__, after, args, before, compare_interfaces, json, m, nested, next, observe_interfaces, path, policy, result, self, shared, shutil, str, subprocess, sys, tempfile, unittest, value. Outputs/bindings: ROOT, after, before, m, nested, path, policy, result, shared, value.
Calls/effect boundaries: (nested / 'hidden.py').write_text, (self.package / '__init__.py').write_text, (self.package / 'roadmap_policy.py').write_text, (self.package / 'unowned.py').unlink, (self.package / 'unowned.py').write_text, Path, Path(__file__).resolve, before.replace, compare_interfaces, json.dumps, json.loads, nested.mkdir, next, observe_interfaces, path.read_text, path.read_text().replace, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaisesRegex, self.assertTrue, self.git, self.package.mkdir, self.temp.cleanup, shared.mkdir, shutil.copyfile, str, subprocess.run, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[0]::ImportFrom

Source: `infra/tests/test_roadmap_interfaces.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[1]::Import

Source: `infra/tests/test_roadmap_interfaces.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_interfaces.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_interfaces.py:5`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_interfaces.py:6`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_interfaces.py:7`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_interfaces.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_interfaces.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[8]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:11`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[8].value.value.value::Call

Source: `infra/tests/test_roadmap_interfaces.py:11`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[8].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_interfaces.py:11`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[9]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:12`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[9].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:12`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[9].value.args[1]::Call

Source: `infra/tests/test_roadmap_interfaces.py:12`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_interfaces.py:13`; AST `fb74a46ac4a7a700efab59110492d53c3fe3568a7c77f496de120b63c0016ca2`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_interfaces.py:14`; AST `f03d490df75c7330951b5ce75380b297979b688b88c1f26364ab52e4c8a2c0af`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_interfaces.py:17`; AST `60fd5f1c89def27e2a01241d1a8f81c78e4ada72d54cffe7de94e866ba366970`.

Rust module: `infra::tests::test_roadmap_interfaces`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, ROOT, after, args, before, compare_interfaces, json, m, nested, next, observe_interfaces, path, policy, result, self, shared, shutil, subprocess, tempfile, unittest, value. Outputs/bindings: after, before, m, nested, path, policy, result, shared, value.
Calls/effect boundaries: (nested / 'hidden.py').write_text, (self.package / '__init__.py').write_text, (self.package / 'roadmap_policy.py').write_text, (self.package / 'unowned.py').unlink, (self.package / 'unowned.py').write_text, Path, before.replace, compare_interfaces, json.dumps, json.loads, nested.mkdir, next, observe_interfaces, path.read_text, path.read_text().replace, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaisesRegex, self.assertTrue, self.git, self.package.mkdir, self.temp.cleanup, shared.mkdir, shutil.copyfile, subprocess.run, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:18`; AST `1c3806a4987310021504c8212bee86db8c13be37940c85c98adc9c3338c42d1f`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, self, shared, shutil, tempfile. Outputs/bindings: shared.
Calls/effect boundaries: (self.package / '__init__.py').write_text, (self.package / 'roadmap_policy.py').write_text, Path, self.git, self.package.mkdir, shared.mkdir, shutil.copyfile, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:19`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:19`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:19`; AST `3fd62e96028b079a923df6e9a7c1c1df8b3ae2536d55ba9d4f31f162d4d5ddb5`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:19`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:20`; AST `625e1a2a4089be7fb9825b7c3622e4a03654df63406fbb1fa1a67b94cc92756d`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:20`; AST `ef24c1b42ea766a0722e7a0654b525c9ae1aba2fc6bc31e483ff049407b3ecb0`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.package.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:20`; AST `74f3f6a567bc485985db9b0baeb90231daf2099cdf3cb96264522c99afe98d4b`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.package.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:21`; AST `4de67e7f9f30bbdcd7799fc60cd85f220196a0a19f6f46ef3532f7d0a61ec593`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:21`; AST `627d21c090eafb66c5a3975ab3011a3c8dc4356627e81f1d15f79c15e1175e77`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:22`; AST `6848657731e8512c984eae33e65f1e407daa5d6af20d08e053e7335d93b5234d`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'roadmap_policy.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:22`; AST `4c46db36094bfa7ed6e3784b9f919d61802497c4310d89f91b926c1fee050556`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'roadmap_policy.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:23`; AST `64a433e7d51b0c2105679a685168fb55724f404a1027a03a7b7c8dcbfe90317e`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: shared.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:23`; AST `d20d143f38d9b5d82545abe3ef1d2ca636f603d0a2b93ac41056e250c71735d1`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:23`; AST `99bcba72db0838f639a464854466bfa2acd0fe9e260d2d59c8e8247715d94a84`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:24`; AST `0fab42a94555c2e368117e83c0c6b637303d08b9030ac3a8c50fdfe608d2d2a4`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:24`; AST `0202850710c66419e5d7f257bce03722ca2d246da579619119f57134d971d012`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `1430bb3a65a10dd0190d1f9005ebf6b31adb6901302279764db1e02c404bbcfe`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `a988752d239643c86702cea863179a165997931847f7a9e5c6e778cd4e153809`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[10]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `3ae985a8aa85b0b5a6dd4c6f76696a89abdff14cb9a52267e9a88fb027b80e5c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `fb3b145e8bfab82e89ac5c6c01b8b8fc5b6be600bd72b00e322823160f1cb9ff`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `9fc45bdd6af5271328f9b50279268242fe577cb9a84bd337816beda74b0ed3fe`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::setUp::root.body[12].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:25`; AST `880d0d1488258f01cba176104b6f92c9300ca2a49f988ab990aa6653419b07cb`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::git::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:27`; AST `271c0d687a4655e50eb1291f354bb3581ea4768e1e956eb23dafe1967addb448`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: args, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::git::root.body[12].body[1].body[0]::Return

Source: `infra/tests/test_roadmap_interfaces.py:28`; AST `3239825df4546b5d0c0c88f2e0ed350d6fd31d8715c731085015ddd757792232`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::git::root.body[12].body[1].body[0].value.value::Call

Source: `infra/tests/test_roadmap_interfaces.py:28`; AST `44cd28b7f261aabba1edf119d7f486a703830077152126737ec3f3bf3e1f87ab`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::tearDown::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:32`; AST `13fc628cded8f8def9f296b061b0d1b4f129ada0770d009511b176b914c63004`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::tearDown::root.body[12].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:33`; AST `03b3f025b568ce93e3252b0f1f4a5ce0348dbf2ecebaae9a0913927af51d7b24`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::tearDown::root.body[12].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:33`; AST `467d2c9d775dc88f51613c917ddb5ec5487d5c87293666d9c9c5f9a88375b66b`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:35`; AST `425964f9cee2301eb8dbc170f47568ee2b2c706e16463607dda1915a959935ed`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: compare_interfaces, m, next, observe_interfaces, path, policy, self, value. Outputs/bindings: m, path, policy, value.
Calls/effect boundaries: compare_interfaces, next, observe_interfaces, path.read_text, path.write_text, self.assertEqual, self.assertIn.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:36`; AST `b0168c9d5ce3c4f2dad5bdfad41d2df5a085773fcfdff337d066133b91b594db`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:37`; AST `afb1650151c23d281ef1ed97503675dff2b1b170b4f392523dd711ed9958e66d`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:37`; AST `aece0f8695d9735155d5a860b4a3e9d6ba37a2db8dfe52661c9b2c4c19258b58`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[1].value.args[0].left::Call

Source: `infra/tests/test_roadmap_interfaces.py:37`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[2]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:38`; AST `48db781082e8210db2e0f6b4d1a35f90ec0138dcc470b089c76eb0373b6e46c6`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_interfaces, self. Outputs/bindings: value.
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:38`; AST `b0b20c348bb7408023c3fca06311f3c74e04d832d4e4b3f01e5b1e17bbd59518`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[3]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:39`; AST `061d822c73e84ae0c85cde36f915ac2c2c6a10d79590d38664ff1a68f668b709`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: m, next, value. Outputs/bindings: m, policy.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:39`; AST `740cbfd1ffd0c4d9ec31fa6772a7ec03b5677405ad760106a67f8266f81a9256`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: m, next, value. Outputs/bindings: m.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[3].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_interfaces.py:39`; AST `7b56b58bf4270b4fba092864e8c32aee1b79f38410e2d143712b93d0a5a92ae5`.

Rust module: `infra::tests::test_roadmap_interfaces`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: m, value. Outputs/bindings: m.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[3].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:40`; AST `1f707a6ee923679e5e07524fd5a7d3a654a297f3f4d03c4f4929a71d939273f4`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:40`; AST `66265d4c4ec6cc42716618874e41758772c7cae0c9cda619f4b016c01ec8b7af`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[5]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:41`; AST `705005eb1209d24ae1bae78061e62b2c7f4716ea8b464e0b39022cb14a79d438`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[5].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:41`; AST `79d7683453d9890109569a8b2304ab0a8a033cdd69c781aa046da2f4df8bc60b`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_observation_does_not_execute_source_and_retains_lifecycle_methods::root.body[12].body[3].body[5].value.args[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:41`; AST `1eb2ae2ceaa88271d51c038770ecb1ee15988ea0a2ce5d084ad1540625cbd2be`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:43`; AST `0042ef195b7ef5e3e8ae7728142028557e799701839283e7754cb6b91ef0ebec`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: after, before, compare_interfaces, path, result, self. Outputs/bindings: after, before, path, result.
Calls/effect boundaries: before.replace, compare_interfaces, path.read_text, path.write_text, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:44`; AST `b0168c9d5ce3c4f2dad5bdfad41d2df5a085773fcfdff337d066133b91b594db`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:44`; AST `dfb21188f6ff842add1f6d1b02a8138431ff3fc8f0a78190a39616d54a198ed8`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:44`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2]::For

Source: `infra/tests/test_roadmap_interfaces.py:45`; AST `752e615435d5ebc2fc36eb49b5ae713f7d891be32ffbdfc56af9630d4e5d137f`.

Rust module: `infra::tests::test_roadmap_interfaces`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: after, before, compare_interfaces, path, result, self. Outputs/bindings: after, result.
Calls/effect boundaries: before.replace, compare_interfaces, path.write_text, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[12].body[4].body[2]; no call, error or mutation may be omitted. Iteration: after in (before.replace('bound=3', 'bound=2'), before.replace('def policy', 'def renamed'), before.replace('def __enter__(self)', 'def __enter__(self, mode)'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].iter.elts[0]::Call

Source: `infra/tests/test_roadmap_interfaces.py:45`; AST `eb25c83b3fa687a51601240f9878ea048d559f0a999618d9b9d7f53a062f5891`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.replace.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].iter.elts[1]::Call

Source: `infra/tests/test_roadmap_interfaces.py:45`; AST `3e356552ce2a611db33d1f821f5d1bbe32d67517e3d19113f7dbcb4a88f2d70a`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.replace.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].iter.elts[2]::Call

Source: `infra/tests/test_roadmap_interfaces.py:46`; AST `c22eb0271d5166138cd65803eb7bec3a48f1b5fb4d4bb4b8a650df28e3a42e4c`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before. Outputs/bindings: (none).
Calls/effect boundaries: before.replace.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:47`; AST `22dcbdd3ddbe84a38518866930b2d5dd4de15c17ceaf9f6e3b4f39cb89d721b9`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:47`; AST `ea6128c07286dbf2799d9de74f7696b360c2c12a933e55bab786f744a94c1d93`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[1]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:48`; AST `d93973f72fde63e08a19b7f0224e4bd975ea87a7a099f246fdde14ac0d4ee69c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, self. Outputs/bindings: result.
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:48`; AST `1eb2ae2ceaa88271d51c038770ecb1ee15988ea0a2ce5d084ad1540625cbd2be`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:49`; AST `f3e1932ddc89d24e4c09e4000c06ca543486e48310f135848a811a8dc300b364`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:49`; AST `51edc789e863ee8d572ce21ba0f10d2dc42aa2ebf44fd8546232187923c11c8b`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:50`; AST `4ea2f19e16f798d26a00c45faff9c8027e6ce153aa03b721d9c09ca1be7dda61`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_changed_default_removed_export_and_lifecycle_break_are_visible::root.body[12].body[4].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:50`; AST `c2f5ac952d8d17a87e7886d188428bf21e207673a35e24f97d62d26fe463d46e`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:52`; AST `f57115f223d862d9da9c81bc73cb2a1073b16644aa8927626697077e1e721887`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: compare_interfaces, path, self. Outputs/bindings: path.
Calls/effect boundaries: compare_interfaces, path.read_text, path.write_text, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:53`; AST `b0168c9d5ce3c4f2dad5bdfad41d2df5a085773fcfdff337d066133b91b594db`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:53`; AST `fbf7bfbe89306f7a73597d3e0caf8da19e409ecdda44266347b537b2083ecf9d`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:53`; AST `2760f38a9b6e298058ded1506bb31f580572f5f88314947846e095c9fac759b0`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[1].value.args[0].left::Call

Source: `infra/tests/test_roadmap_interfaces.py:53`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:54`; AST `19d40e759d0f9f394ee604e6ffc0dc9970aa8597f27e47eaf0f80bd415369d32`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:54`; AST `efdc2c71754ef18298931b5c0bc35621d605e8026cf96a76ae64df95099ba62a`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_added_public_method_is_structurally_additive::root.body[12].body[5].body[2].value.args[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:54`; AST `1eb2ae2ceaa88271d51c038770ecb1ee15988ea0a2ce5d084ad1540625cbd2be`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:56`; AST `f57af70328a3a948cb5feb2bf4fe8e0a5cd4acadb98f303098957afeac46ba22`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: compare_interfaces, path, self. Outputs/bindings: path.
Calls/effect boundaries: compare_interfaces, path.read_text, path.read_text().replace, path.write_text, self.assertFalse, self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:57`; AST `b0168c9d5ce3c4f2dad5bdfad41d2df5a085773fcfdff337d066133b91b594db`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:58`; AST `42ccd0cefb38760f5248c700d30c790d274001378d5e8a3d36d0a55e3e2e6024`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:58`; AST `1ea59552efd0a85ea42b9aed17b2bc5719b7fcc3c9730e4a72691f7a1a567f5d`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:59`; AST `3ae985a8aa85b0b5a6dd4c6f76696a89abdff14cb9a52267e9a88fb027b80e5c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:59`; AST `fb3b145e8bfab82e89ac5c6c01b8b8fc5b6be600bd72b00e322823160f1cb9ff`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:59`; AST `df00d22ef63340b18e21b9ad7ef25dec8c3795c3870924b204fecc2e4ad9487c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:59`; AST `c971c8f01436dcb05e88fca04d6bd3256e9856f0419c2c1c8dd64ccb90ed9f25`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:60`; AST `d3201e4c469dcb7ed516d48e132ef4d87fa734fc052a042f1973f97e4b24ee7b`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:60`; AST `cecd6e507f19f972003088e5e8ec704da847e1d429719dae095731a497d6852a`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_interfaces.py:60`; AST `f160d20e44fd3dfb1abf5353e1a45bdb388a6a92d75b0e01acd265119718c499`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[4].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_interfaces.py:60`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:61`; AST `ec3b0d3508c89ab831ec37463091d18438d1b1f701551b9aad79c1b002ca6f99`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:61`; AST `374922605d7e33a740684e2100c30a578f1f9f974ef4cd897e6e4c4fc82e2834`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_shadowed_declarations_do_not_hide_an_earlier_signature_change::root.body[12].body[6].body[5].value.args[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:61`; AST `1eb2ae2ceaa88271d51c038770ecb1ee15988ea0a2ce5d084ad1540625cbd2be`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:63`; AST `08615c3a6cd2cac68f4cd4609c2d1c357c8ef3d96c100a53f9f50d704a17d2b7`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, json, observe_interfaces, path, self, value. Outputs/bindings: path, value.
Calls/effect boundaries: (self.package / 'unowned.py').unlink, (self.package / 'unowned.py').write_text, json.dumps, json.loads, observe_interfaces, path.read_text, path.write_text, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:64`; AST `c06264564acbb5bc4d8708ebe6bb783a49ba82fe8e495de9b9997e31798d7cc8`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'unowned.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:64`; AST `b0f9a5fdf108875bdd641e0be88b729ae9bc6f36be8c65c2e15bf59bd3ceb68e`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'unowned.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[1]::With

Source: `infra/tests/test_roadmap_interfaces.py:65`; AST `a6e50f42ddfb06e65bf55027ff7a1f7519909eef5f34c56afb2fef69de109d2b`.

Rust module: `infra::tests::test_roadmap_interfaces`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_interfaces.py:65`; AST `964ea69fd8a3fbf69bb4ec1f372d9997f3dea7e9827ef99949351c88843560b5`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:66`; AST `4d8a54b49cf9c80c15331e1aaf408500629c6a0f0def1ee517f9e204351da4c5`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:66`; AST `b0b20c348bb7408023c3fca06311f3c74e04d832d4e4b3f01e5b1e17bbd59518`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:67`; AST `1a0a0463b7322ecb1e4b4cf515a6706d4933becd8523cb0417c8dc49db94c8be`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'unowned.py').unlink.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:67`; AST `2fdaff861f3a55c6b5eca59c7a0bc6577cc29eeccc3cde773acea6aae45c9d32`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'unowned.py').unlink.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[3]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:68`; AST `9221d7878ac0ee2370a0f186bcbf4c21a3dc25892d7f8209eed28cefe099fc77`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[4]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:68`; AST `37a32195bb79186a8f4195e683859955aaa3af2d200e2e476eca9a9aada2caf0`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: value.
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[4].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:68`; AST `4a076f3fdf20f1dd94162a22f2b9944a159c045ed6266d1cb7ac9b597c2ea970`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_interfaces.py:68`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[5]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:69`; AST `504af41a7e1e64e94416914d5cfabe313b52c7b796bfa311afe75af6d5990bd9`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[6]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:69`; AST `15ebdc70822e4b00a80d06bcd9836f36db3791ad2cd9332f5e6cb076eb393ee9`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[6].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:69`; AST `3a12431d0797e340b6ea3222c5db2d0b89ebed8769519018f6fd0f99b02ac15d`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_interfaces.py:69`; AST `ccf75a3fee685fba92dbd87286589aeb7a31a140dc5ab06ed02ae7cde17c019e`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, value. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[7]::With

Source: `infra/tests/test_roadmap_interfaces.py:70`; AST `d880cc8e10420d05bd8a91b3765dbbd0a02a3152112e8cba704dfc88e05604c6`.

Rust module: `infra::tests::test_roadmap_interfaces`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[7].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_interfaces.py:70`; AST `2d06679c3048d44b7a4c3b0152e34f32f96ac8a93ba09fad1187ff0c7ced09a4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[7].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:71`; AST `4d8a54b49cf9c80c15331e1aaf408500629c6a0f0def1ee517f9e204351da4c5`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_unknown_module_or_record_version_fails_without_importing_it::root.body[12].body[7].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:71`; AST `b0b20c348bb7408023c3fca06311f3c74e04d832d4e4b3f01e5b1e17bbd59518`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:73`; AST `909e8fca25527b071b0a76c241faa0c2ecc45f874fa773b74ab8b0b6ca2302d2`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, nested, observe_interfaces, self. Outputs/bindings: nested.
Calls/effect boundaries: (nested / 'hidden.py').write_text, nested.mkdir, observe_interfaces, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:74`; AST `c93e729d0fc71c69569d05ac2f07a8e58bfc419b7877181cc07a8baefe55edf8`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: nested.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[1]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:74`; AST `0836d57657a17ab456327d02021445bcfabe07335a44ee36b41b83fbfe54adbd`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: nested.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:74`; AST `a2f79ce9b18124b31ede6b5775b6c82e683b6753b271679f7a6bd80ac4b2de7c`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: nested.mkdir.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:75`; AST `fd11257673f1b01c7de502311eba92d5c0d117b31c61735106403d89d58cf50c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'hidden.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:75`; AST `00dd32b15a43fc8267b55db5e142c2669620c0fcb3dc8a8027ff3ca6a5ab3bdf`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'hidden.py').write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[3]::With

Source: `infra/tests/test_roadmap_interfaces.py:76`; AST `a6e50f42ddfb06e65bf55027ff7a1f7519909eef5f34c56afb2fef69de109d2b`.

Rust module: `infra::tests::test_roadmap_interfaces`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_interfaces.py:76`; AST `964ea69fd8a3fbf69bb4ec1f372d9997f3dea7e9827ef99949351c88843560b5`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:77`; AST `4d8a54b49cf9c80c15331e1aaf408500629c6a0f0def1ee517f9e204351da4c5`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_nested_unowned_module_is_part_of_the_denominator::root.body[12].body[8].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:77`; AST `b0b20c348bb7408023c3fca06311f3c74e04d832d4e4b3f01e5b1e17bbd59518`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_interfaces.py:79`; AST `40dac2b8858c8b134867006bdb4912f0f1b432b4d8969bb86eb09800a1b6e940`.

Rust module: `infra::tests::test_roadmap_interfaces`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: compare_interfaces, path, self. Outputs/bindings: path.
Calls/effect boundaries: compare_interfaces, path.read_text, path.read_text().replace, path.write_text, self.assertFalse, self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[0]::Assign

Source: `infra/tests/test_roadmap_interfaces.py:80`; AST `b0168c9d5ce3c4f2dad5bdfad41d2df5a085773fcfdff337d066133b91b594db`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[1]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:81`; AST `f3d007e3d549f8d44d550f8fe688762335b1a99a98f046431f0ee95f952fcd44`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:81`; AST `9a7d08188739333e9258ee831350f7c88268c85636ed8dc48f855be407676fa1`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[2]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:82`; AST `3ae985a8aa85b0b5a6dd4c6f76696a89abdff14cb9a52267e9a88fb027b80e5c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[2].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:82`; AST `fb3b145e8bfab82e89ac5c6c01b8b8fc5b6be600bd72b00e322823160f1cb9ff`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[3]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:82`; AST `b4e2e44600b6baacdc82a789c7724cdb528169381c0cf33886e77cbdeab28e1c`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:82`; AST `11052e2d25188f8b538df34f1d85e5d555a711a97e253219599441b4202d7888`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[4]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:83`; AST `1d917568dcad0cf727d89c8054ad3f7610fa19a4d50ec60567708abad29a6cbe`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[4].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:83`; AST `84cebd3b68b8f6037d5b81ff7ba27421a00e3161f139721ebff49ea385dfaf5c`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace, path.write_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_interfaces.py:83`; AST `950f60e0d901351d479fa85207190f85c23aa1f2f45a62248a4c46b5255ad16b`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().replace.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[4].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_interfaces.py:83`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[5]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:84`; AST `ec3b0d3508c89ab831ec37463091d18438d1b1f701551b9aad79c1b002ca6f99`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[5].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:84`; AST `374922605d7e33a740684e2100c30a578f1f9f974ef4cd897e6e4c4fc82e2834`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::ModuleInterfaceTests::test_conditional_declaration_guards_are_part_of_the_interface::root.body[12].body[9].body[5].value.args[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:84`; AST `1eb2ae2ceaa88271d51c038770ecb1ee15988ea0a2ce5d084ad1540625cbd2be`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compare_interfaces, self. Outputs/bindings: (none).
Calls/effect boundaries: compare_interfaces.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[13]::If

Source: `infra/tests/test_roadmap_interfaces.py:87`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_interfaces`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_interfaces.py:88`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_interfaces`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_interfaces.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_interfaces.py:88`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_interfaces`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_interfaces, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
