# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 314. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_destiny.py::module::root::Module

Source: `infra/tests/test_destiny.py:1`; AST `e702f8a3e83362373c46bfdbbcfe87222221bc5985d45d4130cb8a0f06b8106c`.

Rust module: `infra::tests::test_destiny`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: CLI, DestinyFixture, FRAMEWORK, Path, SimpleNamespace, __file__, __name__, all, args, before, contents, data, document, entries, first, fixture, fresh, hashlib, identity, ids, json, len, list, load_profile, ok, os, outside, patch, path, plan, previous, r, relative, report, result, retried, row, rows, second, self, set, source, str, subprocess, sys, tempfile, unittest, work_queue, x. Outputs/bindings: CLI, FRAMEWORK, before, contents, data, document, entries, first, fixture, fresh, identity, ids, outside, path, plan, previous, r, relative, report, result, retried, row, rows, second, source, x.
Calls/effect boundaries: (self.root / '.aegis').symlink_to, (self.root / '.aegis').unlink, (self.root / 'src/new.rs').unlink, (self.root / 'src/runtime.rs').symlink_to, (self.root / 'src/runtime.rs').unlink, Path, Path(__file__).resolve, Path(result['path']).read_text, SimpleNamespace, all, entries.values, first['text'].encode, hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, ids.index, json.dumps, json.loads, len, list, load_profile, os.utime, outside.iterdir, outside.mkdir, patch, path.parent.mkdir, path.read_bytes, path.read_text, path.stat, path.write_text, self.addCleanup, self.assertEqual, self.assertFalse, self.assertGreaterEqual, self.assertIn, self.assertLess, self.assertLessEqual, self.assertNotEqual, self.assertTrue, self.call, self.root.mkdir, self.subTest, self.write, set, str, subprocess.run, sys.path.insert, tempfile.TemporaryDirectory, unittest.main, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[0]::Expr

Source: `infra/tests/test_destiny.py:1`; AST `6d2f10981d400461c2bfde6a247e0800b99405b0972119c6b3a77f9ce4f8cb8d`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[1]::Import

Source: `infra/tests/test_destiny.py:2`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[2]::Import

Source: `infra/tests/test_destiny.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[3]::Import

Source: `infra/tests/test_destiny.py:4`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_destiny.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[5]::Import

Source: `infra/tests/test_destiny.py:6`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[6]::Import

Source: `infra/tests/test_destiny.py:7`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[7]::Import

Source: `infra/tests/test_destiny.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[8]::Import

Source: `infra/tests/test_destiny.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_destiny.py:10`; AST `271cd8a5819453f6952690fd43e9ce152386df249c8de9a1999907454b0006b7`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_destiny.py:11`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[11]::Assign

Source: `infra/tests/test_destiny.py:13`; AST `97bf173db25f481e4314056dd3ee1eb26446998cbaa1e3bd9eff18be6583a592`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: FRAMEWORK.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[11].value.value.value::Call

Source: `infra/tests/test_destiny.py:13`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[11].value.value.value.func.value::Call

Source: `infra/tests/test_destiny.py:13`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[12]::Assign

Source: `infra/tests/test_destiny.py:14`; AST `7b27779e19917713f2ffc8201864788a2093381907fff84849faffd4da73de4b`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FRAMEWORK. Outputs/bindings: CLI.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::root.body[13]::ClassDef

Source: `infra/tests/test_destiny.py:17`; AST `9937acfc5770a06d687664b3f9c6845b5895d0399c7d9bf32d6645ae72dee3a2`.

Rust module: `infra::tests::test_destiny`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: CLI, Path, args, data, json, ok, path, relative, result, self, str, subprocess, sys, tempfile, unittest. Outputs/bindings: path, result.
Calls/effect boundaries: Path, json.loads, path.parent.mkdir, path.write_text, self.addCleanup, self.assertEqual, self.assertNotEqual, self.root.mkdir, self.write, str, subprocess.run, tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0]::FunctionDef

Source: `infra/tests/test_destiny.py:18`; AST `597f7f5c7f672f66335a257eb55936243c0c7993c1f94066da5d1da980fad40d`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, str, subprocess, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.addCleanup, self.root.mkdir, self.write, str, subprocess.run, tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[0]::Assign

Source: `infra/tests/test_destiny.py:19`; AST `4dbc86649f268f127b0a6ac11c31c184758f4bc06a0f8d9ab1a6806930bdd279`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[0].value::Call

Source: `infra/tests/test_destiny.py:19`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[1]::Expr

Source: `infra/tests/test_destiny.py:20`; AST `180794885ca3772c4174f206c159b850c37dfca7c9b0526f940af3d02668bec8`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[1].value::Call

Source: `infra/tests/test_destiny.py:20`; AST `15f69ea0aacdef61fd80213f39cc7414e61bc7d4763858347a221f9a89a73645`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[2]::Assign

Source: `infra/tests/test_destiny.py:21`; AST `217f43d18d99880b0732d1969e5358e32003372751e38ebf49af8af91273c7c6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[2].value.left::Call

Source: `infra/tests/test_destiny.py:21`; AST `350af0ef58dfeabf82fa371e4d1a0525efa6d4376cbcb9b8ead747bbdeb7de21`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[3]::Expr

Source: `infra/tests/test_destiny.py:22`; AST `5b57ad3057a4494b5edcc54ea22adc8c2daf68ee68948db8eab94266507a0ffd`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.root.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[3].value::Call

Source: `infra/tests/test_destiny.py:22`; AST `83c0bf9774e2de836d83d111ae3753edebf9fdd8653203211a84053371914d56`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.root.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[4]::Expr

Source: `infra/tests/test_destiny.py:23`; AST `cd2fc60950148050d1da50ded5874d5cae5a5ab823eb0358e92f1ef2225c2ec6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[4].value::Call

Source: `infra/tests/test_destiny.py:23`; AST `777337577a6632fdaf32857c6b7fbfa9c56494be5f565d5af1b9d80eb19719f5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[4].value.args[0].elts[3]::Call

Source: `infra/tests/test_destiny.py:23`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[4].value.args[0].elts[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[5]::Expr

Source: `infra/tests/test_destiny.py:24`; AST `2016a2544af2d3900f38d391b013642cda9e6ffde7cc48c2db3db28e74126d82`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[5].value::Call

Source: `infra/tests/test_destiny.py:24`; AST `15cac330b8819e424135e668acd0250e99cfbb0cb6576ad2da5be797ff03a8ae`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[6]::Expr

Source: `infra/tests/test_destiny.py:25`; AST `b3f0b4e7e3e016d52735026957d07eee6723c836d9c9e80149c454e51bcaa11a`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[6].value::Call

Source: `infra/tests/test_destiny.py:25`; AST `4d83114cb8b7139adc8caa6d373ce2d55eb3851aed5f8c9168a78daf691cdc7a`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[7]::Expr

Source: `infra/tests/test_destiny.py:26`; AST `333c04c577c5b08526294872c1735e3f01d1ad9b44a7fabf37742931a42ad111`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[7].value::Call

Source: `infra/tests/test_destiny.py:26`; AST `b55c3da25028777e6f8fb07d25df54db7cfbd8bb30af9ea9975fd63bdd9c4d19`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[8]::Expr

Source: `infra/tests/test_destiny.py:27`; AST `003e6ff962b7b8a774b284c3c3aa8c7de0442cd0f7b77505dc5c5b04d161db1c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[8].value::Call

Source: `infra/tests/test_destiny.py:27`; AST `43a5d863a2bc56556eaf2d9fbb2c5026d7a9253c33a96432c51e4c36420b1964`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[9]::Expr

Source: `infra/tests/test_destiny.py:28`; AST `392070f682ef89c75f048d9c792829c21a6f006d57516514abf2b4a238042b1c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[9].value::Call

Source: `infra/tests/test_destiny.py:28`; AST `a372a863b09576dd6e11db2289d8f5a31eb6c8f7a2171c546970ec73d59fc4bb`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[10]::Expr

Source: `infra/tests/test_destiny.py:29`; AST `daed0bed8bf63d92eacd5939eac9db3eb72b470a6decd147ca27d4a3c941ccce`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[10].value::Call

Source: `infra/tests/test_destiny.py:29`; AST `0521cd3951fd0c241d9640034432ac2a6a638725854d0751eb76f6610cf99b15`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[11]::Expr

Source: `infra/tests/test_destiny.py:30`; AST `2774d6eddccf0f6b78d3e7d8bcf86d2bc8b540d97241f757fe621b751fa7744d`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::setUp::root.body[13].body[0].body[11].value::Call

Source: `infra/tests/test_destiny.py:30`; AST `c43410655b1f16f45e3a8f7c9e1e8900368d69056eac8fe01bd359213ecf44e5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1]::FunctionDef

Source: `infra/tests/test_destiny.py:32`; AST `74e43ae0cb8671088303ef6a4c8b524b745fb88f9657dba3dcb2ffb8e9bba8f2`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: data, path, relative, self. Outputs/bindings: path.
Calls/effect boundaries: path.parent.mkdir, path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[0]::Assign

Source: `infra/tests/test_destiny.py:33`; AST `612dd2adce6a63dd3e2fad8942c57edbe760aab2f5efec5eca54b7d564d39a09`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: relative, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[1]::Expr

Source: `infra/tests/test_destiny.py:34`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[1].value::Call

Source: `infra/tests/test_destiny.py:34`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[2]::Expr

Source: `infra/tests/test_destiny.py:35`; AST `57138be383a8fc212a81a43e0909e4d1934e558f2b13d9e536008b755e7986d0`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[2].value::Call

Source: `infra/tests/test_destiny.py:35`; AST `3bd5ab1b55e20dc3e29c6c81bca0d64a5753cbfbd9359539d025a785e771de99`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::write::root.body[13].body[1].body[3]::Return

Source: `infra/tests/test_destiny.py:36`; AST `6a83e41742422cefd09401a733b9520de25fdaca4b583a6ac2a8659697bf9fee`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[13].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2]::FunctionDef

Source: `infra/tests/test_destiny.py:38`; AST `938b7cb91c8a4534193f4e0c83e833f4ae7cb62c9aeb856d003ed088649f9fac`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CLI, args, json, ok, result, self, str, subprocess, sys. Outputs/bindings: result.
Calls/effect boundaries: json.loads, self.assertEqual, self.assertNotEqual, str, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[0]::Assign

Source: `infra/tests/test_destiny.py:39`; AST `8cee11b1b09d717f61e2c8069cc7cd4198f9be43cdd4af5aaf515dfa1c011ca5`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: CLI, args, self, str, subprocess, sys. Outputs/bindings: result.
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[0].value::Call

Source: `infra/tests/test_destiny.py:39`; AST `b5ba9c29d57bf49826c9596750cb8ab9ad5ea05ec342283c517c6b64a5d492ee`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CLI, args, self, str, subprocess, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[0].value.args[0].elts[2]::Call

Source: `infra/tests/test_destiny.py:39`; AST `1645ab0486633a0cc3f02455ccb96c150c4fefb87531144e2917e05a70f1d315`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CLI, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value.args[0].elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[0].value.args[0].elts[4]::Call

Source: `infra/tests/test_destiny.py:39`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].value.args[0].elts[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[1]::If

Source: `infra/tests/test_destiny.py:41`; AST `9abdd6e27e9a81e9273f6f06485666bbdac44fa9145cb7f4db0ea02e3fd0f9be`.

Rust module: `infra::tests::test_destiny`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ok, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[13].body[2].body[1]; no call, error or mutation may be omitted. Condition: ok
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[1].body[0]::Expr

Source: `infra/tests/test_destiny.py:42`; AST `19b0b8bcce357d355ddda61004720b2cbbde2581628207f052113656ce034c02`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[1].body[0].value::Call

Source: `infra/tests/test_destiny.py:42`; AST `3e1b82253203e523ae8d5b0c6b9fe9dc0cf5b60822194ed265167c5381a1d248`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[1].orelse[0]::Expr

Source: `infra/tests/test_destiny.py:44`; AST `e385c4772dc3b5560b127e793bb13b6e592fbc7b732ac3378e15c8bdcaf683c9`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[2].body[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[1].orelse[0].value::Call

Source: `infra/tests/test_destiny.py:44`; AST `fa1c4382d956fded2c33119007f94d633dc9449d9ecea4fb40f133b9cb349364`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[1].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[2]::Return

Source: `infra/tests/test_destiny.py:45`; AST `cde87b992de442e86dec8ebaf774f1e6fbdf46fa4bcd1b13061f08d731f733cf`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[13].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::DestinyFixture::call::root.body[13].body[2].body[2].value::Call

Source: `infra/tests/test_destiny.py:45`; AST `43380d64825738a41395f7ecc09149833b4f8026530d29a3c377de1e3a236eb8`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::root.body[14]::ClassDef

Source: `infra/tests/test_destiny.py:48`; AST `0c05dfc5e3ceba88ff5ca15be470720fb3b4ad53722da7fbf65acbf89eb8fb24`.

Rust module: `infra::tests::test_destiny`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: DestinyFixture, FRAMEWORK, Path, SimpleNamespace, all, before, contents, data, document, entries, first, fixture, fresh, hashlib, identity, ids, json, len, list, load_profile, os, outside, patch, path, plan, previous, r, relative, report, result, retried, row, rows, second, self, set, source, str, subprocess, sys, work_queue, x. Outputs/bindings: before, contents, data, document, entries, first, fixture, fresh, identity, ids, outside, path, plan, previous, r, relative, report, result, retried, row, rows, second, source, x.
Calls/effect boundaries: (self.root / '.aegis').symlink_to, (self.root / '.aegis').unlink, (self.root / 'src/new.rs').unlink, (self.root / 'src/runtime.rs').symlink_to, (self.root / 'src/runtime.rs').unlink, Path, Path(result['path']).read_text, SimpleNamespace, all, entries.values, first['text'].encode, hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, ids.index, json.dumps, json.loads, len, list, load_profile, os.utime, outside.iterdir, outside.mkdir, patch, path.read_bytes, path.read_text, path.stat, path.write_text, self.assertEqual, self.assertFalse, self.assertGreaterEqual, self.assertIn, self.assertLess, self.assertLessEqual, self.assertNotEqual, self.assertTrue, self.call, self.subTest, self.write, set, str, subprocess.run, sys.path.insert, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0]::FunctionDef

Source: `infra/tests/test_destiny.py:49`; AST `2c7ccca995676219f2f0172de310b9659a4a89da3a1a68e808b05ca0a775e6a7`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FRAMEWORK, Path, SimpleNamespace, document, entries, first, fixture, identity, json, load_profile, patch, r, result, row, rows, second, self, source, str, sys, work_queue. Outputs/bindings: document, entries, first, fixture, identity, r, result, row, rows, second, source.
Calls/effect boundaries: Path, Path(result['path']).read_text, SimpleNamespace, entries.values, json.loads, load_profile, patch, self.assertEqual, self.assertFalse, self.assertTrue, self.write, str, sys.path.insert, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[0]::Expr

Source: `infra/tests/test_destiny.py:50`; AST `72f5072e9b9b1f9f02683333b4a822b08014a8b94f58caafb68b8b5a5ab20848`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FRAMEWORK, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[0].value::Call

Source: `infra/tests/test_destiny.py:50`; AST `96f079bc5f0514dd302df1d7cb89240f40008437bcbd311f1877decc91bb5d77`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[0].value.args[1]::Call

Source: `infra/tests/test_destiny.py:50`; AST `f23fe396ae12e6e752ea3a84527eb2559f24e1e2785aa55ff4b4c998eda0c0aa`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FRAMEWORK, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[1]::ImportFrom

Source: `infra/tests/test_destiny.py:51`; AST `fad6498e106b1798122c37d53dfe2785bfa2d2e049e8bc618dbf12706e84ddaa`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[2]::ImportFrom

Source: `infra/tests/test_destiny.py:52`; AST `05e9642838c6434f3e54a3cae3a7d134214b846b7a2f7a8877d63941a7b5c06e`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[3]::Assign

Source: `infra/tests/test_destiny.py:53`; AST `6bbd446adf8cebf553baf59053525644a9c1698b292a000bf44a5ad63849767e`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[4]::Assign

Source: `infra/tests/test_destiny.py:54`; AST `69d287f7e77c8384c9284698e86d5aab7e908b39c2db9d79361ad9c93c5bd1a2`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source. Outputs/bindings: first.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[5]::Assign

Source: `infra/tests/test_destiny.py:55`; AST `6bde3c7db2147ffc30bbf7ea12500d146543f566373df64b8abb4eae1966743b`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source. Outputs/bindings: second.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[6]::Expr

Source: `infra/tests/test_destiny.py:56`; AST `6fc1ed4115fc6019be50b649bc00607335a0133b63747eaf7eca6919b4de9c6a`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self, source. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[6].value::Call

Source: `infra/tests/test_destiny.py:56`; AST `01d20c6528d7e7937fd9b00bb58f09178aa0c8e26243f7ffc3ec4f78aa7e5be3`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self, source. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[7]::Assign

Source: `infra/tests/test_destiny.py:58`; AST `9ff3c704651be2238491ff8d085a90c25ca3cad226ecebf382eade4e3d34f5f6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, fixture, identity, second, source. Outputs/bindings: fixture, identity, rows.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[7].value::ListComp

Source: `infra/tests/test_destiny.py:58`; AST `a8e1e53e1d0a118f96aac80b15257215415a58631491704ca434f658afc75106`.

Rust module: `infra::tests::test_destiny`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: first, fixture, identity, second, source. Outputs/bindings: fixture, identity.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[14].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8]::With

Source: `infra/tests/test_destiny.py:62`; AST `a574a2c7dcf4c53178ed44cb12e92e8f5f03b33398ec6f394b028a4703f67e77`.

Rust module: `infra::tests::test_destiny`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: SimpleNamespace, load_profile, patch, rows, self, work_queue. Outputs/bindings: result.
Calls/effect boundaries: SimpleNamespace, load_profile, patch, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[14].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8].items[0].context_expr::Call

Source: `infra/tests/test_destiny.py:62`; AST `310191987b3cb49f0d6b41e2d995b925d255fda70775b5a3e42578b44f2d2bbc`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, rows. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8].body[0]::Assign

Source: `infra/tests/test_destiny.py:63`; AST `aa0d4793ccb27e706874d8d1717abe7ec6ece3dc032f2af2044416ba406f4068`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SimpleNamespace, load_profile, self, work_queue. Outputs/bindings: result.
Calls/effect boundaries: SimpleNamespace, load_profile, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8].body[0].value::Call

Source: `infra/tests/test_destiny.py:63`; AST `1a3013362529eb0a60b368dea4d136d4e9ecf776c543aeebb36d8935bc6262f5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace, load_profile, self, work_queue. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace, load_profile, work_queue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8].body[0].value.args[1]::Call

Source: `infra/tests/test_destiny.py:63`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[8].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[8].body[0].value.args[2]::Call

Source: `infra/tests/test_destiny.py:63`; AST `7095862a050da0c72c11eef163f90383777a34378e4884e743961cbb9ffc84c1`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[8].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[9]::Expr

Source: `infra/tests/test_destiny.py:64`; AST `73ece4a7b9167fff6ce6c119574e78986dff74ecbda0f6807ea51aa4936fa337`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[9].value::Call

Source: `infra/tests/test_destiny.py:64`; AST `4e09ed6a56959f0ae46b0aba76bfdc8685ce04378c5894ef59d689a560941a45`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[10]::Assign

Source: `infra/tests/test_destiny.py:65`; AST `ee18abb242fac1cabf14640cbed8d0cb5b53b7100253229aadcf0d2e75a54616`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, json, result. Outputs/bindings: document.
Calls/effect boundaries: Path, Path(result['path']).read_text, json.loads.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[10].value::Call

Source: `infra/tests/test_destiny.py:65`; AST `2f39c993c750f124a7506777e0657882c59bc8324bb600acf8151e27f3a9a4f5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, json, result. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(result['path']).read_text, json.loads.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[10].value.args[0]::Call

Source: `infra/tests/test_destiny.py:65`; AST `87e1f941402a2d0e40c9dca1bd5c291126456fdf314f83b8d7a66d2786dff995`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, result. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(result['path']).read_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[10].value.args[0].func.value::Call

Source: `infra/tests/test_destiny.py:65`; AST `d17e839db22d186b3eb65c05f22d631c074c73d00508ba0376075d715a902cd5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, result. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[10].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[11]::Assign

Source: `infra/tests/test_destiny.py:66`; AST `e0481edc4d32e38f63fd75f4bc31f1b38dac31b1460f1f29c1048c577a09b0bb`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: document, r. Outputs/bindings: entries, r.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[11].value::DictComp

Source: `infra/tests/test_destiny.py:66`; AST `eb02dbebaec0a34f2b41d8d0ee5bdea3dba6c846af1d17b1f5332735f22604bf`.

Rust module: `infra::tests::test_destiny`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: document, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[14].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[12]::Expr

Source: `infra/tests/test_destiny.py:67`; AST `b86d7c829b298e9c6c09e708447c8fc3fcab40c2ba547b26955e5a9822419ef1`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[12].value::Call

Source: `infra/tests/test_destiny.py:67`; AST `e5c77c6c7157b6896a4f9de38d610f99c1a9f1664897bb493531c141a53ed031`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[13]::Expr

Source: `infra/tests/test_destiny.py:68`; AST `bd7bef6f1483b1f010c6e906d210c5bcb69cb06824b3115da5a1132c3eab3432`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[13].value::Call

Source: `infra/tests/test_destiny.py:68`; AST `90e2e03629fcf2795cf48070198920f0beee35ee993f2ec7a45396840aab1327`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14]::For

Source: `infra/tests/test_destiny.py:69`; AST `0906020e2381ad7955d20f2577f7b7e3f9a903b3a61ce09967cd7457505d502a`.

Rust module: `infra::tests::test_destiny`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: entries, row, self. Outputs/bindings: row.
Calls/effect boundaries: entries.values, self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[14].body[0].body[14]; no call, error or mutation may be omitted. Iteration: row in entries.values()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].iter::Call

Source: `infra/tests/test_destiny.py:69`; AST `912d737e9726e2f2d732aff0f31a00c1fa6c57f79ed844957d40ddd4ccdd4c3e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries. Outputs/bindings: (none).
Calls/effect boundaries: entries.values.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[14].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[0]::Expr

Source: `infra/tests/test_destiny.py:70`; AST `a295f94ed184eeb03ce85e859440fc90aecb3bf52d20325062e862a889af1858`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[0].value::Call

Source: `infra/tests/test_destiny.py:70`; AST `bc99272db0f3003fb19f25c88ea654ffa2af60c86f1385a8f05bd022003d3e29`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[1]::Expr

Source: `infra/tests/test_destiny.py:71`; AST `e54b501d9443550edd49335891d3d88b16481e710673c78b123a6a805d207fb9`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[1].value::Call

Source: `infra/tests/test_destiny.py:71`; AST `5ad52adcbed718d9a3386584506a62c409fe6ec8d8ea4c05da9ef66c4a78b006`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[2]::Expr

Source: `infra/tests/test_destiny.py:72`; AST `9d1bd6c071de89ccfa5b05c1bceb2e1702b1f5c1bba3209914e5f5aeef3ec078`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_actual_queue_keeps_fixture_identities_and_independent_lanes::root.body[14].body[0].body[14].body[2].value::Call

Source: `infra/tests/test_destiny.py:72`; AST `2dba1d710241c9ea384f1d48074b6acef5549dd96fd62714f007bedd08808495`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1]::FunctionDef

Source: `infra/tests/test_destiny.py:74`; AST `a218d8ad1cb50d3aad7ae80e66e6faee9f6ebd69672fa342bb39116e6b9931aa`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, ids, len, plan, row, self, set. Outputs/bindings: ids, plan, row.
Calls/effect boundaries: all, ids.index, len, self.assertEqual, self.assertLess, self.assertTrue, self.call, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[0]::Assign

Source: `infra/tests/test_destiny.py:75`; AST `a1105286cf1419ac37831d37fa6d1f1f58e149d582475f7ae1dd2d924cffc205`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: plan.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[0].value::Call

Source: `infra/tests/test_destiny.py:75`; AST `b6652e6bfef3ddbc2f5da931d7269f9a8376c8dd32a89a2a03dab23cfc73b4b0`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[1]::Assign

Source: `infra/tests/test_destiny.py:76`; AST `ed3a917cc91f4302e77ec2062dbebe4fc850421266dfcd0c49b0ec2607ceafa6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, row. Outputs/bindings: ids, row.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[1].value::ListComp

Source: `infra/tests/test_destiny.py:76`; AST `f9c3b525a6582c28c9b4722f7a0df0390aeee94844ded93bcc4ef0941326ce25`.

Rust module: `infra::tests::test_destiny`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: plan, row. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[14].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[2]::Expr

Source: `infra/tests/test_destiny.py:77`; AST `a8ebb2b7f039acbf1a97a1865344581d589af5f7b174cf78f4de674e1abad3f6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, len, self, set. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[2].value::Call

Source: `infra/tests/test_destiny.py:77`; AST `1f35ae958657a9b3e3d583c8ccf3072d6abbb273fcfdce70a89e32b46d1fe3a8`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, self, set. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny.py:77`; AST `e9ff8c6d4cd447580e3ae476d39cdd538e64139104de929c715ef5318d853424`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[2].value.args[1]::Call

Source: `infra/tests/test_destiny.py:77`; AST `392a9c6c899c1b887c4cb41a948a33de0352ff7c7be2a32c7a4d965ee6b3a8a2`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[2].value.args[1].args[0]::Call

Source: `infra/tests/test_destiny.py:77`; AST `b5d0e953c49c3b05c4f5acc7b5c0af435cfb16d965600b49af73f1b9fe8b980e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[3]::Expr

Source: `infra/tests/test_destiny.py:78`; AST `dc201772721a59daf62b9deefc5d93bd4805176643b469e7865cbb7943a9601c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[3].value::Call

Source: `infra/tests/test_destiny.py:78`; AST `bad7cc8f0d42f11ae55e6d47a004b411affa72d4689ec6284593da0f39ccfd7e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue, set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[3].value.args[0].comparators[0]::Call

Source: `infra/tests/test_destiny.py:78`; AST `b5d0e953c49c3b05c4f5acc7b5c0af435cfb16d965600b49af73f1b9fe8b980e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[4]::Expr

Source: `infra/tests/test_destiny.py:79`; AST `a48b52e534e4cba6ca834e365feb0ec509e222131de0ada357835dabbc5eefa1`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: ids.index, self.assertLess.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[4].value::Call

Source: `infra/tests/test_destiny.py:79`; AST `f131ba036dff973d6d6b13225ee29240b22c35750d9620ff2d344b6cacec14cf`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: ids.index, self.assertLess.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny.py:79`; AST `46b10d61944e3f855652c2edca60a54a7c212e029b0064db37569a08dedaae77`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids. Outputs/bindings: (none).
Calls/effect boundaries: ids.index.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[4].value.args[1]::Call

Source: `infra/tests/test_destiny.py:79`; AST `6ccd0579fa404fe212b491b6cf66ccbfbd5824278f4944d39ef8d4805590f8d7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids. Outputs/bindings: (none).
Calls/effect boundaries: ids.index.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[5]::Expr

Source: `infra/tests/test_destiny.py:80`; AST `c13b8949eb3c03baeb0960589e77ad030b5d2991159115b5faa03a90d01c0f3e`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[5].value::Call

Source: `infra/tests/test_destiny.py:80`; AST `013fe08713247bf0d177ec6b9274de6e17d24547942d69f94a815cdf7ca415b1`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[6]::Expr

Source: `infra/tests/test_destiny.py:81`; AST `5630181d1d7f2bdf85d6e6b2217b297696b6846383aee644ea50b33bf3e9e099`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, plan, row, self. Outputs/bindings: row.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[6].value::Call

Source: `infra/tests/test_destiny.py:81`; AST `8f13e696951150a45a1f0505286bfe77a500afe2fe52b97a213fd1aeaa98ea0f`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, plan, row, self. Outputs/bindings: row.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[6].value.args[0]::Call

Source: `infra/tests/test_destiny.py:81`; AST `0b6fb3c36350848f2a7488ce1ae569d5fab1f81d5855bd813260f7b40ecc35ff`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, plan, row. Outputs/bindings: row.
Calls/effect boundaries: all.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_runtime_plan_is_ordered_and_deduplicated::root.body[14].body[1].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_destiny.py:81`; AST `f942392bc59db9fd5e9afc090a15c4fdba74076ef7a56f579df6f3aa073864c9`.

Rust module: `infra::tests::test_destiny`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: plan, row. Outputs/bindings: row.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[14].body[1].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2]::FunctionDef

Source: `infra/tests/test_destiny.py:83`; AST `754f7c53fa07ccbf9114634c5baacc1f336eefb7c7173ef64e6df35fce2c0972`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ids, self, x. Outputs/bindings: ids, x.
Calls/effect boundaries: self.assertTrue, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2].body[0]::Assign

Source: `infra/tests/test_destiny.py:84`; AST `1a25e349019f4167b9aaed519c3c2ba35faa4c290d400a16bbf313973fed5447`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, x. Outputs/bindings: ids, x.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2].body[0].value::SetComp

Source: `infra/tests/test_destiny.py:84`; AST `f0cebda95c6653553b28dd7447e23f2bb64b2b99af15aea202014eb860691864`.

Rust module: `infra::tests::test_destiny`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: self, x. Outputs/bindings: x.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2].body[0].value.generators[0].iter.value::Call

Source: `infra/tests/test_destiny.py:84`; AST `639b95d841886c80b05652ba99c8dbbf01cbc0f61c8226b0337a2d66c47f2c92`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].value.generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2].body[1]::Expr

Source: `infra/tests/test_destiny.py:85`; AST `336f56bfad4f2147f84087f5d4b168f559bdd282b2227eaf0d1b31abc46fe7f8`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_python_geometry_routes_to_cross_language_contracts::root.body[14].body[2].body[1].value::Call

Source: `infra/tests/test_destiny.py:85`; AST `414e014223a9d2a4e3254186e2689d4a1eab34b78fde57338e83fe24d9b552ed`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ids, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3]::FunctionDef

Source: `infra/tests/test_destiny.py:87`; AST `b74138c0edae4f1d08ae174864b34d21ee4dfa684ec49eca032560912b66ba4a`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: plan, self, x. Outputs/bindings: plan, x.
Calls/effect boundaries: self.assertIn, self.assertTrue, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[0]::Assign

Source: `infra/tests/test_destiny.py:88`; AST `e03d73f5e6ced9d795fe65840bacbcec08e508c64b4c3ed03b988f5cfdb7fa18`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: plan.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[0].value::Call

Source: `infra/tests/test_destiny.py:88`; AST `f7802792788b214c2ed605070ff78d07e9cefd3c79cc1f84007e2de006a619ec`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[1]::Expr

Source: `infra/tests/test_destiny.py:89`; AST `965f2920e9d827bc5fbe7f59f812cefbb64836f9a4c4ae9aba2ccbfa02b769a2`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[1].value::Call

Source: `infra/tests/test_destiny.py:89`; AST `3fdbff2b2c90f40bb86967af03dfd8b2b30ad08b37643b28b6ac7591027b415e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[2]::Expr

Source: `infra/tests/test_destiny.py:90`; AST `00eab680b7da47cd344d35b1592321464b0db87fb51696fbfa1432ad4d30a013`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[2].value::Call

Source: `infra/tests/test_destiny.py:90`; AST `faa90c409765cf5acd755eaeaad3449d429cf9819907dcae27b40b7995e93b5f`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[3]::Expr

Source: `infra/tests/test_destiny.py:91`; AST `847c40125c0501704003e6308353cc48b4ccaf20d29d907faf3777a282ba1b64`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, self, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[3].value::Call

Source: `infra/tests/test_destiny.py:91`; AST `7e3801b36c4e8f067d7af3bd4c2ffe4b6fea89f0cea8e8ae5ab52e2f494d2554`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan, self, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_paths_fail_conservatively_and_empty_is_not_pass::root.body[14].body[3].body[3].value.args[1]::SetComp

Source: `infra/tests/test_destiny.py:91`; AST `c9764106a7629989c28bc192742a24355f4c0311b283568bdc17e640b0c7be76`.

Rust module: `infra::tests::test_destiny`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: plan, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[3].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4]::FunctionDef

Source: `infra/tests/test_destiny.py:93`; AST `c53fef302c800ba0cfde36760cdc721a0a4bc1fa04cb20727ff883cf9c3a95bf`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: len, plan, self, x. Outputs/bindings: plan, x.
Calls/effect boundaries: len, self.assertGreaterEqual, self.assertTrue, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[0]::Assign

Source: `infra/tests/test_destiny.py:94`; AST `0c82f0dd6c5521127f93adc78544e89f8646d27a2650600170babb4d21731095`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: plan.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[0].value::Call

Source: `infra/tests/test_destiny.py:94`; AST `e0c6279ae8124ac1d78fa4fdc57ec6fae22747ebd52b16fe7197bd156e216823`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[1]::Expr

Source: `infra/tests/test_destiny.py:95`; AST `47576b074ec34e0e29753d641e5511231f5af5d28df0a841be2db53d08395c2f`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: plan, self, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[1].value::Call

Source: `infra/tests/test_destiny.py:95`; AST `02406ce94d8d84b4ea826df56e78c7c72cc06e3d0b115636bbc109d69d6867ec`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: plan, self, x. Outputs/bindings: x.
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[1].value.args[0].comparators[0]::SetComp

Source: `infra/tests/test_destiny.py:95`; AST `c9764106a7629989c28bc192742a24355f4c0311b283568bdc17e640b0c7be76`.

Rust module: `infra::tests::test_destiny`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: plan, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered SetComp evaluation at root.body[14].body[4].body[1].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[2]::Expr

Source: `infra/tests/test_destiny.py:96`; AST `7e3c24d0ea04c85f1facf72e872cf3ae1bced492b5a1e49bb9b1c8cf473b7970`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertGreaterEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[2].value::Call

Source: `infra/tests/test_destiny.py:96`; AST `917431e9741116e022aa92b12fa86413064e97ffa3f6e0ef6d9c37dc337a81b6`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, plan, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertGreaterEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_release_includes_external_and_platform_gates::root.body[14].body[4].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny.py:96`; AST `95c8f2c55914d4e81947cfe1eadf9443875a3d782750117270b8fb99866805a8`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, plan. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5]::FunctionDef

Source: `infra/tests/test_destiny.py:98`; AST `0ac80eec663d623387b60d3fdaa79b85b1f12cc558913eefb7de29f71cf14ebc`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: path, self. Outputs/bindings: path.
Calls/effect boundaries: self.assertEqual, self.call, self.subTest.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0]::For

Source: `infra/tests/test_destiny.py:99`; AST `ada3a1074c9edcf4df63893f1bab62d48545f865cb14d902cea3480b40db3b6b`.

Rust module: `infra::tests::test_destiny`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: path, self. Outputs/bindings: path.
Calls/effect boundaries: self.assertEqual, self.call, self.subTest.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[14].body[5].body[0]; no call, error or mutation may be omitted. Iteration: path in ('../secret', '/tmp/secret', 'src/../../secret', 'C:\\outside\\secret')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0].body[0]::With

Source: `infra/tests/test_destiny.py:100`; AST `573828269187a43413b4f867c2a678ecfdcbb7aa6a025f21eee1446e055ee9e1`.

Rust module: `infra::tests::test_destiny`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call, self.subTest.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[14].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_destiny.py:100`; AST `f217da1f277053e7b82b79a91960719f9650ab098eaad15e9afb698c9e211590`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_destiny.py:101`; AST `9c3b5273e97c30f95b747a955fe6429c6a9142036e22a420df0e4f08f207ea2c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_destiny.py:101`; AST `c57416f02e642b15cc1b4e3d764a19ade248ba211f92adcbaffea43d87a1bb1d`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_changed_paths_cannot_escape::root.body[14].body[5].body[0].body[0].body[0].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:101`; AST `5e2710589aaeac76df4f52c18c267d1890ccbedb7cce738c4c9e23ad6f9a06d1`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].body[0].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6]::FunctionDef

Source: `infra/tests/test_destiny.py:103`; AST `4240f5b51f7c24f699e9ba6cbf9c19ba18da07dca230e677168343781c15ef24`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: first, fresh, second, self. Outputs/bindings: first, fresh, second.
Calls/effect boundaries: self.assertEqual, self.assertFalse, self.assertNotEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[0]::Assign

Source: `infra/tests/test_destiny.py:104`; AST `182161a5c7b06b29079deb8e4bebe9d9928e23bf36c832c09f37089189d45597`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: first.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[0].value::Call

Source: `infra/tests/test_destiny.py:104`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[1]::Expr

Source: `infra/tests/test_destiny.py:105`; AST `98430267c67ace1af95e867503785af4153b96885d0e142d2b1939c41f2c3bca`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[1].value::Call

Source: `infra/tests/test_destiny.py:105`; AST `2ac977ada1cc4e48b2379b03b2fca68bee7d4098e23d24a242eb2523015b4a2a`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[2]::Expr

Source: `infra/tests/test_destiny.py:106`; AST `351eef7e080c8f9adea663dbb51a83fcbe766748b4d0087632e4f7ad69116b04`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[2].value::Call

Source: `infra/tests/test_destiny.py:106`; AST `5445268a421f9f23352c6bd87a4ee69216f85370b7168b21f8eca1f1e6cf7eb2`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[3]::Assign

Source: `infra/tests/test_destiny.py:107`; AST `63b4b833f92705107e561af2552a57616d64b855e430f5e381882fec61c233b3`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: second.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[3].value::Call

Source: `infra/tests/test_destiny.py:107`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[4]::Expr

Source: `infra/tests/test_destiny.py:108`; AST `a729fcb9bc8c1b2297fdbd8a00502e5e96c1d966f17576d8515d40ee4eb683df`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[4].value::Call

Source: `infra/tests/test_destiny.py:108`; AST `0d93c6d4c5ce2cdd14cef1118f81aa38ddeab608ecf2ca4ae4e4de8381e757a1`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[5]::Expr

Source: `infra/tests/test_destiny.py:109`; AST `3ded47248835a0e6e5221f3f1c529eb1cd2b3fc74b820a7bd6d6488dd2d66b63`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[5].value::Call

Source: `infra/tests/test_destiny.py:109`; AST `db48fb19198388e7cdd0e0936e03f5981bbdcc0cf79d6574bbe6f5be1963bf66`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[6]::Expr

Source: `infra/tests/test_destiny.py:110`; AST `af075aacac3e1d98222ef9e1c944f2c018c57e0ad5e05b1af469feb0b78622e9`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[6].value::Call

Source: `infra/tests/test_destiny.py:110`; AST `5f5879fb8e293a7fb790f161e8038024b2e8eeeebeb0a98be82569519be056b8`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[7]::Assign

Source: `infra/tests/test_destiny.py:111`; AST `cd14d83660b81934d083c6786767d5983d2c16b4e3934f87a3769b504f09f83e`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: fresh.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[7].value::Call

Source: `infra/tests/test_destiny.py:111`; AST `8409949bfefd7456f039466f790a933dfc108296210967b805e41a07eab2f669`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[8]::Expr

Source: `infra/tests/test_destiny.py:112`; AST `6adcecaeb52382dd182d9178b9f8dcb630cbe8f62926e5c1edead46971be51c5`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, fresh, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_marker_success_is_an_observation_and_reuse_is_explicit::root.body[14].body[6].body[8].value::Call

Source: `infra/tests/test_destiny.py:112`; AST `ffbfea240bf4dd949b74d66e544a2f7419ee9f0f427f2b6ed32f85951bc4b6fb`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, fresh, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7]::FunctionDef

Source: `infra/tests/test_destiny.py:114`; AST `f983fa1f78fdb72febccdf219fb4843f7a139d02dbf997bc55afbb25c58d4654`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: contents, previous, relative, result, self. Outputs/bindings: contents, previous, relative, result.
Calls/effect boundaries: (self.root / 'src/new.rs').unlink, self.assertEqual, self.assertNotEqual, self.call, self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[0]::Assign

Source: `infra/tests/test_destiny.py:115`; AST `dc98c67dcd36d957b845eeed818455408afb00d13d0773a8d1d564ed1b97c490`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: previous.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[0].value.value::Call

Source: `infra/tests/test_destiny.py:115`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1]::For

Source: `infra/tests/test_destiny.py:116`; AST `3a75ebc503b834484e5c50297e6b1da9df3dfe308743708ed2e143efda54f6e1`.

Rust module: `infra::tests::test_destiny`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: contents, previous, relative, result, self. Outputs/bindings: contents, previous, relative, result.
Calls/effect boundaries: self.assertEqual, self.assertNotEqual, self.call, self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[14].body[7].body[1]; no call, error or mutation may be omitted. Iteration: (relative, contents) in (('src/runtime.rs', 'pub fn tick() { panic!() }\n'), ('src/new.rs', '// new\n'), ('.cargo/config.toml', '[net]\noffline=true\n'))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[0]::Expr

Source: `infra/tests/test_destiny.py:118`; AST `45b201049e72bc045f83fb0ebc3b376e61f69e02c8518658bd4b3c646fb5da3c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: contents, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[0].value::Call

Source: `infra/tests/test_destiny.py:118`; AST `15d4af289657f4c9a6f5cd0ce5d9460a1a11908c7694934f634cbd557e6ccfe5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: contents, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[1]::Assign

Source: `infra/tests/test_destiny.py:119`; AST `6095e5e6f3a12b2180157bd3e95d20a1ce808ad0a31224430858d163bcc246db`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[1].value::Call

Source: `infra/tests/test_destiny.py:119`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[2]::Expr

Source: `infra/tests/test_destiny.py:120`; AST `0b344111dd1ba62341940e971d207fa8d3a3768016446528f22928dfc10f85c2`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[2].value::Call

Source: `infra/tests/test_destiny.py:120`; AST `f8c3d5410f824e84f4ca68b9a3e12d6a3c2f72ca1d17745bec9e8767c2177926`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[3]::Expr

Source: `infra/tests/test_destiny.py:121`; AST `7830781f89933288d3086b4d9287973ceb253104f64001ea9b7df5b34f6da669`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[3].value::Call

Source: `infra/tests/test_destiny.py:121`; AST `1f410fc09f0b39f4e27a624080ac2becb57414842b305cb109b1b9249c4ddb00`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[1].body[4]::Assign

Source: `infra/tests/test_destiny.py:122`; AST `0d5bfc6c4e17eab2e590771906da94416bd6985e87f052b9484170c7051266bb`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: previous.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[2]::Expr

Source: `infra/tests/test_destiny.py:123`; AST `75b48b8e1d3e582a914dbab45a5a917cd0c900277ea03571cd38ca12f0dcc937`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/new.rs').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[2].value::Call

Source: `infra/tests/test_destiny.py:123`; AST `79d87fc5fc9c2b9f099ebf9ff88065cc8c181adb902d985089e587093aa27011`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/new.rs').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[3]::Expr

Source: `infra/tests/test_destiny.py:124`; AST `bac6816871038d67f38b7da2ef52e0a64b231d5e476109f7a80710d7921e7d43`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: previous, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[3].value::Call

Source: `infra/tests/test_destiny.py:124`; AST `244922e019975a1e6f70b9a6fe0b4da82d7ec7ea3fec5e4030f39ea8b9fc8144`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: previous, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_edit_add_delete_and_ignored_cargo_configuration_invalidate::root.body[14].body[7].body[3].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:124`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8]::FunctionDef

Source: `infra/tests/test_destiny.py:126`; AST `18ecb4f38e0f96ffc4c19003f82cd6df956a17bbf42d37ae0eb54dee483aecdc`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: first, retried, second, self. Outputs/bindings: first, retried, second.
Calls/effect boundaries: self.assertEqual, self.assertFalse, self.assertNotEqual, self.call, self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[0]::Expr

Source: `infra/tests/test_destiny.py:127`; AST `e929f7f3859792b1f323edae35d65800daf5a3d8c1baaf41f3735020592c2654`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[0].value::Call

Source: `infra/tests/test_destiny.py:127`; AST `a0f1c14c798b63368ff30c6fa7a491a19b72e000df517e5d85ca15d97c3d2b5f`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[1]::Assign

Source: `infra/tests/test_destiny.py:128`; AST `1c25925d3fad524df67a0d1aa3a4a7859a3b5e153cb01a1a993ad7da1faaa3c9`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: first.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[1].value::Call

Source: `infra/tests/test_destiny.py:128`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[2]::Expr

Source: `infra/tests/test_destiny.py:129`; AST `4e9bc1bb42e5ae15d5680be25206aec97534d5bbbcf4a87f011cc99c028f818d`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[2].value::Call

Source: `infra/tests/test_destiny.py:129`; AST `846cd7804d096b3a1333b6b4879b818989c7050fe511277778f9040e59f209b6`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[3]::Assign

Source: `infra/tests/test_destiny.py:130`; AST `ab7bf42cf6bf54861b690e95051ca3b4a007850ab9033fd6917912ad3038c5d7`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: second.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[3].value::Call

Source: `infra/tests/test_destiny.py:130`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[4]::Expr

Source: `infra/tests/test_destiny.py:131`; AST `7f61514c28bfe7cb672b576ebedf0cafcdf8afd731a9597a9d3dfc8da5512b2f`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[4].value::Call

Source: `infra/tests/test_destiny.py:131`; AST `abb3569656b5d9727b2a804839a42a9024aca9ca24fad34d694b36e81c18fa7f`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[5]::Expr

Source: `infra/tests/test_destiny.py:132`; AST `af075aacac3e1d98222ef9e1c944f2c018c57e0ad5e05b1af469feb0b78622e9`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[5].value::Call

Source: `infra/tests/test_destiny.py:132`; AST `5f5879fb8e293a7fb790f161e8038024b2e8eeeebeb0a98be82569519be056b8`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[6]::Assign

Source: `infra/tests/test_destiny.py:133`; AST `948f2341982652abc48bdc3841467271966e3adea47482ed33d61a9a9d151a8c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: retried.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[6].value::Call

Source: `infra/tests/test_destiny.py:133`; AST `81df13a5560d8efd5f5692164441954123b5b8bc2befe86fc1568db50c49e070`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[7]::Expr

Source: `infra/tests/test_destiny.py:134`; AST `89147790e4a8681fb5e3f34e6b297857e56a6de128692a2d4580c3ab59c23abf`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retried, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[7].value::Call

Source: `infra/tests/test_destiny.py:134`; AST `fab4a86de59cc5655cf8c024dde78843d70aee51d2cc9bcd8bd761400d6af5ea`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retried, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[8]::Expr

Source: `infra/tests/test_destiny.py:135`; AST `34ae91817cb477009771b6640581cf4a09c2648979ab8cae0d73f7d7bc6984c7`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, retried, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_failure_is_not_retried_implicitly_or_promoted::root.body[14].body[8].body[8].value::Call

Source: `infra/tests/test_destiny.py:135`; AST `36751839062914e42e3958eb39930b8fa8d7b23121fa2265e30008b4adc9b02f`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, retried, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9]::FunctionDef

Source: `infra/tests/test_destiny.py:137`; AST `e4af27e410e10824e70432fb97a53e4c2a08a88266e1d72661267bbcfeaa4a76`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: first, self, subprocess. Outputs/bindings: first.
Calls/effect boundaries: self.assertEqual, self.assertNotEqual, self.call, self.write, subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[0]::Assign

Source: `infra/tests/test_destiny.py:138`; AST `182161a5c7b06b29079deb8e4bebe9d9928e23bf36c832c09f37089189d45597`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: first.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[0].value::Call

Source: `infra/tests/test_destiny.py:138`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[1]::Expr

Source: `infra/tests/test_destiny.py:139`; AST `dc87017e55a3467c9b4551e90d3a7481766966e0d55a46d959d8bb2eaf6f8d2b`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[1].value::Call

Source: `infra/tests/test_destiny.py:139`; AST `265c42420471f12aa9a6c06933fff405f44383e26fb8235d113ee8152a6aada7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[2]::Expr

Source: `infra/tests/test_destiny.py:140`; AST `65558c97e7b40f28a2bc1acc395aa44b7f2f0b7a1339cca6088fb75f8c394cb6`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[2].value::Call

Source: `infra/tests/test_destiny.py:140`; AST `122e3009d5c22822abe948bc0d34eb9ec7d626dc96363a8c2c08223d0595a5ec`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[2].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:140`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[3]::Expr

Source: `infra/tests/test_destiny.py:141`; AST `f4bf813d1beacbc5ce91a6b0be57164003d30b7d993193fd5b298db4690eef7b`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[3].value::Call

Source: `infra/tests/test_destiny.py:141`; AST `c877dfae6d9d506572600367efa0df84385c8cbc7219cb3e1dc176b38fc36e0a`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[4]::Expr

Source: `infra/tests/test_destiny.py:142`; AST `94cf81e325947bcda46bcc987b626dde66ac709d38668dd4869eda379c9b669e`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[4].value::Call

Source: `infra/tests/test_destiny.py:142`; AST `26e1a5ac65e136b4edb993b56a298331a1d9dd53b7dd43687375fd893613fccf`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_generated_outputs_do_not_invalidate_untracked_but_tracked_do::root.body[14].body[9].body[4].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:142`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10]::FunctionDef

Source: `infra/tests/test_destiny.py:144`; AST `03f761328a18ed0187885d942a3f97b7aaa99423628a713c2aaa12d0041b5c46`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: data, json, path, report, self. Outputs/bindings: data, path, report.
Calls/effect boundaries: json.dumps, json.loads, path.read_text, path.write_text, self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[0]::Assign

Source: `infra/tests/test_destiny.py:145`; AST `b9dcc95c72f35e80bfb8908d21456763fec3d13ec097e11e655254e3a4008dfe`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: report.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[0].value::Call

Source: `infra/tests/test_destiny.py:145`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[1]::Assign

Source: `infra/tests/test_destiny.py:146`; AST `6788d86bc00a19cbfce54299d4dc71c5ec919e0fb1ac9a43768ad74a15759dda`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: report, self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[2]::Assign

Source: `infra/tests/test_destiny.py:147`; AST `1beb99e24c7fb19acb824fb75ad0b7796ac65edcef53ed15f0a1c714300db001`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: data.
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[2].value::Call

Source: `infra/tests/test_destiny.py:147`; AST `4a076f3fdf20f1dd94162a22f2b9944a159c045ed6266d1cb7ac9b597c2ea970`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny.py:147`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[3]::Assign

Source: `infra/tests/test_destiny.py:148`; AST `6df8b43b66c0f903e0ee4e837cc2d73cc7dd23b0d7528c68b2c891622fa0df27`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[4]::Expr

Source: `infra/tests/test_destiny.py:149`; AST `574aa6d25cc8f41c9b3d62979f20e15e222375344e09d3f9b8aeb766dbf8740f`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: data, json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[4].value::Call

Source: `infra/tests/test_destiny.py:149`; AST `b95299993a945f91fc85f55d0c899dc3c829942b8c6a6f3704557e8a4ba00e04`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny.py:149`; AST `b17242147d72229e62d2e4e84cff51ec9151bb5ca1dcce026b7118911a8429e6`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: data, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[5]::Expr

Source: `infra/tests/test_destiny.py:150`; AST `fd53fd8af409653b0a87a0370e9ce189bf149d9470803a2d26e6b8cdbe582507`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[5].value::Call

Source: `infra/tests/test_destiny.py:150`; AST `2313b002d1d6973486e7fc4915dcb513b96478c83ad3ad23b024a356f1fa1a04`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_cache_tampering_is_rejected::root.body[14].body[10].body[5].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:150`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11]::FunctionDef

Source: `infra/tests/test_destiny.py:152`; AST `1987672921d76db1090bb91052b3873681831ac91301c52c13dbebc3c3d18924`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, list, outside, self. Outputs/bindings: outside.
Calls/effect boundaries: (self.root / '.aegis').symlink_to, (self.root / '.aegis').unlink, (self.root / 'src/runtime.rs').symlink_to, (self.root / 'src/runtime.rs').unlink, Path, list, outside.iterdir, outside.mkdir, self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[0]::Assign

Source: `infra/tests/test_destiny.py:153`; AST `d0f746ffec230190e684d4078b177df36cb4ebf207b008e0a2b8f53401fbb422`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: outside.
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[0].value.left::Call

Source: `infra/tests/test_destiny.py:153`; AST `350af0ef58dfeabf82fa371e4d1a0525efa6d4376cbcb9b8ead747bbdeb7de21`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[1]::Expr

Source: `infra/tests/test_destiny.py:154`; AST `a1d8fb3c849c0c16fbd5497785da59337edbf591ece2d3690a0a45bf877e7a53`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outside. Outputs/bindings: (none).
Calls/effect boundaries: outside.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[1].value::Call

Source: `infra/tests/test_destiny.py:154`; AST `7bff71907fdb7e4033ce307625684d6f273a45de93ac58f241a84d0140731dde`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outside. Outputs/bindings: (none).
Calls/effect boundaries: outside.mkdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[2]::Expr

Source: `infra/tests/test_destiny.py:155`; AST `25352c9cdb44939bfee8d7c0b4fc32a42031d4fed24a1f98562481582817484a`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outside, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').symlink_to.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[2].value::Call

Source: `infra/tests/test_destiny.py:155`; AST `242dd7bde7ef8675a76909da89d5fc7b26c27bb5d19cbda3befdac16805b1001`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outside, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').symlink_to.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[3]::Expr

Source: `infra/tests/test_destiny.py:156`; AST `763719e493656acc34a538b110ecf586d94bce688da3934cd54c7112e28e97cf`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[3].value::Call

Source: `infra/tests/test_destiny.py:156`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[4]::Expr

Source: `infra/tests/test_destiny.py:157`; AST `4aa37feba67d8dcd343dd520b732c3196e6e4964df7094d6129082e5a11ca096`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, outside, self. Outputs/bindings: (none).
Calls/effect boundaries: list, outside.iterdir, self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[4].value::Call

Source: `infra/tests/test_destiny.py:157`; AST `d2092e10ba885da4854247970e3b6aadacca55d04a543127ed43a9d5c7568771`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, outside, self. Outputs/bindings: (none).
Calls/effect boundaries: list, outside.iterdir, self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[4].value.args[0]::Call

Source: `infra/tests/test_destiny.py:157`; AST `256800316db17a14a969cf361333197a5f431b1310568146dbc128c013fd8ba6`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, outside. Outputs/bindings: (none).
Calls/effect boundaries: list, outside.iterdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[4].value.args[0].args[0]::Call

Source: `infra/tests/test_destiny.py:157`; AST `96ddbd03d3ba2c6492d18462a02cbca409eb3e99e9eb17af85dd53ecbf73fc74`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outside. Outputs/bindings: (none).
Calls/effect boundaries: outside.iterdir.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[5]::Expr

Source: `infra/tests/test_destiny.py:158`; AST `c64d1294a584f82865b21c5b863773e66aefaa1e3a98bb97d09204de1c0fc7b2`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[5].value::Call

Source: `infra/tests/test_destiny.py:158`; AST `5e85b24b422593fe677e7af55f784fc756234aa302a3611818c7702485957827`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[6]::Expr

Source: `infra/tests/test_destiny.py:159`; AST `5892aca1293444f534b73272a4ae5c031c6aea75e02be4800f21233f3d2ec289`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/runtime.rs').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[6].value::Call

Source: `infra/tests/test_destiny.py:159`; AST `24005b03613c522d54c2be02f9073e894c0d381040b65e8f7b17f7ba841fe324`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/runtime.rs').unlink.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[7]::Expr

Source: `infra/tests/test_destiny.py:160`; AST `5ee71e9925c464a5e1c74e6e8db86e003d845bf7c710e729d2e42df05905acc4`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: outside, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/runtime.rs').symlink_to.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[7].value::Call

Source: `infra/tests/test_destiny.py:160`; AST `47482382f1c1f88a53f3a1b197966cc390ed20b68234de82d33f84760e6a434e`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: outside, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'src/runtime.rs').symlink_to.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[8]::Expr

Source: `infra/tests/test_destiny.py:161`; AST `763719e493656acc34a538b110ecf586d94bce688da3934cd54c7112e28e97cf`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_redirected_state_and_sources_fail_closed::root.body[14].body[11].body[8].value::Call

Source: `infra/tests/test_destiny.py:161`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[11].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12]::FunctionDef

Source: `infra/tests/test_destiny.py:163`; AST `0fb8a425a2847209c1b0c293fcacec3a7e07a37c78fb9e9d3a409bca742c33a9`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, first, hashlib, len, os, path, self. Outputs/bindings: before, first, path.
Calls/effect boundaries: first['text'].encode, hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, len, os.utime, path.read_bytes, path.stat, path.write_text, self.assertEqual, self.assertLessEqual, self.assertTrue, self.call, self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[0]::Assign

Source: `infra/tests/test_destiny.py:164`; AST `9492284f1356c5da26d74d6fa7b11040971e17dfad9cd6d44ae53575eaac2a85`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[0].value::Call

Source: `infra/tests/test_destiny.py:164`; AST `2b2ff03359842c905e761af8990ad390a1a8ba948b61c55df200f63451e2f430`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[1]::Assign

Source: `infra/tests/test_destiny.py:165`; AST `e74d90ce4386a4d616c159ad50f6ffc1f6763f57d453e3234414061850a80f1c`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: first.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[1].value::Call

Source: `infra/tests/test_destiny.py:165`; AST `a7607c86679a31ccf7e4dc6c0fb4250d6e1d3cd47281bdea0664e6029e8212af`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[2]::Expr

Source: `infra/tests/test_destiny.py:166`; AST `1336e87a4ac1049b7bc9d48ac0428c104b4a28fa9b9ca6d166fa3083b3858618`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, len, self. Outputs/bindings: (none).
Calls/effect boundaries: first['text'].encode, len, self.assertLessEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[2].value::Call

Source: `infra/tests/test_destiny.py:166`; AST `79c630133e90ba6bf15b1dcaf3458e8318047639e981cd26ee3f9dc0977717dc`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, len, self. Outputs/bindings: (none).
Calls/effect boundaries: first['text'].encode, len, self.assertLessEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[2].value.args[0]::Call

Source: `infra/tests/test_destiny.py:166`; AST `8beb68dbc41f25164f69a63887b5ce5fb4373a62e40118a8fbf9d8740e0add82`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, len. Outputs/bindings: (none).
Calls/effect boundaries: first['text'].encode, len.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[2].value.args[0].args[0]::Call

Source: `infra/tests/test_destiny.py:166`; AST `bc04595a044e603cfe6fd365e218be079afd56b180f91d642c59425233feaf9b`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first['text'].encode.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[3]::Expr

Source: `infra/tests/test_destiny.py:167`; AST `3a74bf753dc2abf903560c16492d4569c541df910f14e74da282f8bb0cd98d6a`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[3].value::Call

Source: `infra/tests/test_destiny.py:167`; AST `e229db3dd491063ce1563177f561db4b53246897b98e040a9f70a72978fa4623`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[4]::Expr

Source: `infra/tests/test_destiny.py:168`; AST `791c18acbf9750b462d852a6dab0f546110d45206991611a6ecc68971fb098cb`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, hashlib, path, self. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, path.read_bytes, self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[4].value::Call

Source: `infra/tests/test_destiny.py:168`; AST `1e19bb9ac8c3c6fbf124ebb277de6f9782ac77a8d0ca3ec8d0bd82ce232c45eb`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, hashlib, path, self. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, path.read_bytes, self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[4].value.args[1]::Call

Source: `infra/tests/test_destiny.py:168`; AST `e3df6d84750bc9b1dcb5c4ba5f588032030d7cd08ed852cb1297a60011703e55`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, hashlib.sha256(path.read_bytes()).hexdigest, path.read_bytes.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[4].value.args[1].func.value::Call

Source: `infra/tests/test_destiny.py:168`; AST `59e4f63783edebc00f4b4b816f155be4903d482bffc1cc84742b1e045970c0ef`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib, path. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256, path.read_bytes.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[4].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[4].value.args[1].func.value.args[0]::Call

Source: `infra/tests/test_destiny.py:168`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[4].value.args[1].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[5]::Expr

Source: `infra/tests/test_destiny.py:169`; AST `9da0546e33fe497c17574275a2adac62156bf2b6abd5ade4768e47132172544a`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[5].value::Call

Source: `infra/tests/test_destiny.py:169`; AST `ec749de6b79583c76822a104450ad97a76cb462951245f9ee81fd0f301b4d6ff`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[5].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:169`; AST `a7607c86679a31ccf7e4dc6c0fb4250d6e1d3cd47281bdea0664e6029e8212af`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[6]::Assign

Source: `infra/tests/test_destiny.py:170`; AST `659d4c0ee3dd2bd1b761e1b79971d42c57ac9ea7cc33fafed71e683e55b57360`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.stat.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[6].value::Call

Source: `infra/tests/test_destiny.py:170`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[7]::Expr

Source: `infra/tests/test_destiny.py:171`; AST `c1e6cbceb788236124910d0b65f38fec6dfcccb701049d05c033d0d8bc087bf8`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[7].value::Call

Source: `infra/tests/test_destiny.py:171`; AST `630bafe72ece94c2e822400c8313d8a1445be141dda927c87421b0822ff81b90`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[8]::Expr

Source: `infra/tests/test_destiny.py:172`; AST `7374008d47e3d01ef9c0d1744e5cd22c72236cbc802faf937ef8477b9694a1d8`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.utime.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[8].value::Call

Source: `infra/tests/test_destiny.py:172`; AST `c9429e7b71407fe72aefdec2c6623ee8949796a8d62a9200f065ec6edcfefc29`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, os, path. Outputs/bindings: (none).
Calls/effect boundaries: os.utime.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[9]::Expr

Source: `infra/tests/test_destiny.py:173`; AST `8ba7327773734ad045b921ac02646132f3d4cac0e986c4203083ee070e9d3c6d`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[9].value::Call

Source: `infra/tests/test_destiny.py:173`; AST `70ea3bac9f12005bdb4bb089d318a5eae9b46a635484c3f81957116cd6c6bfe5`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[9].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:173`; AST `a7607c86679a31ccf7e4dc6c0fb4250d6e1d3cd47281bdea0664e6029e8212af`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[9].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[10]::Expr

Source: `infra/tests/test_destiny.py:174`; AST `ba74a240599c1525055d03e2847be0abbb31ade5c2a2f79bfb779647a13fa869`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[10].value::Call

Source: `infra/tests/test_destiny.py:174`; AST `02eb8da1a60ac9012664ce8a57542effe034a5ba96c761db4c0145aa930dc265`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_context_is_bounded_and_freshness_does_not_depend_on_mtime::root.body[14].body[12].body[10].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:174`; AST `0e80f1a16db6f8a8cca4889d7250cc2340854eef11377207f47f4dbce8ba59f1`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].body[10].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13]::FunctionDef

Source: `infra/tests/test_destiny.py:176`; AST `b5602add6075118ea3befaa362e525f96679c4ac6b0aa3e4ab4e4e9e851e5b72`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: result, self. Outputs/bindings: result.
Calls/effect boundaries: self.assertEqual, self.call, self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[0]::Expr

Source: `infra/tests/test_destiny.py:177`; AST `6a664084d479b8aafa0fa770aa81ce459dec3ffc08bf0b5b31a92470c14e6b06`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[0].value::Call

Source: `infra/tests/test_destiny.py:177`; AST `d6110e9f80e6c1b2ba25d59497246d055a0bbd3ed3872c1807858813196c7aea`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[1]::Assign

Source: `infra/tests/test_destiny.py:178`; AST `54909a09b18a882e450895fa002a9663675ccf0b92a9e13a17326f287c6d3832`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[1].value::Call

Source: `infra/tests/test_destiny.py:178`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[2]::Expr

Source: `infra/tests/test_destiny.py:179`; AST `6e3021b2b43df95bbd396e9605191332bd353f96b5fc99f93c20c0ad10426fab`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_source_mutation_during_check_cannot_be_reused::root.body[14].body[13].body[2].value::Call

Source: `infra/tests/test_destiny.py:179`; AST `5cace417bb73c1e0491fe46d9d97eee518ce45731b488a04029da5b456bb5219`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_check_and_unreasoned_rerun_rejected::root.body[14].body[14]::FunctionDef

Source: `infra/tests/test_destiny.py:181`; AST `57f9fd9c17d5dbfe887a886145e4b51ce6f74477d66e6830364bd75a447d652a`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_check_and_unreasoned_rerun_rejected::root.body[14].body[14].body[0]::Expr

Source: `infra/tests/test_destiny.py:182`; AST `ed6274721183e60ac1a7bfcde63c6f5e265b874069ffead2ea92f7e40a4c9571`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_check_and_unreasoned_rerun_rejected::root.body[14].body[14].body[0].value::Call

Source: `infra/tests/test_destiny.py:182`; AST `ea78432748caf9058a0bde836f1e3e515d9073d047d0c8b259cabf7bf74d18f3`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_check_and_unreasoned_rerun_rejected::root.body[14].body[14].body[1]::Expr

Source: `infra/tests/test_destiny.py:183`; AST `b2c3893df3fba4438fff142edf0012e0d5fb8590f2d99f61f88b24a0c6e2731f`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_unknown_check_and_unreasoned_rerun_rejected::root.body[14].body[14].body[1].value::Call

Source: `infra/tests/test_destiny.py:183`; AST `88dca55ed22ba332187dcfba01986eb0d63372acf89a1aa624bc31e45a77ec8c`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15]::FunctionDef

Source: `infra/tests/test_destiny.py:185`; AST `8772ae53a1f892c100e1e2fba7ec981c2e2e804825d218acdd5ac08c7913342f`.

Rust module: `infra::tests::test_destiny`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[0]::Expr

Source: `infra/tests/test_destiny.py:186`; AST `663d789583d408ac8699abb973dec59c2f21e61e48b5e1b520ef1c98f28a7762`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[0].value::Call

Source: `infra/tests/test_destiny.py:186`; AST `48253b14e2da43f08973d1a5feda27523b5c2f8080482f300e1201fa987a421d`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[0].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:186`; AST `b98cc6692ad3439c976f63364cf64eec5e8d802f2ad9b712fbef55dbb3414d67`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[15].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[1]::Expr

Source: `infra/tests/test_destiny.py:187`; AST `6812617a9a29c482374b49ea1a7219b8c2e55b5418616672d66ef606166e0018`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[1].value::Call

Source: `infra/tests/test_destiny.py:187`; AST `6b8f20ba3a47a6ac86dc3628a3cd8540b6e5a5ee9b37ac8b3e6613be2bd31365`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::TestDestiny::test_budget_and_native_prerequisite_are_not_pass::root.body[14].body[15].body[1].value.args[0].value::Call

Source: `infra/tests/test_destiny.py:187`; AST `5f94903ef2df36169e4016822aec56b95637f4818f7ba5726624b8d00c996140`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].body[15].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[15]::If

Source: `infra/tests/test_destiny.py:190`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_destiny`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[15]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[15].body[0]::Expr

Source: `infra/tests/test_destiny.py:191`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_destiny`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny.py::module::root.body[15].body[0].value::Call

Source: `infra/tests/test_destiny.py:191`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_destiny`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.catalog, agentinfra.destiny, hashlib, json, os, pathlib, subprocess, sys, tempfile, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; sha2
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
