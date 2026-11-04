# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 222. Inventory digest: `b642baecfaf050ec4ee70cdd063267562be50db60138bb01cde94c788b78c98b`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_retained_native.py::module::root::Module

Source: `infra/tests/test_roadmap_retained_native.py:1`; AST `ac23b8d7fa1407faadb47c9321ad19cd754244e0bff6cefb07756c096cf0952d`.

Rust module: `infra::tests::test_roadmap_retained_native`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, POLICY_PATH, Path, ROOT, __file__, _reader_executable, before, compiled, dict, digest, file_binding, first, first_tool, json, k, materialize, name, observe_native_owner, os, owner, patch, path, prior, reader, recompute, record, result, route, second, self, sha, shared, shutil, socket, str, tempfile, temporary, unittest, v. Outputs/bindings: ROOT, before, compiled, first, first_tool, k, name, owner, path, prior, reader, record, result, route, second, shared, temporary, v.
Calls/effect boundaries: (self.root / '.aegis').mkdir, (self.root / '.aegis/project.json').read_bytes, (self.root / '.aegis/project.json').read_text, (self.root / '.aegis/project.json').unlink, (self.root / '.aegis/project.json').write_text, (self.root / 'framework.toml').write_text, (self.root / 'protocol.json').read_bytes, (self.root / 'protocol.json').write_text, (self.root / 'retained-protocol.json').write_bytes, Path, Path(__file__).resolve, _reader_executable, dict, digest, file_binding, first['argv'][-1].startswith, json.dumps, json.loads, materialize, observe_native_owner, os.getpid, patch, patch.dict, path.read_text, path.write_text, reader.assert_not_called, second['argv'][-1].startswith, self.addCleanup, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.installed_path.parent.mkdir, self.installed_path.read_bytes, self.installed_path.write_bytes, self.manifest.items, self.retained, self.save_manifest, self.schema.write_text, shared.mkdir, shutil.copyfile, socket.gethostname, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:1`; AST `00dbb68ea973fc7b25282e63cf8f657a6ab1d85e90af0ad2f2abd8108635bf47`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_retained_native.py:4`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_retained_native.py:5`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_retained_native.py:7`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_retained_native.py:8`; AST `9df267ed6eef4f61eaaffaebdf9ac9fe93bcf6d1aab9647b1fd045430624c91e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_retained_native.py:9`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[8]::Import

Source: `infra/tests/test_roadmap_retained_native.py:10`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:11`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:13`; AST `5aa56cdf6a003fb50619a2b4256ff75cbb2e8d9603c51855a602a91958944fb2`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:14`; AST `7903500660d6419532fb05d53920d5290554e3194c5894134211635fe8ad7cbf`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:15`; AST `a6292a2050119772b35445e26eac2ee96e486d36a5c1f256821e2e60823bd95f`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_roadmap_retained_native.py:16`; AST `9522470acdd9432bb8a66c5f3ab64ab27f43c5e9d9cfed23e8413315fafcd375`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[14]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:19`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[14].value.value.value::Call

Source: `infra/tests/test_roadmap_retained_native.py:19`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::root.body[14].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_retained_native.py:19`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::root.body[15]::ClassDef

Source: `infra/tests/test_roadmap_retained_native.py:22`; AST `e0b0e56a251719d4143fa0499f511a30bc30b7e27b4d15401797a69bb8b01561`.

Rust module: `infra::tests::test_roadmap_retained_native`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, POLICY_PATH, Path, ROOT, _reader_executable, before, compiled, dict, digest, file_binding, first, first_tool, json, k, materialize, name, observe_native_owner, os, owner, patch, path, prior, reader, recompute, record, result, route, second, self, sha, shared, shutil, socket, str, tempfile, temporary, unittest, v. Outputs/bindings: before, compiled, first, first_tool, k, name, owner, path, prior, reader, record, result, route, second, shared, temporary, v.
Calls/effect boundaries: (self.root / '.aegis').mkdir, (self.root / '.aegis/project.json').read_bytes, (self.root / '.aegis/project.json').read_text, (self.root / '.aegis/project.json').unlink, (self.root / '.aegis/project.json').write_text, (self.root / 'framework.toml').write_text, (self.root / 'protocol.json').read_bytes, (self.root / 'protocol.json').write_text, (self.root / 'retained-protocol.json').write_bytes, Path, _reader_executable, dict, digest, file_binding, first['argv'][-1].startswith, json.dumps, json.loads, materialize, observe_native_owner, os.getpid, patch, patch.dict, path.read_text, path.write_text, reader.assert_not_called, second['argv'][-1].startswith, self.addCleanup, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.installed_path.parent.mkdir, self.installed_path.read_bytes, self.installed_path.write_bytes, self.manifest.items, self.retained, self.save_manifest, self.schema.write_text, shared.mkdir, shutil.copyfile, socket.gethostname, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:23`; AST `d17630cdc765daf8785c6663b71bcf348ae2a19b9cc33f38c7ce1888f7ac76cb`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, digest, file_binding, name, self, shared, shutil, str, tempfile, temporary. Outputs/bindings: name, shared, temporary.
Calls/effect boundaries: Path, digest, file_binding, self.addCleanup, self.installed_path.parent.mkdir, self.installed_path.read_bytes, self.installed_path.write_bytes, self.save_manifest, self.schema.write_text, shared.mkdir, shutil.copyfile, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:24`; AST `a2d347c7d87a6dffb982ace4e927a2aef489346acc659c30cc9cd282b9136072`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: tempfile. Outputs/bindings: temporary.
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:24`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:25`; AST `fc8cb5f798102a85161d3dd39e90e7aade08d9309b19a85559f8601bfd6784aa`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, temporary. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:25`; AST `0528b755a77a14ffa0ae9cda8be534caaceecdb0c16066696c8d88463d197ee2`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, temporary. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:26`; AST `bca8a0504dd30148aa3f5c1218761994003973fe589e94a02dc0d6241a73f946`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self, temporary. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:26`; AST `e2847547a5d529fd43b5a4ae5fbc4154d68731781f79eaace52ab2553840633c`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, temporary. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:27`; AST `64a433e7d51b0c2105679a685168fb55724f404a1027a03a7b7c8dcbfe90317e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: shared.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:28`; AST `d20d143f38d9b5d82545abe3ef1d2ca636f603d0a2b93ac41056e250c71735d1`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:28`; AST `99bcba72db0838f639a464854466bfa2acd0fe9e260d2d59c8e8247715d94a84`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[5]::For

Source: `infra/tests/test_roadmap_retained_native.py:29`; AST `daa5ee34868098cf470b6dbc8dfcbc6da7171324fbe510773775e59b3c3ba1ba`.

Rust module: `infra::tests::test_roadmap_retained_native`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, name, shared, shutil. Outputs/bindings: name.
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[15].body[0].body[5]; no call, error or mutation may be omitted. Iteration: name in ('registry.json', 'records.schema.json')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:30`; AST `db7d7a871703fd92e816bbfd9ff370a38e278f3f25d86eaf0c06e96abeb4120f`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, name, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:30`; AST `fed25c609f0527a549ec132ad9975f1bed9ae48319462f7ae165e4cbea1ac3e0`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, name, shared, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:31`; AST `da28adb039ddd1a23155b1f1271fd0e650aeb23f9950c2f504e0d8d2bf9147a6`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:32`; AST `129cc42ba7b1d7d137ae14c58df383c4198608b6714b9bffa45ca2d18467ead8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.installed_path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:32`; AST `e6d6730749f0d363b2fac551ca573a2991af49e227647984f0709e20fa104870`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.installed_path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:33`; AST `ac3b68b7ce9717fc13e5fadc94c714e2c58fe7349fc95f9e05f53eee1960c25c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.installed_path.write_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:33`; AST `4a316010ac400b13e32fa4def0d612d62fe8e478873845a833ff2001d1d30c84`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.installed_path.write_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[9]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:34`; AST `326469b38c00b2c7f6bcf8396f58b185a525a718a248ddccf5798a921c1b8731`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.installed_path.read_bytes, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[9].value.values[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:34`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[9].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[9].value.values[1]::Call

Source: `infra/tests/test_roadmap_retained_native.py:34`; AST `9216e490ccb7e8348a7ca5b759b640237193502c43b1afcd41bfeac5cd390d20`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.installed_path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[9].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[9].value.values[1].args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:34`; AST `154f59405766f44d31a69455f1e7d928f95594f86a69e82ef8d3bdfcc5817d7e`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.installed_path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[9].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[10]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:35`; AST `622a4b211472c84285e7278cd4b18cb1592fa113b7cf8dfffa50c95d7237fddd`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:35`; AST `43c39924ed99efdc764808e82b18f717a96aecfba261f73adb2e1c4cf765a34e`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[11]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:36`; AST `f3580dbbee138274ebbc86a7dfe7d986cdffe74c618448e2cceaeb5684b2230f`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[12]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:37`; AST `7efaca63d0d6d21b32ea9d3532a370c9fe924535b958a984ae7f27a420e19dbd`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[12].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:37`; AST `23560503d985b072c75f40d4bec790a83fce9e01dc0ac992c0a9ad9171244a97`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[13]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:38`; AST `0646972adbb67d87f3f4f821fbd83391dc1a4df8c381f43ca059543f06882a9e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, self, str. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[13].value.values[2].values[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:39`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[13].value.values[2].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[13].value.values[3].elts[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:40`; AST `e8659631a3bf40d8133cce91488c386095b7660d7c4409042b48179f7eedd0a9`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[13].value.values[3].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[14]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:41`; AST `4eb16cb94e8d73894d9f32c84b613b50295fa9813b91dd83e35cbb26d2dbc656`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::setUp::root.body[15].body[0].body[14].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:41`; AST `0c498040b2e5d706ffaea19e5f9fdc0483331b73842082adfefdeee600c70592`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:43`; AST `2fc5acccb658625a8b309bdf8fa38c664dc5212db775dd47b5497d78cc3e0b25`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: digest, file_binding, json, k, recompute, record, self, v. Outputs/bindings: k, record, v.
Calls/effect boundaries: (self.root / '.aegis').mkdir, (self.root / '.aegis/project.json').write_text, (self.root / 'protocol.json').write_text, digest, file_binding, json.dumps, self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[0]::If

Source: `infra/tests/test_roadmap_retained_native.py:44`; AST `8958ff03b0ea327e7cf836f9b5239d4e7966dd3e60061aab88876ea2c82a8d82`.

Rust module: `infra::tests::test_roadmap_retained_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: digest, k, recompute, self, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted. Condition: recompute
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:45`; AST `f88699765bf5a792aa62aa5044ec617b2acdbd174e41366a3e511e8f3efa3370`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, k, self, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:45`; AST `6f9210a06bf8bd14a2f044cedddd14c8e43533e0a7a1217aee02e8951bf26d3e`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, self, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[0].body[0].value.args[0]::DictComp

Source: `infra/tests/test_roadmap_retained_native.py:45`; AST `d6fea8f3df35a64d27a37be4736738d9a5d7b49227280434e483e6fd89150fc3`.

Rust module: `infra::tests::test_roadmap_retained_native`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, self, v. Outputs/bindings: k, v.
Calls/effect boundaries: self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[15].body[1].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[0].body[0].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_retained_native.py:45`; AST `f1d9e71725e44527a0bc07b6830686bbd18fcabd43517abd0b13eb191c2bfcfb`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.manifest.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].body[0].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[1]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:46`; AST `6f08d7c9f07b282f8b1cabaa4ce2a22b11f942bf3e09bb16b05d2b185a92596f`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'protocol.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:46`; AST `9a75613c6fd8c97ed1ff8615dc8721a1d2c7a31d96cbaf99e6af2d59e46be096`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'protocol.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:46`; AST `19349a888149acd5e27cc083a01890322a698572b5ba39666a2af6d82ee52a3e`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[2]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:47`; AST `5cf342b3eb288622b97daf9c2dfcbfc8af2f2f90739420b659a4729c867eb802`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, self. Outputs/bindings: record.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[2].value.values[2]::Call

Source: `infra/tests/test_roadmap_retained_native.py:47`; AST `524c607452ea5fa78c104e7a3a91e8df337b4a9dc9f23ab843ee12c8394c6f9d`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[2].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:48`; AST `eefdb945759c53b81ba4afc382b1809c4a0951862791479e9726e04e7df2fde1`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:48`; AST `dbe6a4987592f9b63ee200095a0fd65e9df815b0b884c9d5c4482d53190a3a2d`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis').mkdir.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[4]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:49`; AST `00c2818be52a260551e7ed26aee6efdddc838333f7309bcb12f931b09193cd42`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[4].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:49`; AST `4f84076c42a37300d8f0b2e0339bc9b8b94ef5891e36c1d498065c44c89873b8`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::save_manifest::root.body[15].body[1].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:49`; AST `9801d8cd7a9ebda309ba7a97d184dcd2522e700d6096278c995c006e6719c1ad`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::retained::root.body[15].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:51`; AST `78756c49bbd0491d9aa91af703b858a4713c7f864f71aaf8de9554e14a980e09`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _reader_executable, path, self, sha, str. Outputs/bindings: (none).
Calls/effect boundaries: _reader_executable, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::retained::root.body[15].body[2].body[0]::Return

Source: `infra/tests/test_roadmap_retained_native.py:52`; AST `a777f1da5749d83a7fd5041ac5bc688bb2d5c1187f6078e5aa8daecd56961858`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _reader_executable, path, self, sha, str. Outputs/bindings: (none).
Calls/effect boundaries: _reader_executable, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::retained::root.body[15].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:52`; AST `42b06349af49bf04c07b91c31c44c4a636909c834e88f1cf463b12d0c8a127bb`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _reader_executable, path, self, sha, str. Outputs/bindings: (none).
Calls/effect boundaries: _reader_executable, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::retained::root.body[15].body[2].body[0].value.args[2].values[1].left::Call

Source: `infra/tests/test_roadmap_retained_native.py:52`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value.args[2].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:55`; AST `037fb83cfdbfa7505174bd3441e131cd8e609bf4988aac5390df8f24ea149a54`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _reader_executable, result, self, str. Outputs/bindings: result.
Calls/effect boundaries: (self.root / '.aegis/project.json').unlink, _reader_executable, self.assertEqual, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:56`; AST `af9c3fa02da4e5ff87d25820c40c6cc7a5d08568cf1d1e691d118a10c0ff4833`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').unlink.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:56`; AST `3b915d2b340eec9614bd637866ea7037b78225718448d4d3dee009d9ab2a05aa`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').unlink.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[1]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:57`; AST `489521bfd6769c5b3e9e5d693c54c8359860a6260750087214fe4c20dbeae987`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _reader_executable, self, str. Outputs/bindings: result.
Calls/effect boundaries: _reader_executable, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:57`; AST `68b3342c8c5b63157500fd8d5f6a9e12f2d6a29a75c2959ea4d57d520b2ad214`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _reader_executable, self, str. Outputs/bindings: (none).
Calls/effect boundaries: _reader_executable, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[1].value.args[2]::Call

Source: `infra/tests/test_roadmap_retained_native.py:57`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:59`; AST `e5163bbe33de1206cc740e2945778210d8b1aa58b9cb48598686d2cbeac01561`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:59`; AST `f4ab2282aefcbb385029b1f32169ed812cfd3cb3426114b22e7c579087c335b6`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[2].value.args[1]::Call

Source: `infra/tests/test_roadmap_retained_native.py:59`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:60`; AST `ed1149dddb8163fcdaca8d882bb191d2f1402cd332c87bb528e6b94e0b0e05bb`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_installed_active_bytes_need_no_historical_protocol_fallback::root.body[15].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:60`; AST `ec828813671c56856971862ac9f0a01dd186df846f685f6720099350725c3719`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:62`; AST `a00a13f93f2bff1fec71b49078dacb6e59518cac439206e258ffd845aaa6ff9c`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, result, self. Outputs/bindings: before, result.
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes, self.assertEqual, self.assertNotEqual, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:63`; AST `218740fba67dfa5d5b0da397ad001d66c578d5b54a3888d3836f2fc36cc290b7`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:63`; AST `f92840261bf8231a877295315998a83cbef80f22eefe106a053154db978382d8`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:64`; AST `d57f766fc8752d89a46f39beba7e72080cf608036ceeacd5edd9677f5929154e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:64`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:65`; AST `099d5c1c39c939c28fd20ac3bbf8cecad6e81a14ce56a31a7d611e30a8d99733`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:65`; AST `3cb4c29b5f7d3b51450777d5f86da33873a5de555340789283ee064d14973c17`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:66`; AST `4302771ef59ad8ea3f38b65d5dad1340b50d9f1d8825a10868ca1cc5f11183b8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:66`; AST `fd5b828782ce1022fb36d276efc896ed16d7ee2b61d6668b259088f8ec71812d`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:67`; AST `d8270f8e28c4d73d07e3245c70bb92d58a7b06624df9583cfac82721fb5248f1`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:67`; AST `8f1acf1ef14df5c65b824c39406b120a5e276d2095099c150940ca2073bc8a58`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:68`; AST `6e60acc77f7e67d46fceb2238e7f92d9efb555b51f65888f615be21409e124b5`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:68`; AST `44b9553e5eb6f2308d5ab8359edbb0de819cd335714bdd17cf970f2077dce593`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:69`; AST `9619b556f82aba299c01770ba613e19c5380cad79aa1e89c9cac289f4748b1cb`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:69`; AST `7727a53e3b10b11b3f9464290d92c2ba88a2fb0aad0f6e6faeece4d1c76c7d4f`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_retained_route_uses_exact_prior_pin_without_changing_project_or_goal::root.body[15].body[4].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:69`; AST `f92840261bf8231a877295315998a83cbef80f22eefe106a053154db978382d8`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:71`; AST `5bf7278d13f41fdfa0c36831692cd8c05303a02da69141e073b46ae75b630524`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, digest, json, record, self, str. Outputs/bindings: record.
Calls/effect boundaries: (self.root / '.aegis/project.json').read_text, (self.root / '.aegis/project.json').write_text, digest, json.dumps, json.loads, self.assertRaisesRegex, self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[0]::With

Source: `infra/tests/test_roadmap_retained_native.py:72`; AST `dd1361412bc5222965db6b37a3ef3fa477675a0f13730ebec6a6b6270230c08e`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.assertRaisesRegex, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:72`; AST `df62919312098031c7a8708c2732c7c83a759e303bbf9d5ec8d2e864ecb6a962`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:73`; AST `39a12144a590cb95dc2b712794db83c4ad9274707d871f85288e73857ff79a59`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:73`; AST `6f29b89ed18746bbce8ec47f3ee404657715dcfa378b146dc9d3ea690d53b1ae`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[0].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:73`; AST `5ac2bc27988bf2c9e1db87bfa32bafe6132d42b875a08e97adbd5a244c5c37e5`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[1]::With

Source: `infra/tests/test_roadmap_retained_native.py:74`; AST `821db1449ae0c7e99d9c419ee4e898eff970de6125956b0673701ad5e0ee675e`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:74`; AST `4cff40e47f51a7919dcbe24cd8b61425c59ea5441e5ec0c1651ca35639c84d65`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:75`; AST `b383b16fe50a32c50cc55fa2ae641fc024c00dc31c4dff1929568e446f2db3c8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:75`; AST `7459b8459fccf9144a1482aa98ea574d8560a3aa40ed38f56a9c14c769b6a4df`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[1].body[0].value.keywords[0].value.left::Call

Source: `infra/tests/test_roadmap_retained_native.py:75`; AST `f680f04f30ce6133d57938389d35e0cc58b43cf966a9bec2813a22a81b9cebfb`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[1].body[0].value.keywords[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[2]::With

Source: `infra/tests/test_roadmap_retained_native.py:76`; AST `3240b5a674df676f184665976a952f1bb09f65797d12a133cdddcb593b4aefd9`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:76`; AST `c646bbbf40db98447bc71a788ba17343edcc3a62646373c3a0709ef7f744366a`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:77`; AST `a6f00f0b6c75c4360d87afbcff3a2b99f6dedbdb3403f7f0ec64ca5cb6a82493`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:77`; AST `16fd93200ce9568719a7ec30d7047715f6a224f1c18f6de232ce30a1ba5e3fef`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.retained, str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[2].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:77`; AST `32b82a81a9503d1ce17453b74ca02c1a8ef22d8d0464c2e5713aae8a09a14130`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[2].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[3]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:78`; AST `a2974624d34ba7a03712f99ab63af785fd6c30e01894480ad3b7ef534e4bf1a8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: record.
Calls/effect boundaries: (self.root / '.aegis/project.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:78`; AST `94c157abb3fcfb4fb7151a8c8ee081d2c7543f274436a86a83864e5b42f2ed3d`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:78`; AST `ecf04460efe315a7aa9e1213fa98954e5287509be225701fe3a6207895a8fe13`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[4]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:79`; AST `8b30785abbe864382b7a6353e07b41e29a318e2a50c55ef946102c2136b586b1`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[5]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:80`; AST `00c2818be52a260551e7ed26aee6efdddc838333f7309bcb12f931b09193cd42`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[5].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:80`; AST `4f84076c42a37300d8f0b2e0339bc9b8b94ef5891e36c1d498065c44c89873b8`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/project.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:80`; AST `9801d8cd7a9ebda309ba7a97d184dcd2522e700d6096278c995c006e6719c1ad`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[6]::With

Source: `infra/tests/test_roadmap_retained_native.py:81`; AST `3ed05f2ade2d0e2314bae406d5f6c8a18ba1e464d20c1980b49a45356f19af86`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:81`; AST `e89d768cdd7225ecced752529c7e5c431f45d5e021e689761a3bed95f27452f9`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:82`; AST `cd234bf9ac1238b0899ff1199a2b517bc8e96bdac6188bb94b0d533a4e05bf1c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[5].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_unpinned_bytes_unrelated_paths_and_nondeleted_mismatch_are_rejected::root.body[15].body[5].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:82`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:84`; AST `c9be877f0fc8df2f3609a733d9aeaabe884f59ca8f45d026c7d1d240a72f9e96`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained, self.save_manifest, self.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:85`; AST `07ce40dcf2694bec0179d651280d997d087143907448917a562b38796102b5eb`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:86`; AST `00888515a5d3e4f5968ac18092d7db3efb0cfc16ae72066d64bdb4c94114abcf`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:86`; AST `eefa0c0fd85b3038e0e0425dcdba9377b531f4ffc19d94091ae5e7027f1cd1f0`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[2]::With

Source: `infra/tests/test_roadmap_retained_native.py:87`; AST `c29e42b3c49effb863cf31e8e8efe96a61e663863210b9b3af56f1270e743926`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:87`; AST `df62919312098031c7a8708c2732c7c83a759e303bbf9d5ec8d2e864ecb6a962`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:88`; AST `cd234bf9ac1238b0899ff1199a2b517bc8e96bdac6188bb94b0d533a4e05bf1c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:88`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:89`; AST `4eb16cb94e8d73894d9f32c84b613b50295fa9813b91dd83e35cbb26d2dbc656`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:89`; AST `0c498040b2e5d706ffaea19e5f9fdc0483331b73842082adfefdeee600c70592`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:90`; AST `59e80d6f8e8e0a42bac097ae1b3af3478fab59985f827b6a49d8023e29001385`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:90`; AST `b987db341edb85f0703ea957343e50111c71fce507d401ca456055df65fa37b6`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[5]::With

Source: `infra/tests/test_roadmap_retained_native.py:91`; AST `c29e42b3c49effb863cf31e8e8efe96a61e663863210b9b3af56f1270e743926`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:91`; AST `df62919312098031c7a8708c2732c7c83a759e303bbf9d5ec8d2e864ecb6a962`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:92`; AST `cd234bf9ac1238b0899ff1199a2b517bc8e96bdac6188bb94b0d533a4e05bf1c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[6].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_rebound_but_tampered_manifest_digest_or_schema_bytes_are_rejected::root.body[15].body[6].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:92`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:94`; AST `18fddc4a079fe8329948086237e8c124b53cbe67d7d01e2ddd9035f63ac1de85`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained, self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:95`; AST `049cf958e54bc09d4ad6da3518e051e4085cab78b7226c324f8806c2bc790113`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:96`; AST `4eb16cb94e8d73894d9f32c84b613b50295fa9813b91dd83e35cbb26d2dbc656`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:96`; AST `0c498040b2e5d706ffaea19e5f9fdc0483331b73842082adfefdeee600c70592`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[2]::With

Source: `infra/tests/test_roadmap_retained_native.py:97`; AST `c29e42b3c49effb863cf31e8e8efe96a61e663863210b9b3af56f1270e743926`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:97`; AST `df62919312098031c7a8708c2732c7c83a759e303bbf9d5ec8d2e864ecb6a962`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:98`; AST `cd234bf9ac1238b0899ff1199a2b517bc8e96bdac6188bb94b0d533a4e05bf1c`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_other_protocol_kind_cannot_supply_native_executable_authority::root.body[15].body[7].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:98`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:100`; AST `2e799a760abd59921d0320f37ee256f81e9ba196a634067c7e1f85c09810cb9e`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: file_binding, json, path, prior, record, result, self. Outputs/bindings: path, prior, record, result.
Calls/effect boundaries: (self.root / 'protocol.json').read_bytes, (self.root / 'retained-protocol.json').write_bytes, file_binding, json.dumps, json.loads, path.read_text, path.write_text, self.assertEqual, self.retained, self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:101`; AST `0861d577cd1dd8d99d7cc779d54a7892deec511362aaab318942964ccea422b7`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'protocol.json').read_bytes, (self.root / 'retained-protocol.json').write_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:101`; AST `f4d47c459647a109c70c8410ba5844fae49bf3ba8cc749b4bdb5257073d8bc6f`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'protocol.json').read_bytes, (self.root / 'retained-protocol.json').write_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:101`; AST `8c0b1a163122cc718dd62b6b02aa53e988e866d79ba108c224bd27a481414221`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'protocol.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[1]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:102`; AST `51c801c7afa45ff0a2fdafbf5db9a074e5cdcb0268fb6b6c7a149a07cce5a4bd`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, self. Outputs/bindings: prior.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:102`; AST `25d2e675325787f58ca2ddfaa86e391df7c540ebe1bfef4a1b9889196d57fee1`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[2]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:103`; AST `c9f27c05cf3ac99cd13f408fdebcdc2ff5a45aff460a73f69c460fb6ee571ada`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:104`; AST `4eb16cb94e8d73894d9f32c84b613b50295fa9813b91dd83e35cbb26d2dbc656`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:104`; AST `0c498040b2e5d706ffaea19e5f9fdc0483331b73842082adfefdeee600c70592`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.save_manifest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[4]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:105`; AST `21b2a0755d4d416aa5f58d075d8fb3eed7b04c9edfe92ef106097bf655d22490`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[5]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:106`; AST `3f2ecf20c369a70da1c2b2c090ea27892ab858e247930f9afe296b219f719a51`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: record.
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[5].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:106`; AST `4a076f3fdf20f1dd94162a22f2b9944a159c045ed6266d1cb7ac9b597c2ea970`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:106`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[6]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:107`; AST `c50e5ca8aeda29170654ef7a94bb4ec7197870635c9e017a56575124a64cd0e3`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior, record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[7]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:108`; AST `2dcd96a6f749d79ac226af0dfa1e2f0a5a59e3a2596bdc7ec6a3912065ba011d`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[7].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:108`; AST `fb1057813419dca2782b9d0ddc1d8ee2908847fd7edf1019e8d4a09d9e819ce4`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[7].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:108`; AST `9801d8cd7a9ebda309ba7a97d184dcd2522e700d6096278c995c006e6719c1ad`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[8]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:109`; AST `d57f766fc8752d89a46f39beba7e72080cf608036ceeacd5edd9677f5929154e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[8].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:109`; AST `c92bbbe787a7452f590d8b71d659933aa80cd4d9f106a547542537d771a1a794`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[9]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:110`; AST `63709546711c7ec22d506ac9c4588aa2bce9db0d12314d799b2c8e25afdeb79e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: prior, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[9].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:110`; AST `ac204702c2d13cdd8c65bb4414b8c953cab4671d21f6c699a3ada952b8b5ac63`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: prior, result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[10]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:111`; AST `4302771ef59ad8ea3f38b65d5dad1340b50d9f1d8825a10868ca1cc5f11183b8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[8].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_later_installed_protocol_pin_keeps_the_running_prior_pin_available::root.body[15].body[8].body[10].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:111`; AST `fd5b828782ce1022fb36d276efc896ed16d7ee2b61d6668b259088f8ec71812d`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[8].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:113`; AST `2b76f5d8ab33e91104a42e734b1ac09bc67cfb71a6f112720d9c1f131ef6f806`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: POLICY_PATH, ROOT, compiled, dict, first, first_tool, json, materialize, os, patch, path, record, second, self, shutil. Outputs/bindings: compiled, first, first_tool, path, record, second.
Calls/effect boundaries: (self.root / 'framework.toml').write_text, dict, first['argv'][-1].startswith, json.dumps, json.loads, materialize, patch, patch.dict, path.read_text, path.write_text, second['argv'][-1].startswith, self.assertNotEqual, self.assertTrue, shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:114`; AST `e181c2a386a091ee3af398825fc50db65c9ab6ecc05d92fa3853729f3556f121`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, ROOT, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:114`; AST `bfba2b5b2ece2113806f571d1abde52516afa040d01d792333dade0e15decad1`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, ROOT, self, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[1]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:115`; AST `686154b8806a4385cb6d6df16505ef6f65e2459c5599c939583dcc8d698cc3fa`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'framework.toml').write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:115`; AST `3866f1ad7b9640f23dde616c58248d519cd4afe1818cf40452792bf18abf5f26`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'framework.toml').write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[2]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:116`; AST `21b2a0755d4d416aa5f58d075d8fb3eed7b04c9edfe92ef106097bf655d22490`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[3]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:117`; AST `3f2ecf20c369a70da1c2b2c090ea27892ab858e247930f9afe296b219f719a51`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: record.
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:117`; AST `4a076f3fdf20f1dd94162a22f2b9944a159c045ed6266d1cb7ac9b597c2ea970`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:117`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[4]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:118`; AST `eb7fe6a5c5bb4b612c46e9005ab7f68e7ed80d09bb87d6610164699ec0d67120`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[5]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:119`; AST `2dcd96a6f749d79ac226af0dfa1e2f0a5a59e3a2596bdc7ec6a3912065ba011d`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[5].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:119`; AST `fb1057813419dca2782b9d0ddc1d8ee2908847fd7edf1019e8d4a09d9e819ce4`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:119`; AST `9801d8cd7a9ebda309ba7a97d184dcd2522e700d6096278c995c006e6719c1ad`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, record. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[6]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:120`; AST `9a01a573e91a24214b1d8f537df1878b9060ec56fc3ff7d69ec54e22df4d337e`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH. Outputs/bindings: compiled.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[7]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:124`; AST `cc51d328338a012b21d4eb86d80f09173acbe6addace16575068d5ba4c05350d`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: first_tool.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[7].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:124`; AST `64b3cf3ca36158d662e6060a610b4536f37471f8d950e98ef519339772808a9c`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8]::With

Source: `infra/tests/test_roadmap_retained_native.py:125`; AST `d5a9326e189a1606306b9efb180bed703e6cc424f03ce48dac589316e617ae60`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: compiled, first_tool, materialize, os, patch, self. Outputs/bindings: first, second.
Calls/effect boundaries: materialize, patch, patch.dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[9].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:125`; AST `13a68c711265ee7416727ffc11c97134d0b8336d8fd580a2df21ef159d8f0fe6`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:126`; AST `fe6e5db699f5fe3278d269463c3df610c4ada7d23cd310ae66a5dd17375d92c1`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first_tool, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:127`; AST `591809019edf10340d8c9c22548d42a91a86511aa4dbf2bff53b2466292c1e50`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:128`; AST `ee4543fc7fa03dc30f18f6bb8304c93c3f6d49a65db321657b253ec65cbb6b43`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, self. Outputs/bindings: first.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:128`; AST `806b89bcad28cfa69302eea50837ae7c1b1736e5e8198f249a22583c7d03ca05`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, self. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].body[1]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:129`; AST `5c402db95692117d9b8360b6193ee1973d3d528f658743ab9b22a62aa48d8161`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, self. Outputs/bindings: second.
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[9].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:129`; AST `806b89bcad28cfa69302eea50837ae7c1b1736e5e8198f249a22583c7d03ca05`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, self. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[9]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:130`; AST `4955279159099624d6925a3f0a0575748176834a72bb2c6e61bb8437499f3404`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[9].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:130`; AST `68bae6a33334c2bb6d3d22df92f7dd3bd6324302edcb49db773fd08391b87b9f`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[10]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:131`; AST `dde6ce69b436d60cfe20a32ced4531d736c36d4c0e1e5ead120b419c5f72b9d9`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[10].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:131`; AST `9042f7be15e47cf5c272852d3c16a2745cabd9a18285fce497864f7cd3ab674b`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[11]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:132`; AST `5565ff8bf0165fc607601185ad10ce6e18b49bfb0c1628a7badb217ff18b554a`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first['argv'][-1].startswith, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[11].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:132`; AST `ea07fc122854f9c9a2daedd6c1d522f4b425e72309b9ba59cb7ed0fd16a46217`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, self. Outputs/bindings: (none).
Calls/effect boundaries: first['argv'][-1].startswith, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[11].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:132`; AST `f2976dd351dab7c938a94d5540fd11058eb94c667291c1bbaf13bdd2a64cd90c`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first['argv'][-1].startswith.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[12]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:133`; AST `f7a5a1c15948fc998097d07ad9e675b3e77bf8ed65b4e64d1e849adabd423ff2`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second['argv'][-1].startswith, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[9].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[12].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:133`; AST `0d0f71a9179cc689fddff3045cffa7d320a784783fe5447cb8dc37fb84280599`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second, self. Outputs/bindings: (none).
Calls/effect boundaries: second['argv'][-1].startswith, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_protocol_exports_for_different_binaries_cannot_overwrite_a_retained_schema_pin::root.body[15].body[9].body[12].value.args[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:133`; AST `c925922fbed33af70959f28bb54ba6d63e8d2acd1ed252d59ea717026938c9e0`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: second. Outputs/bindings: (none).
Calls/effect boundaries: second['argv'][-1].startswith.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[9].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10]::FunctionDef

Source: `infra/tests/test_roadmap_retained_native.py:135`; AST `84bfae88624ccdaf4a1b3e11e0defaf19aa0f84bfdb21fd087ecf26e14a556ad`.

Rust module: `infra::tests::test_roadmap_retained_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, observe_native_owner, os, owner, patch, reader, route, self, socket. Outputs/bindings: owner, reader, route.
Calls/effect boundaries: observe_native_owner, os.getpid, patch, reader.assert_not_called, self.assertRaisesRegex, socket.gethostname.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[0]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:136`; AST `9ea230cc66d52ee4e717c871d63a669c40ab69879d46823834bd29fa24c17c7f`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, socket. Outputs/bindings: owner.
Calls/effect boundaries: os.getpid, socket.gethostname.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[0].value.values[0]::Call

Source: `infra/tests/test_roadmap_retained_native.py:136`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[0].value.values[1]::Call

Source: `infra/tests/test_roadmap_retained_native.py:136`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[1]::Assign

Source: `infra/tests/test_roadmap_retained_native.py:137`; AST `90bc73f406d259e27bbfdc1105e0667ffdc602df7aa4f203225de9a2195440c8`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: route.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2]::With

Source: `infra/tests/test_roadmap_retained_native.py:138`; AST `c68342e28714689798dd976c2e6477d0f47058b64a7d605b6e3506fae87e1b6f`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, observe_native_owner, owner, patch, route, self. Outputs/bindings: reader.
Calls/effect boundaries: observe_native_owner, patch, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:138`; AST `7fd08c3f13242a5e0cda3a3c64af984fd1bec5f1785a726b3348d57bf34beca2`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:139`; AST `f917911b046dd3d66e3df7c2e0c75e5572d7bd74edb9a1b37d5b566ad6a34062`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:140`; AST `51a447dfd9befbff324f38517dabd8cf64a10a9a3719e92d1affa4b001aac9b5`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, route. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].items[3].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:141`; AST `020ad3d8e2ce5b1533014905cb5a290dd8b320187af407c8dfcf326c528dc704`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].items[3].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].body[0]::With

Source: `infra/tests/test_roadmap_retained_native.py:142`; AST `72486f1312634b35ee7726054b6c40209ee3c5eb8ee826c5417a864c17c0cc1e`.

Rust module: `infra::tests::test_roadmap_retained_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, observe_native_owner, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_native_owner, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[15].body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retained_native.py:142`; AST `3e6ef890fc266d63d74c9c7b5a3a523dbbab0f096fb35b00ebd49219d821ac73`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:143`; AST `705250aa2ca7a170933876235431706f7274f6dc1fd999bf5cd3b13fd4867512`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observe_native_owner, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:143`; AST `66f4a106e007440d5f48ee3def63ffc0a496c3a08bad279b3e82a4e1e10fbdf1`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observe_native_owner, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: observe_native_owner.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[3]::Expr

Source: `infra/tests/test_roadmap_retained_native.py:144`; AST `4f6e0ef484d8ab1829ddd8752ce7d90bba9862f93a3f1e5fc3b1da03fbd3cda0`.

Rust module: `infra::tests::test_roadmap_retained_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reader. Outputs/bindings: (none).
Calls/effect boundaries: reader.assert_not_called.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retained_native.py::module::RetainedNativeExecutableTests::test_changed_process_creation_identity_stops_before_native_reader_dispatch::root.body[15].body[10].body[3].value::Call

Source: `infra/tests/test_roadmap_retained_native.py:144`; AST `840ba296340961e6e8aa0380c698acb5eee7e8c19241a6ebe07c46821d005ed2`.

Rust module: `infra::tests::test_roadmap_retained_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reader. Outputs/bindings: (none).
Calls/effect boundaries: reader.assert_not_called.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_persistence, agentinfra.roadmap_records, agentinfra.roadmap_work, json, os, pathlib, shutil, socket, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[15].body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
