# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 274. Inventory digest: `b5639f45d801001b883f0a7dbdebe9e55654232aefb5796324234fa3d194f917`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_portability.py::module::root::Module

Source: `infra/tests/test_roadmap_portability.py:1`; AST `e4e4a807b8a920fc7d6c6fcd5dded9851bf3a2560b4f37647c5f0fae51d86a73`.

Rust module: `infra::tests::test_roadmap_portability`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, FileTransaction, OSError, Path, ROOT, __file__, __name__, after, all, args, artifacts, before, canonical, change, check, current, dict, digest, fail, first, i, index, inventory, json, kwargs, len, local, markdown, old, old_document, old_index, owned, p, part, parts, patch, path, publish, range, raw, read_json, record, relative, resolved, result, s, second, self, shard, shards, source, stage, stamp, str, sys, tempfile, transaction, u, units, unittest. Outputs/bindings: ROOT, after, before, change, current, first, i, index, local, old, old_document, old_index, owned, p, part, parts, path, raw, record, relative, resolved, result, s, second, shard, source, stamp, u, units.
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists, (self.base / 'infra__b.py.md').exists, (self.base / 'inventory.json').exists, (self.base / 'inventory.json').write_text, (self.base / 'units/units-0000.json').exists, (self.base / 'user-notes.txt').read_text, (self.base / 'user-notes.txt').write_text, (self.base / (source['path'].replace('/', '__') + '.md')).write_text, (self.base / part['path']).read_bytes, (self.base / relative).read_bytes, (self.root / 'infra').mkdir, (self.root / 'infra/a.py').unlink, (self.root / 'infra/a.py').write_text, (self.root / 'infra/added.py').write_text, (self.root / 'infra/b.py').write_text, (self.root / 'infra/x').mkdir, (self.root / 'infra/x/y.py').write_text, (self.root / 'infra/x__y.py').write_text, FileTransaction, OSError, Path, Path(__file__).resolve, all, artifacts, canonical, check, dict, digest, inventory, json.dumps, len, markdown, old_document.read_bytes, old_document.stat, owned.items, p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, parts.values, patch, path.parent.mkdir, path.read_bytes, path.write_bytes, path.write_text, publish, range, read_json, self.assertEqual, self.assertFalse, self.assertLessEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.base.joinpath, self.base.joinpath('units').mkdir, self.base.joinpath('units/units-0000.json').write_text, self.base.rglob, self.subTest, self.temp.cleanup, shards, source['path'].replace, str, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[0]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[1]::Import

Source: `infra/tests/test_roadmap_portability.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_portability.py:5`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_portability.py:6`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_portability.py:7`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:8`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[7]::Assign

Source: `infra/tests/test_roadmap_portability.py:10`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[7].value.value.value::Call

Source: `infra/tests/test_roadmap_portability.py:10`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[7].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_portability.py:10`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[8]::Expr

Source: `infra/tests/test_roadmap_portability.py:11`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[8].value::Call

Source: `infra/tests/test_roadmap_portability.py:11`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[8].value.args[1]::Call

Source: `infra/tests/test_roadmap_portability.py:11`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:12`; AST `9b2bc15df551d2f572aaf19e186c344ae9275ecddcef9c9d9b609cfeee18f7d4`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:13`; AST `b2ad68ad2792e4099b622a0cc4c5d3668868953b47e72bd18e193cfb7ff85d73`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_portability.py:14`; AST `5ee152238b187a04ee5ce0c1b5c22b6cae0bd9dd43a85035c83abd211f6eb177`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_portability.py:17`; AST `0615b81dd9300f6443042ae4177c027122e612250d07c498fe3b0e032a4d336b`.

Rust module: `infra::tests::test_roadmap_portability`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, FileTransaction, OSError, Path, after, all, args, artifacts, before, canonical, change, check, current, dict, digest, fail, first, i, index, inventory, json, kwargs, len, local, markdown, old, old_document, old_index, owned, p, part, parts, patch, path, publish, range, raw, read_json, record, relative, resolved, result, s, second, self, shard, shards, source, stage, stamp, str, tempfile, transaction, u, units, unittest. Outputs/bindings: after, before, change, current, first, i, index, local, old, old_document, old_index, owned, p, part, parts, path, raw, record, relative, resolved, result, s, second, shard, source, stamp, u, units.
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists, (self.base / 'infra__b.py.md').exists, (self.base / 'inventory.json').exists, (self.base / 'inventory.json').write_text, (self.base / 'units/units-0000.json').exists, (self.base / 'user-notes.txt').read_text, (self.base / 'user-notes.txt').write_text, (self.base / (source['path'].replace('/', '__') + '.md')).write_text, (self.base / part['path']).read_bytes, (self.base / relative).read_bytes, (self.root / 'infra').mkdir, (self.root / 'infra/a.py').unlink, (self.root / 'infra/a.py').write_text, (self.root / 'infra/added.py').write_text, (self.root / 'infra/b.py').write_text, (self.root / 'infra/x').mkdir, (self.root / 'infra/x/y.py').write_text, (self.root / 'infra/x__y.py').write_text, FileTransaction, OSError, Path, all, artifacts, canonical, check, dict, digest, inventory, json.dumps, len, markdown, old_document.read_bytes, old_document.stat, owned.items, p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, parts.values, patch, path.parent.mkdir, path.read_bytes, path.write_bytes, path.write_text, publish, range, read_json, self.assertEqual, self.assertFalse, self.assertLessEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.base.joinpath, self.base.joinpath('units').mkdir, self.base.joinpath('units/units-0000.json').write_text, self.base.rglob, self.subTest, self.temp.cleanup, shards, source['path'].replace, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:18`; AST `4a347ee2f61ff503a82309e0abb338d8680c35136a0925d259fa3dcede70793f`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra').mkdir, (self.root / 'infra/a.py').write_text, (self.root / 'infra/b.py').write_text, Path, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:19`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:19`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_portability.py:19`; AST `3fd62e96028b079a923df6e9a7c1c1df8b3ae2536d55ba9d4f31f162d4d5ddb5`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:19`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_portability.py:20`; AST `847a9b1d304fd6408b3cb72db9e5dacb6c57f665bfe2b4ee406086f5f23b6bf9`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:20`; AST `9371287eb45cde05e3fd243863e84319741d2955c8a705a50d6d82cfca52e189`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_portability.py:21`; AST `af9ef2b69cb05ba189b056ae9e75622f8e31bac7eed6fdb957143e4cce606fa8`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:21`; AST `b8649f047457712857c29d30ca7cb5e3a951734dd941225a845523141626f5bc`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_portability.py:22`; AST `87a1829724d7dea867f317b7bed20d919eb4c4f812b83993e27a29dea5f638c8`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/b.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_portability.py:22`; AST `954d25a5379f335f7dc3bc339a67e18a9e213d00268e95e53c9aeb9ca432d6d4`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/b.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::setUp::root.body[12].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_portability.py:23`; AST `5a5b910fd21c369578890b023aad6b2969a5c87883cf117ff4664e8c4913bd26`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::tearDown::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:25`; AST `13fc628cded8f8def9f296b061b0d1b4f129ada0770d009511b176b914c63004`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::tearDown::root.body[12].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:26`; AST `03b3f025b568ce93e3252b0f1f4a5ce0348dbf2ecebaae9a0913927af51d7b24`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::tearDown::root.body[12].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:26`; AST `467d2c9d775dc88f51613c917ddb5ec5487d5c87293666d9c9c5f9a88375b66b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:28`; AST `5135292d311e79b9fee0ba67154e1590f234600ba3a1a0e650778b58fec35c02`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: all, before, check, first, inventory, old_document, old_index, owned, part, publish, raw, read_json, relative, result, second, self, stamp, u. Outputs/bindings: before, first, old_document, old_index, owned, part, raw, relative, result, second, stamp, u.
Calls/effect boundaries: (self.base / part['path']).read_bytes, (self.base / relative).read_bytes, (self.root / 'infra/a.py').write_text, all, check, inventory, old_document.read_bytes, old_document.stat, owned.items, publish, read_json, self.assertEqual, self.assertLessEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:29`; AST `a6ccf6120950ae2cbda31f27f6cff2d97891372566b8cb15e4d2659439bdfffd`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: first.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:29`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:29`; AST `1f85c3182a21e4fa91e5f058145ab0ce7c32d0d01a77aed48c35f343bbccecc3`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:29`; AST `14c989a5b372cd3509c888d20949105ec6da09de4c25be13ce901ae3edbdfd8f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[2]::Assign

Source: `infra/tests/test_roadmap_portability.py:30`; AST `7fdcfac5c1c56d7c014e60d6d8c1d57c09a155498c1399688c048a3ea82304a6`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: old_index.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:30`; AST `a38edc7ca35b2b10f19d02de30239427671e37b4426ae032a98556968070b670`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[3]::Assign

Source: `infra/tests/test_roadmap_portability.py:31`; AST `28ee62905790fe1afeede157a5826bb874f581a3c31ccf70cc046edb6f779363`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: old_document.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[4]::Assign

Source: `infra/tests/test_roadmap_portability.py:32`; AST `2052109d72db375343c6d7cc22050938e7ad7b56c7ca9f3de60fdacc9d3be5c3`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old_document. Outputs/bindings: before.
Calls/effect boundaries: old_document.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_portability.py:32`; AST `5942678fe88cc0e3184561df09b3fccd0f6b7fc55fec95d73e68af8461feda23`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_document. Outputs/bindings: (none).
Calls/effect boundaries: old_document.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[5]::Assign

Source: `infra/tests/test_roadmap_portability.py:32`; AST `04523ed1516440f8f1beac539b09bcfaa84e58c0d531b27a5daac513ec70d19b`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old_document. Outputs/bindings: stamp.
Calls/effect boundaries: old_document.stat.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[5].value.value::Call

Source: `infra/tests/test_roadmap_portability.py:32`; AST `18874097067ae97b41d9dc41b8ca47bc33fee59a27af9f09eff546d3c2602546`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_document. Outputs/bindings: (none).
Calls/effect boundaries: old_document.stat.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[5].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6]::Assign

Source: `infra/tests/test_roadmap_portability.py:33`; AST `cabe6ee41607c44028410c78febf1778c860785471c16004182ae77fcab17c5f`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, old_index, part, read_json, self, u. Outputs/bindings: owned, part, u.
Calls/effect boundaries: (self.base / part['path']).read_bytes, all, read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6].value::DictComp

Source: `infra/tests/test_roadmap_portability.py:33`; AST `69e1fda7b5e6e75be2240e6e94bacf1dc75f7637cb538893b43954f1745539eb`.

Rust module: `infra::tests::test_roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: all, old_index, part, read_json, self, u. Outputs/bindings: part, u.
Calls/effect boundaries: (self.base / part['path']).read_bytes, all, read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6].value.value::Call

Source: `infra/tests/test_roadmap_portability.py:33`; AST `19713f7d5190d0011741349b337f2d4af3f7e8a1ff188860bf83d188b83e74df`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: part, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / part['path']).read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[6].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6].value.generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_portability.py:34`; AST `7abf40d7c4ca4025040c226248d504e9431e4f89a3037dadb23a9b7144d3c741`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, part, read_json, self, u. Outputs/bindings: u.
Calls/effect boundaries: all, read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[6].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6].value.generators[0].ifs[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_portability.py:34`; AST `3a8557519ca097df5878165c1e432dbb4ad46e8001bc8d79ae676d0de0d7a40a`.

Rust module: `infra::tests::test_roadmap_portability`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: part, read_json, self, u. Outputs/bindings: u.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[2].body[6].value.generators[0].ifs[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[6].value.generators[0].ifs[0].args[0].generators[0].iter.value::Call

Source: `infra/tests/test_roadmap_portability.py:34`; AST `c82a3c26110ba30588c7e7783121f36b42fe08a901c505e0b7742a5136079315`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: part, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[6].value.generators[0].ifs[0].args[0].generators[0].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[7]::Expr

Source: `infra/tests/test_roadmap_portability.py:35`; AST `e7828c923fdb5378a15ecd45fd22709d17909d3b2666225b838d722b59b04d97`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[7].value::Call

Source: `infra/tests/test_roadmap_portability.py:35`; AST `1a8005610d0616cd5be982e5248002d9aeb2a9b54b50d282edb90f5cf1dbb103`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[8]::Assign

Source: `infra/tests/test_roadmap_portability.py:36`; AST `9ff9b32aef4007db666bc4a0032768baf7aaef369d3f40595a2815c50e3ab32c`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: second.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[8].value::Call

Source: `infra/tests/test_roadmap_portability.py:36`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[9]::Assign

Source: `infra/tests/test_roadmap_portability.py:36`; AST `deba095d64a2b86c413ae470e8054f223ee7a36ed6c92501cc1732139fd51b5e`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, second, self. Outputs/bindings: result.
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[9].value::Call

Source: `infra/tests/test_roadmap_portability.py:36`; AST `e407467ff9779b246c928b9e57b5ce6961e8595eafb8ca5cf6e191861cb76255`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, second, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[10]::Expr

Source: `infra/tests/test_roadmap_portability.py:37`; AST `7167b50930fdec4b06292294332ca4e3b857cac398f552a17580dc18d8c0356a`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, old_document, self. Outputs/bindings: (none).
Calls/effect boundaries: old_document.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[10].value::Call

Source: `infra/tests/test_roadmap_portability.py:37`; AST `a5d6a191baa7866f2267c336d11ce3c81143956fe22be190854dcf9ac627523b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, old_document, self. Outputs/bindings: (none).
Calls/effect boundaries: old_document.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[10].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:37`; AST `5942678fe88cc0e3184561df09b3fccd0f6b7fc55fec95d73e68af8461feda23`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_document. Outputs/bindings: (none).
Calls/effect boundaries: old_document.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[11]::Expr

Source: `infra/tests/test_roadmap_portability.py:38`; AST `b76ca039f2f794b7a7f797fdcf102869684d5ef1d2b5b36e4811faee4b380fbc`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old_document, self, stamp. Outputs/bindings: (none).
Calls/effect boundaries: old_document.stat, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[11].value::Call

Source: `infra/tests/test_roadmap_portability.py:38`; AST `172371bb291840789b7200175c90dd0086210de3b202fa70cb1ab53cf963618c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_document, self, stamp. Outputs/bindings: (none).
Calls/effect boundaries: old_document.stat, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[11].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:38`; AST `18874097067ae97b41d9dc41b8ca47bc33fee59a27af9f09eff546d3c2602546`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: old_document. Outputs/bindings: (none).
Calls/effect boundaries: old_document.stat.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[11].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[12]::For

Source: `infra/tests/test_roadmap_portability.py:39`; AST `cb4fbe56f5c3cdffb724306055bfabc1c686cfc6b03acbc3f1c230e5ddf589ce`.

Rust module: `infra::tests::test_roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: owned, raw, relative, self. Outputs/bindings: raw, relative.
Calls/effect boundaries: (self.base / relative).read_bytes, owned.items, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[2].body[12]; no call, error or mutation may be omitted. Iteration: (relative, raw) in owned.items()
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[12].iter::Call

Source: `infra/tests/test_roadmap_portability.py:39`; AST `cdd499cd0503e317b3b71fecb248b0a43855d55f9ed3c0a2e8ec79497e67ad76`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owned. Outputs/bindings: (none).
Calls/effect boundaries: owned.items.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[12].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[12].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:39`; AST `5ffd5458d100d89f6c5d4214b207f33264bef8b5594e13a29432f3490e9a3017`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / relative).read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[12].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:39`; AST `3e69129cf53dd670f6f56d93199f18cc8d96a69b4f484ebd1890f64e932d9f81`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, relative, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / relative).read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[12].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:39`; AST `b1d57cc7917bf9732d08c474ccf0bc52607ffad67be938c467f6d680c5a29c5d`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: relative, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / relative).read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[12].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[13]::Expr

Source: `infra/tests/test_roadmap_portability.py:40`; AST `7cbfd581a9639a086869b4da14b8f4b70a1ffc2086b684299b98530208832064`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, second, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[13].value::Call

Source: `infra/tests/test_roadmap_portability.py:40`; AST `a75fd4c3c5a7ad5471369f4c2b54e96fac3e1c6e8321314b45419c821ac4f30c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, second, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[13].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:40`; AST `1aca5e40af82985e89a192402ada3d35f2b3019f9d70b8047bbb0122b6af7640`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, second, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[13].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[14]::Expr

Source: `infra/tests/test_roadmap_portability.py:41`; AST `0ad7c079e14c005bca1433a7edc9c18fb79cf633f31fab2611986528c95cf953`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertLessEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[14].value::Call

Source: `infra/tests/test_roadmap_portability.py:41`; AST `92ee76209cd227a804192cb4a27708b87da33407f572ec6b0cddbc01cabe46d6`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertLessEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[15]::Expr

Source: `infra/tests/test_roadmap_portability.py:42`; AST `bdf7146dcdb99f0c0574e612417d7c473dfd50d81ba7b8f845f23f86b3aa5532`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, second, self. Outputs/bindings: (none).
Calls/effect boundaries: publish, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[15].value::Call

Source: `infra/tests/test_roadmap_portability.py:42`; AST `f25ce4a4afb3a09506266a6642edd9f9362406631dac0b675c6c052ef67a1831`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, second, self. Outputs/bindings: (none).
Calls/effect boundaries: publish, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_editing_one_source_leaves_other_document_and_shard_bytes_unchanged::root.body[12].body[2].body[15].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:42`; AST `e407467ff9779b246c928b9e57b5ce6961e8595eafb8ca5cf6e191861cb76255`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, second, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[15].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:44`; AST `113e6fda9d4cc158cd4c3ed57e2dbe56cef7b83073534dfb2066341edce2c10e`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, change, inventory, path, publish, record, self. Outputs/bindings: change, path, record.
Calls/effect boundaries: (self.root / 'infra/a.py').unlink, (self.root / 'infra/added.py').write_text, inventory, path.parent.mkdir, path.write_text, publish, self.assertRaisesRegex, self.subTest.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0]::For

Source: `infra/tests/test_roadmap_portability.py:45`; AST `b3fe3c351fbde812f5a38c36d3364f5661979890fcd37bb414d81f7de2536be5`.

Rust module: `infra::tests::test_roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, change, inventory, path, publish, record, self. Outputs/bindings: change, path, record.
Calls/effect boundaries: (self.root / 'infra/a.py').unlink, (self.root / 'infra/added.py').write_text, inventory, path.parent.mkdir, path.write_text, publish, self.assertRaisesRegex, self.subTest.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted. Iteration: change in ('add', 'delete', 'override')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0]::With

Source: `infra/tests/test_roadmap_portability.py:46`; AST `d299cf2e21ae9624c3d8db2f5b62766a664964d4019be00652a8535e5c992ec4`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, change, inventory, path, publish, record, self. Outputs/bindings: path, record.
Calls/effect boundaries: (self.root / 'infra/a.py').unlink, (self.root / 'infra/added.py').write_text, inventory, path.parent.mkdir, path.write_text, publish, self.assertRaisesRegex, self.subTest.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:46`; AST `4e3239625279997680cb3a05426c614ed3b48e93e9e97caf403e535c23727457`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: change, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:47`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:47`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1]::If

Source: `infra/tests/test_roadmap_portability.py:48`; AST `b72a84b87da2865b1a71f1b936e7152d648ce6c90800718ca392ad57dba6af69`.

Rust module: `infra::tests::test_roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: change, path, self. Outputs/bindings: path.
Calls/effect boundaries: (self.root / 'infra/a.py').unlink, (self.root / 'infra/added.py').write_text, path.parent.mkdir, path.write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[0].body[0].body[1]; no call, error or mutation may be omitted. Condition: change == 'add'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:48`; AST `be434a10f23e274466258bf4f3e24ff35ea902030d82226db8a6f0944e61c451`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/added.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:48`; AST `c87a3a752af421ba7d364d7ef8205f69bf20434d26c96c691d23e05372b1e091`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/added.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0]::If

Source: `infra/tests/test_roadmap_portability.py:49`; AST `9db72e6b5628abf13e3959434786a56a779e46e705a5324b0842b9ab2feb2e28`.

Rust module: `infra::tests::test_roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: change, path, self. Outputs/bindings: path.
Calls/effect boundaries: (self.root / 'infra/a.py').unlink, path.parent.mkdir, path.write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: change == 'delete'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:49`; AST `119c7dcc350646ae2faf01dc4d746c6e437c6fa65ec0c93be7d67b16c5d0355d`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').unlink.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:49`; AST `f2100858c7284f575e82d2e9ad6faa1bf65a6c0143d546a904b76c0a7ae10aef`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').unlink.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:51`; AST `905b2b784c3c83702f5108e6a284877c136cb482c3eb9c3cd003979746ed4577`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:51`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:51`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[2]::Expr

Source: `infra/tests/test_roadmap_portability.py:52`; AST `32bb72ada71852dbea13663b76fc05684f4a298023aabd6cff5f3274fed2e42a`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:52`; AST `02cad40b7231e15a677229fe0d608921452610312de98e5c5255cf14b17073ad`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[1].orelse[0].orelse[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[2]::With

Source: `infra/tests/test_roadmap_portability.py:53`; AST `bcdb93fb29e94793f79a044a4c3f67f9bf1c3e0909c62562b47a45af83956539`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:53`; AST `801ee8671a466add13f02452a2e0d8d93e332ba0c953abb47cece430737b049e`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:54`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[0].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_source_additions_deletions_and_override_edits_invalidate_captured_generation::root.body[12].body[3].body[0].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:54`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:56`; AST `809d90a66a911821fc3238dc9ab0c207ba15b04624c6ea22c79e81043b06c135`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, all, canonical, dict, i, index, len, p, parts, range, record, s, self, shards, str, u, units. Outputs/bindings: i, index, p, parts, record, s, u, units.
Calls/effect boundaries: all, canonical, dict, len, parts.values, range, self.assertEqual, self.assertRaisesRegex, self.assertTrue, shards, str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:57`; AST `32005f9586ecf136dc3617a2a9e8e70fc2be60954f574881373f8bdac6707520`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, i, range, str. Outputs/bindings: i, units.
Calls/effect boundaries: dict, range, str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[0].value::ListComp

Source: `infra/tests/test_roadmap_portability.py:57`; AST `c7445c56222359b02ed7db46959e6ae33db02c1c49293f268f468524ce37f03f`.

Rust module: `infra::tests::test_roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: dict, i, range, str. Outputs/bindings: i.
Calls/effect boundaries: dict, range, str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[0].value.elt::Call

Source: `infra/tests/test_roadmap_portability.py:57`; AST `27d4afe24109a3ff84a95b89ef5c17076f031bef2fcbe80e97b226f91a378291`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, i, str. Outputs/bindings: (none).
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[0].value.elt.keywords[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:57`; AST `3480c9734dde8ba366f953e1f08b6c8860809f5c547f367960e813792d6cd22a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value.elt.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[0].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_portability.py:57`; AST `a409a903687ffb87d3c2b9daad7c5418b6ef99ae3d8bb3b29355c25b976e3543`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_portability.py:58`; AST `5341cd00d5d724017107738ddc58a9136a6744b0336e15539346630ea8a2fbb5`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, units. Outputs/bindings: record.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:58`; AST `b99ea2f22dea4caca72faeb22ab38ad5a3007134c898922426ca79ba528478aa`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, units. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[2]::Assign

Source: `infra/tests/test_roadmap_portability.py:59`; AST `84699a3ac7b5d8723912e92dbeac3e9f6cd5ee247380e6870b665a8c561370e6`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, shards. Outputs/bindings: index, parts.
Calls/effect boundaries: shards.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:59`; AST `a11dc777784adaf3227785513b709bec30d0c25fb5e0f071bf3317257c7bdee3`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, shards. Outputs/bindings: (none).
Calls/effect boundaries: shards.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_portability.py:60`; AST `60bb5e565d42ad1a4cc756d766360245d30312863756f9b8165b2cc6c7c7a19e`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, parts, self, u, units. Outputs/bindings: p, u.
Calls/effect boundaries: parts.values, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:60`; AST `85d3ba98614106535fb0eca37dcdd9d9aeb8b2e8947a98ffbe5297afc2c27b1a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, parts, self, u, units. Outputs/bindings: p, u.
Calls/effect boundaries: parts.values, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[3].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_portability.py:60`; AST `1169f51a63a1e415355b27f4bb696f20bf95f4b973d841000dbe2f072d9f2e21`.

Rust module: `infra::tests::test_roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: p, parts, u. Outputs/bindings: p, u.
Calls/effect boundaries: parts.values.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[3].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_portability.py:60`; AST `ba7f837c60b04e22a610823269d8e0368bc2b1b0a944345ebafdac7abde8d1c4`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.values.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_portability.py:61`; AST `18c4896c5bbeb2365cac12512bd9d996dd3a0bd6ba7be7b71442dc607d3f3896`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, canonical, len, p, parts, self. Outputs/bindings: p.
Calls/effect boundaries: all, canonical, len, parts.values, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_portability.py:61`; AST `b0688b60a38e9d0a0592fa222a64123949d773cddf793e48b2402b21a01c8880`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, canonical, len, p, parts, self. Outputs/bindings: p.
Calls/effect boundaries: all, canonical, len, parts.values, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:61`; AST `78a200fd82d11a53309a93f148d2298122f2e3b651a6a0348a750d524df561c0`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, canonical, len, p, parts. Outputs/bindings: p.
Calls/effect boundaries: all, canonical, len, parts.values.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_portability.py:61`; AST `abc81c102ef6753ed8fd034bd0cbb7e646513fbfe66fb57f3cdf0afe92fd5071`.

Rust module: `infra::tests::test_roadmap_portability`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: canonical, len, p, parts. Outputs/bindings: p.
Calls/effect boundaries: canonical, len, parts.values.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[4].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value.args[0].args[0].elt.left.left::Call

Source: `infra/tests/test_roadmap_portability.py:61`; AST `4be31ec0e429f5e8644d61125b9541b08818639af18a222f7ec7ac3ac51ab97a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, len, p. Outputs/bindings: (none).
Calls/effect boundaries: canonical, len.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value.args[0].args[0].elt.left.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value.args[0].args[0].elt.left.left.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:61`; AST `1838f341bd651149f200aa19b211053e80c66143a16301be6c7efe744ca92b0f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, p. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value.args[0].args[0].elt.left.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[4].value.args[0].args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_portability.py:61`; AST `ba7f837c60b04e22a610823269d8e0368bc2b1b0a944345ebafdac7abde8d1c4`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parts. Outputs/bindings: (none).
Calls/effect boundaries: parts.values.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_portability.py:62`; AST `5767ffbad0d2989b3b56d65d370140ea979ce839c9dad81813c435a36f6db057`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, index, s, self. Outputs/bindings: s.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_portability.py:62`; AST `49cc0aa4935a13bef047d3bbc64a323699d1335f332bfb4e2f53d75ec4193222`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, index, s, self. Outputs/bindings: s.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:62`; AST `1c3530f8dd9303838174a178e38960c58b87ccc1068336ce910f9337e09c6dd7`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, index, s. Outputs/bindings: s.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[5].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_portability.py:62`; AST `e163fd78d563cbc97a35c9b622cc1920c51cc7cd096aa9ddd7478200bc831319`.

Rust module: `infra::tests::test_roadmap_portability`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: index, s. Outputs/bindings: s.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[4].body[5].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[6]::With

Source: `infra/tests/test_roadmap_portability.py:63`; AST `bada28c5dc47950a0761c603cd37d77e08b7e25f51b446dc8649d112d451e725`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, record, self, shards. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, shards.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:63`; AST `1a0b52199505e1dfc6d3df8a7c7a73853c10537472efc171ae4ac0f5bd026845`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:64`; AST `525966709416eb0ca982e8a982fc3541a97d2a199f5c091a67a224089c0b3c18`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, shards. Outputs/bindings: (none).
Calls/effect boundaries: shards.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_physical_utf8_shard_bound_includes_envelope_and_final_newline::root.body[12].body[4].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:64`; AST `959dd8c36164a15ce6c87a4da2bbaac2b9e3b5617ed2d0d692b9105d881771d8`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, shards. Outputs/bindings: (none).
Calls/effect boundaries: shards.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:66`; AST `37a22e0b8ac90cb49050e0bb91ae1e5c872f7ee48823ddba20701b219af91439`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, before, check, inventory, path, publish, record, self. Outputs/bindings: before, path, record.
Calls/effect boundaries: check, inventory, path.read_bytes, path.write_bytes, publish, self.assertEqual, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:67`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:67`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:67`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:67`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[2]::Assign

Source: `infra/tests/test_roadmap_portability.py:68`; AST `f74b8b3e222734007bb5dbdb267468eb12efb1fd0d2b14224e38035ce0c4dcce`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[3]::Expr

Source: `infra/tests/test_roadmap_portability.py:68`; AST `edd25e361af486a97e991d890891e4054c5721af402a7f2c636252a0a591afec`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, path.write_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:68`; AST `6d1e56179e99ecbc46fe68f19d1514e50979583d9fa4b47af228ca9a0277d7b0`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, path.write_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[3].value.args[0].left::Call

Source: `infra/tests/test_roadmap_portability.py:68`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[4]::Assign

Source: `infra/tests/test_roadmap_portability.py:69`; AST `7be2c3931aa069b4d490b975d00dcc6fda3e361647bf2bec6a22f528d37d0897`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[4].value::Call

Source: `infra/tests/test_roadmap_portability.py:69`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[5]::With

Source: `infra/tests/test_roadmap_portability.py:70`; AST `8b1b043c0f21b3df8c96aa87136c81a52db16ad836e630f36b3f40f27dfbb6a0`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:70`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:70`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:70`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[6]::Expr

Source: `infra/tests/test_roadmap_portability.py:71`; AST `42c88e9cd5b261e9d53f8010a597ed26949ea0b52744950f44e3cfaf0b2133f9`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[6].value::Call

Source: `infra/tests/test_roadmap_portability.py:71`; AST `5ca0d971b1a61c0727bb77dd1b4a92521d9badb136b4d40681096ec1032a4ac5`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:71`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[7]::With

Source: `infra/tests/test_roadmap_portability.py:72`; AST `b30561a616f95e4f6c3f28edd79d50ec5d4fa7010f2c35586f8cd8d83f469b07`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[7].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:72`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:72`; AST `76234d8c5ba4d77fb069c225972ae7715a6c987095a4f5fe3d08e6b41f07b6eb`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_edits_to_owned_artifacts_are_preserved_and_block_regeneration::root.body[12].body[5].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:72`; AST `5e262dd0d842995b0fa9bef7b02bd7af6bcacc00044f25cf275c5a80c4235d1b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:74`; AST `31481061f8418fdc5cb371b9467e2b85fb0fe5e824a2dfce9fc0434d276fea5b`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: check, current, dict, digest, index, inventory, json, len, local, markdown, old, publish, read_json, record, resolved, self, shard, source, u. Outputs/bindings: current, index, local, old, record, resolved, shard, source, u.
Calls/effect boundaries: (self.base / 'inventory.json').write_text, (self.base / 'units/units-0000.json').exists, (self.base / 'user-notes.txt').read_text, (self.base / 'user-notes.txt').write_text, (self.base / (source['path'].replace('/', '__') + '.md')).write_text, check, dict, digest, inventory, json.dumps, len, markdown, publish, read_json, self.assertEqual, self.assertFalse, self.base.joinpath, self.base.joinpath('units').mkdir, self.base.joinpath('units/units-0000.json').write_text, source['path'].replace.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:75`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:75`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[1]::Assign

Source: `infra/tests/test_roadmap_portability.py:77`; AST `436879b6a3d8b1e5cf77c679deccf4748852217779b8be50a14b5dd50d1991be`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: old.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_portability.py:78`; AST `b3851da4b7cca100e0e30a01a295226bcc96937befc2e47e629b6b2d96acd32e`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.joinpath, self.base.joinpath('units').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:78`; AST `cd6c42752735fbac8ffc259d4040ad2bc4fc9113195156b096c54a214341a347`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.joinpath, self.base.joinpath('units').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[2].value.func.value::Call

Source: `infra/tests/test_roadmap_portability.py:78`; AST `c2435f1e68d0f75752b82fad5a78161764cc25bbc875931a7b142055b07a9af9`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.joinpath.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[3]::Expr

Source: `infra/tests/test_roadmap_portability.py:79`; AST `25babd7e93d61a7c4d8388c133abd155b0b2a83dcb1e5423c0399a4cf3774d82`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, old, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.base.joinpath, self.base.joinpath('units/units-0000.json').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:79`; AST `7ccd3e219e3a9e0848057a88160a1b7d2ba3f3ea0f55fd325986b52229c03d32`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, old, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, self.base.joinpath, self.base.joinpath('units/units-0000.json').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[3].value.func.value::Call

Source: `infra/tests/test_roadmap_portability.py:79`; AST `ac65eaa7d98877bf2e90ff670bfd0dcef4c6ba249b904cf70929c0dc4971c521`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.joinpath.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[3].value.args[0].left::Call

Source: `infra/tests/test_roadmap_portability.py:79`; AST `4bf8d602fac692738ba426443e1b45ae84d0d27002ca5c672776f00d3fb41316`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, old. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[4]::Assign

Source: `infra/tests/test_roadmap_portability.py:80`; AST `f83fb302afcf75d636d155ad65e6cdf7b589689ac69c1107bccdb2f7f7302cc6`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, len, old, record. Outputs/bindings: index.
Calls/effect boundaries: digest, len.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[4].value.values[4]::Call

Source: `infra/tests/test_roadmap_portability.py:81`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[4].value.values[6].elts[0].values[1]::Call

Source: `infra/tests/test_roadmap_portability.py:82`; AST `f4f5a4cedc09ec12f98623aa9598e1dadaf46cc187b728dfea5ab29f4f3b0811`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, old. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value.values[6].elts[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[4].value.values[6].elts[0].values[2]::Call

Source: `infra/tests/test_roadmap_portability.py:82`; AST `cf288c8de9d42d513d1b1a52a032da7d5a8fe3f6b9b95d79ce2bd7139ad15ee4`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value.values[6].elts[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_portability.py:83`; AST `6252d5010c88a6b4d0f7079e65c489ddeea4ff0725e937066af6494af9bf5bbd`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: index, json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'inventory.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_portability.py:83`; AST `cc3665ab61c5c730af9dbc9461600230f190b90d85e27a253beef1be00f727ba`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'inventory.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[5].value.args[0].left::Call

Source: `infra/tests/test_roadmap_portability.py:83`; AST `0325cc757d50a0714ea46a4458c2bd6d393d5691e6ce5f933ea43f9a53f2897f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: index, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6]::For

Source: `infra/tests/test_roadmap_portability.py:84`; AST `c1875c8b73c3147057c925aaabb45280e28ce228a642dbbcc57ca84814a0d723`.

Rust module: `infra::tests::test_roadmap_portability`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: dict, local, markdown, record, self, source, u. Outputs/bindings: local, source, u.
Calls/effect boundaries: (self.base / (source['path'].replace('/', '__') + '.md')).write_text, dict, markdown, source['path'].replace.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[6].body[6]; no call, error or mutation may be omitted. Iteration: source in record['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_portability.py:85`; AST `56c538479cce4e4e169bd88a1a3bb8c2587f3a158203c004a4294efc8ecd2e2c`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, record, source, u. Outputs/bindings: local, u.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:85`; AST `2bec37b2117c2f8cfd20b367c5beed29cc6746cef8c59d2b542d657e811b3fb1`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, record, source, u. Outputs/bindings: u.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[0].value.keywords[1].value::ListComp

Source: `infra/tests/test_roadmap_portability.py:85`; AST `8c3a41aa19526923efb80703034df2bb0908e38a152bb6f470320106bab452fd`.

Rust module: `infra::tests::test_roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: record, source, u. Outputs/bindings: u.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[6].body[6].body[0].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:86`; AST `c7639a95f4f559bb830810b5cf48747cf4efb3b9d4fb5ac1d8647e81efdfb0ba`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: local, markdown, self, source. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / (source['path'].replace('/', '__') + '.md')).write_text, markdown, source['path'].replace.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:86`; AST `e7463bf46d31afff8aa3dd97ecdcfe3f51dcc1b17e776ad310b5b032f91f9ae1`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: local, markdown, self, source. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / (source['path'].replace('/', '__') + '.md')).write_text, markdown, source['path'].replace.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[1].value.func.value.right.left::Call

Source: `infra/tests/test_roadmap_portability.py:86`; AST `9b2de27704610ae2cbf3b2beffecf18cf8cdd0f1d8e61bbef3eb0ac16d02a512`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source['path'].replace.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].body[1].value.func.value.right.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[6].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:86`; AST `dbf9e5722c8177ff78bdbe305e7d02bd9a18e883bee89f60a375c06647425bbd`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: local, markdown. Outputs/bindings: (none).
Calls/effect boundaries: markdown.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[6].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[7]::Expr

Source: `infra/tests/test_roadmap_portability.py:87`; AST `e010b7a90e4af1dc35d2a20d47773599314991c4fcee6fc4d53cda740ff18afa`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'user-notes.txt').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[7].value::Call

Source: `infra/tests/test_roadmap_portability.py:87`; AST `5f8cabb810b26b4ebea387b803b09a5c4deb360c65754c941df6192b542f3675`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'user-notes.txt').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[8]::Expr

Source: `infra/tests/test_roadmap_portability.py:88`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[8].value::Call

Source: `infra/tests/test_roadmap_portability.py:88`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[9]::Assign

Source: `infra/tests/test_roadmap_portability.py:89`; AST `a6a5a6f7578f439b8397ccba3fbd4d27fc5962647b0504836d301d5a9ac77ca3`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, self. Outputs/bindings: current.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[9].value::Call

Source: `infra/tests/test_roadmap_portability.py:89`; AST `a38edc7ca35b2b10f19d02de30239427671e37b4426ae032a98556968070b670`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[10]::Assign

Source: `infra/tests/test_roadmap_portability.py:90`; AST `928f3cc8f38da8c2619156dcddb5257e4b657e79d8f494bd999b1bae1a9c5e36`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, read_json, self, shard, u. Outputs/bindings: resolved, shard, u.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[10].value::ListComp

Source: `infra/tests/test_roadmap_portability.py:90`; AST `9d397cc7bd0ad7194764451561e79b46554867612df314423ae23578f16d0df0`.

Rust module: `infra::tests::test_roadmap_portability`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: current, read_json, self, shard, u. Outputs/bindings: shard, u.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[6].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[10].value.generators[1].iter.value::Call

Source: `infra/tests/test_roadmap_portability.py:90`; AST `76f1adeaaa6c7a24d5146fe28a298308f0cc87a155a64adfb1ec39ed847034a6`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, self, shard. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[10].value.generators[1].iter.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[11]::Expr

Source: `infra/tests/test_roadmap_portability.py:91`; AST `2d1c68b3dcbf8e90f8b8baca3334136ce1347b82b04d22fe5875e4a792bf71b5`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, resolved, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[11].value::Call

Source: `infra/tests/test_roadmap_portability.py:91`; AST `36cdb208f80b60b6b8e0e5c0a6437fd11296900ea726a50f3e68d77aac81f00b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, resolved, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[12]::Expr

Source: `infra/tests/test_roadmap_portability.py:92`; AST `22b1daf4f01ac6ce338a54b8fe4445289c2f8649e45526dcac0a3664391fd8b3`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'units/units-0000.json').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[12].value::Call

Source: `infra/tests/test_roadmap_portability.py:92`; AST `023cef91dfc5b2742868fd9c4971aea1a304acaa29f3334ad1c8676b46988492`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'units/units-0000.json').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[12].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:92`; AST `359eaa81a3e3c782ad84b6c0aff002ce8e53853fac8347fa2e541b6a338f46cb`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'units/units-0000.json').exists.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[13]::Expr

Source: `infra/tests/test_roadmap_portability.py:93`; AST `62b2d1032500860e231889c3c5946af239418ce50481fe19d4e88dd93d0564b0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'user-notes.txt').read_text, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[13].value::Call

Source: `infra/tests/test_roadmap_portability.py:93`; AST `729c79401ffc776d2b69c52cf4dc77c90673fb7cf0846171fc51514ebed6266b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'user-notes.txt').read_text, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[13].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:93`; AST `f93ddfd305063f9d616d46fab152c90dc1adb91279f2190c3971aff837a6446f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'user-notes.txt').read_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[13].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[14]::Expr

Source: `infra/tests/test_roadmap_portability.py:94`; AST `1ca21f717b7e0cc898e5c7a35fe2f30b959295d4768867d28f1709d37429ddc0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[14].value::Call

Source: `infra/tests/test_roadmap_portability.py:94`; AST `d1a512e03cb41e94c42e0b3e723dc56a9d6fe7f3f33c77c1c94811c94e6f9579`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_legacy_layout_migration_preserves_every_unit_and_unowned_file::root.body[12].body[6].body[14].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:94`; AST `5e262dd0d842995b0fa9bef7b02bd7af6bcacc00044f25cf275c5a80c4235d1b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[14].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:96`; AST `e40bcb6ea757151fcf618b732d0c9239abfbd4d9bfd633922887ca7acab88ecf`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: check, inventory, publish, record, self. Outputs/bindings: record.
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists, (self.base / 'infra__b.py.md').exists, (self.root / 'infra/a.py').unlink, check, inventory, publish, self.assertEqual, self.assertFalse, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:97`; AST `71cfe3237109df906bfe944f146ecdd9366565cb418aeaf2657a2190e908e48f`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:97`; AST `5378c4041c56a6086f9d2a4354aed3963a3f3c76f6fb580b5f27694cb2cb9d3c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_portability.py:97`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:98`; AST `119c7dcc350646ae2faf01dc4d746c6e437c6fa65ec0c93be7d67b16c5d0355d`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').unlink.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:98`; AST `f2100858c7284f575e82d2e9ad6faa1bf65a6c0143d546a904b76c0a7ae10aef`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').unlink.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[2]::Assign

Source: `infra/tests/test_roadmap_portability.py:99`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:99`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[3]::Expr

Source: `infra/tests/test_roadmap_portability.py:99`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:99`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[4]::Expr

Source: `infra/tests/test_roadmap_portability.py:100`; AST `1fb07fe6df321849c10acb1eb9d4f4f4f42e6f40a1fa28c0b3aa52feee55dfbd`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[4].value::Call

Source: `infra/tests/test_roadmap_portability.py:100`; AST `fefb7cd50a7a34a24cf8f8927fe68d9a3fb446f1d7223409fbc50f03bef50d8e`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:100`; AST `0cbc789401c4cf3a4391ed4e1d833b4fc04ea1d3c8021284c1382fe881e707eb`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__a.py.md').exists.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[5]::Expr

Source: `infra/tests/test_roadmap_portability.py:101`; AST `d6915318be708acaaa93faaa00006e5a199a2bff1ade256cd3e5017cd97372a0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__b.py.md').exists, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[5].value::Call

Source: `infra/tests/test_roadmap_portability.py:101`; AST `26a0685e84ee5eb558710df8ce2afd5d55388b80c3a28dbafc79490ae0c007cd`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__b.py.md').exists, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:101`; AST `0001b720e3f4ffb0f9c9b84233858e5be878fc2a37b99cbd5649de4827610f19`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'infra__b.py.md').exists.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[6]::Expr

Source: `infra/tests/test_roadmap_portability.py:102`; AST `1ca21f717b7e0cc898e5c7a35fe2f30b959295d4768867d28f1709d37429ddc0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[6].value::Call

Source: `infra/tests/test_roadmap_portability.py:102`; AST `d1a512e03cb41e94c42e0b3e723dc56a9d6fe7f3f33c77c1c94811c94e6f9579`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_deleted_source_retires_only_its_owned_generated_artifacts::root.body[12].body[7].body[6].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:102`; AST `5e262dd0d842995b0fa9bef7b02bd7af6bcacc00044f25cf275c5a80c4235d1b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:104`; AST `38fbd7ff53682e94bc0af64585795066ae5e36059ed6d17bb134b9f271649544`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, OSError, after, args, before, check, fail, inventory, kwargs, p, patch, publish, record, self, stage, transaction. Outputs/bindings: after, before, p, record.
Calls/effect boundaries: (self.root / 'infra/a.py').write_text, FileTransaction, OSError, check, inventory, p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, patch, publish, self.assertEqual, self.assertRaisesRegex, self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:105`; AST `71cfe3237109df906bfe944f146ecdd9366565cb418aeaf2657a2190e908e48f`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:105`; AST `5378c4041c56a6086f9d2a4354aed3963a3f3c76f6fb580b5f27694cb2cb9d3c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, publish, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory, publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_portability.py:105`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1]::Assign

Source: `infra/tests/test_roadmap_portability.py:106`; AST `0c191aef00c871a4a6cabd4453b49ee8a2fdec149e7bd3b5b2f1b712402403fc`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, self. Outputs/bindings: before, p.
Calls/effect boundaries: p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value::DictComp

Source: `infra/tests/test_roadmap_portability.py:106`; AST `6f8903e91ac343bd6f2e651e69f23540aab423b1621e6bcdbd504f1d8c9236a5`.

Rust module: `infra::tests::test_roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: p, self. Outputs/bindings: p.
Calls/effect boundaries: p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value.key::Call

Source: `infra/tests/test_roadmap_portability.py:106`; AST `bd7a067b7242e0bb35918341d7cf43993fd1d5646a7a740fd40c8f22f6d25e4a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, self. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(self.base).as_posix.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value.key; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value.key.func.value::Call

Source: `infra/tests/test_roadmap_portability.py:106`; AST `2dff1e6a7ba986c5aabb2fc56244d8b59c19e48109191697a876fdcd852c9145`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, self. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value.key.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value.value::Call

Source: `infra/tests/test_roadmap_portability.py:106`; AST `6b83dca35b721a6480711503aa48f3d020a7a02c07f5371d07b93bdc3b0800e8`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_portability.py:106`; AST `8789029c2dfb7dd5fb1508108243197029dc9c781a9b1d2f221adaba91937460`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[1].value.generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_portability.py:106`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[2]::Expr

Source: `infra/tests/test_roadmap_portability.py:107`; AST `d26f0db2e86428b4997441004383f93ecf23ad4887b71c9eb1d096c2bcd59f91`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:107`; AST `0b7c2a1e1b00f6163496044e03029b8fb6a53eb60ed006e7b27671527dd1164d`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/a.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[3]::Assign

Source: `infra/tests/test_roadmap_portability.py:108`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:108`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::fail::root.body[12].body[8].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:110`; AST `ff1f296fb7bb688ac1a08fa2d0492c093d42590c100f0edb44ae716f97c507ac`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, stage. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::fail::root.body[12].body[8].body[4].body[0]::If

Source: `infra/tests/test_roadmap_portability.py:111`; AST `13d12204f6c4a1203c397c29c83c8b255af241dbc7088c9d57332e62fbe3bdef`.

Rust module: `infra::tests::test_roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: OSError, stage. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[8].body[4].body[0]; no call, error or mutation may be omitted. Condition: stage == 'after_destination'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::fail::root.body[12].body[8].body[4].body[0].body[0]::Raise

Source: `infra/tests/test_roadmap_portability.py:111`; AST `0f85576fc984261d3c4a77bbf1eedc0fa88ce32b36af2239886ffe7e81264bd6`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Raise evaluation at root.body[12].body[8].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::fail::root.body[12].body[8].body[4].body[0].body[0].exc::Call

Source: `infra/tests/test_roadmap_portability.py:111`; AST `e6907ef5b45247af71aee7ab3c22ecc5216b4051fffbc0bbc382a8749708d38a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[4].body[0].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::transaction::root.body[12].body[8].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:113`; AST `d826f13529f947ce8efd29c8031daf75a11c8c03ec668d6c9b95add145b2c1e8`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileTransaction, args, fail, kwargs. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::transaction::root.body[12].body[8].body[5].body[0]::Return

Source: `infra/tests/test_roadmap_portability.py:114`; AST `8221611ca76c02338ab8b874b5ef40153f1c4cfff424d5302ddaa8c774d8877a`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileTransaction, args, fail, kwargs. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[8].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::transaction::root.body[12].body[8].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:114`; AST `76ea7819b3bb36b98ab0b4a2e41b41e578eb2e2521f03d704dcac662ea40fab0`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileTransaction, args, fail, kwargs. Outputs/bindings: (none).
Calls/effect boundaries: FileTransaction.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6]::With

Source: `infra/tests/test_roadmap_portability.py:116`; AST `4998dea2a5449e4756b92bddd9a875f9cda7673d56b8164b57f997dd26461c85`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: OSError, patch, publish, record, self, transaction. Outputs/bindings: (none).
Calls/effect boundaries: patch, publish, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:116`; AST `e6f08aaa365ad997f030a0227679cb8f9e6b2c7fafed82d340aba0131cd7aeea`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, transaction. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6].body[0]::With

Source: `infra/tests/test_roadmap_portability.py:117`; AST `bf300358cb0edc13fb2865ef31dfc20526f4b9885c9bafd9bf378b0f98f66373`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: OSError, publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:117`; AST `2cdc378012de1524bc930582ae4869f37014305a930ab8bcfb2d71b271e64b64`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:118`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:118`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7]::Assign

Source: `infra/tests/test_roadmap_portability.py:119`; AST `98cc7bd50785ebe6e5d35089a5e1b125c05763895782a6389331f0d8f729bddd`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, self. Outputs/bindings: after, p.
Calls/effect boundaries: p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value::DictComp

Source: `infra/tests/test_roadmap_portability.py:119`; AST `6f8903e91ac343bd6f2e651e69f23540aab423b1621e6bcdbd504f1d8c9236a5`.

Rust module: `infra::tests::test_roadmap_portability`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: p, self. Outputs/bindings: p.
Calls/effect boundaries: p.is_file, p.read_bytes, p.relative_to, p.relative_to(self.base).as_posix, self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value.key::Call

Source: `infra/tests/test_roadmap_portability.py:119`; AST `bd7a067b7242e0bb35918341d7cf43993fd1d5646a7a740fd40c8f22f6d25e4a`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, self. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(self.base).as_posix.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value.key; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value.key.func.value::Call

Source: `infra/tests/test_roadmap_portability.py:119`; AST `2dff1e6a7ba986c5aabb2fc56244d8b59c19e48109191697a876fdcd852c9145`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, self. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value.key.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value.value::Call

Source: `infra/tests/test_roadmap_portability.py:119`; AST `6b83dca35b721a6480711503aa48f3d020a7a02c07f5371d07b93bdc3b0800e8`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.read_bytes.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_portability.py:119`; AST `8789029c2dfb7dd5fb1508108243197029dc9c781a9b1d2f221adaba91937460`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.base.rglob.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[7].value.generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_portability.py:119`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[8]::Expr

Source: `infra/tests/test_roadmap_portability.py:120`; AST `eef317b99241e740fea53b4037eb045b61536148315a994abdc01d726e43d852`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[8].value::Call

Source: `infra/tests/test_roadmap_portability.py:120`; AST `906712e3861b8b0073714ac747ee375c6779f5c44cbfdc995f8f1558615c394f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[9]::Expr

Source: `infra/tests/test_roadmap_portability.py:121`; AST `bcc828fe1aadf1e803a533cc766fe7ff9f4b56d8aef7e70366e5c4a46d2dd994`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[9].value::Call

Source: `infra/tests/test_roadmap_portability.py:121`; AST `c33b92ab786ff033a75db9caa3a7a1f9a4c6dea17164fa163c8c7e8d8944e226`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: publish, record, self. Outputs/bindings: (none).
Calls/effect boundaries: publish.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[10]::Expr

Source: `infra/tests/test_roadmap_portability.py:122`; AST `1ca21f717b7e0cc898e5c7a35fe2f30b959295d4768867d28f1709d37429ddc0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[10].value::Call

Source: `infra/tests/test_roadmap_portability.py:122`; AST `d1a512e03cb41e94c42e0b3e723dc56a9d6fe7f3f33c77c1c94811c94e6f9579`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_interrupted_publication_restores_old_artifacts_and_reuses_existing_recovery::root.body[12].body[8].body[10].value.args[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:122`; AST `5e262dd0d842995b0fa9bef7b02bd7af6bcacc00044f25cf275c5a80c4235d1b`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: check, record, self. Outputs/bindings: (none).
Calls/effect boundaries: check.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[10].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_portability.py:124`; AST `57b213f77c9aea6cd3bdb8f7373dd182b13a9c5187a47961a60ed1ca2682072d`.

Rust module: `infra::tests::test_roadmap_portability`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, artifacts, inventory, record, self. Outputs/bindings: record.
Calls/effect boundaries: (self.base / 'inventory.json').exists, (self.root / 'infra/x').mkdir, (self.root / 'infra/x/y.py').write_text, (self.root / 'infra/x__y.py').write_text, artifacts, inventory, self.assertFalse, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:125`; AST `870b3138cc439a23ef11a55d4e8029b327fcc3b8ee48b00194e256e0306f9da0`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:125`; AST `bb1c9b0275448e6a4fb2b65b00a69770ac825f087518a59efced0be8e8fb14f7`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x').mkdir.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[1]::Expr

Source: `infra/tests/test_roadmap_portability.py:126`; AST `3fac62d205ce08a79529e7f8b710c46232a0c99fa6c62afb3f9537fac80860a2`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x/y.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_portability.py:126`; AST `3e2b353cf95f410fc8e081135a856c3071ecd7cb9a3db426c2c4cf6507cf503e`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x/y.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[2]::Expr

Source: `infra/tests/test_roadmap_portability.py:127`; AST `7e984f17914021a2cd33bd02a7a4cc88d7f4a5ce3076ff82ca91ff9c1f7527ec`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x__y.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[2].value::Call

Source: `infra/tests/test_roadmap_portability.py:127`; AST `d8924d5d0ec49d3bfc21e95dae41ce6ba540fec5ca60f783b6164519ad304421`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'infra/x__y.py').write_text.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[3]::Assign

Source: `infra/tests/test_roadmap_portability.py:128`; AST `6dc5c4fcadacda52b5dd75fd35a60a0ea9924812cb1ce88085c1e4df4408a987`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inventory, self. Outputs/bindings: record.
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_portability.py:128`; AST `808aa3b4691c2be2092462314a85e79d73b93453f6c907e3b21df3fec541c10f`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: inventory.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[4]::With

Source: `infra/tests/test_roadmap_portability.py:129`; AST `042b7f6cd04896e32952b571bdeaf5a717619bb11a3fdf0748a7352b0d117198`.

Rust module: `infra::tests::test_roadmap_portability`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, artifacts, record, self. Outputs/bindings: (none).
Calls/effect boundaries: artifacts, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_portability.py:129`; AST `32630f8f5eb849170cda6117eb7b2c8b4a05c5bbe86211eb9506e572ddefe71c`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:130`; AST `35efc35ba11936812edf63224ee98064338b66cb1c056256cd14d79b4b7d99c6`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, record. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:130`; AST `e871a7c4e4c56cc8b6474f468a3c079fab9a6680d054a5dc6c8086f418e23a35`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, record. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[5]::Expr

Source: `infra/tests/test_roadmap_portability.py:131`; AST `8905f12d5c34362c46e95cab5926317590975b3509f63fca02ea891212974f51`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'inventory.json').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[5].value::Call

Source: `infra/tests/test_roadmap_portability.py:131`; AST `aeb8f84e6db992b214acb871688d0a6c3d08ec2aefcc5627260e00ba00f9b0f1`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'inventory.json').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::PortabilityPublicationTests::test_document_path_collision_cannot_merge_two_source_owners::root.body[12].body[9].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_portability.py:131`; AST `2095cc7b550a97cb6e3070fa3190be29d9e89cb44dd7f8c3faf55afbc4fcfc6e`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.base / 'inventory.json').exists.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[13]::If

Source: `infra/tests/test_roadmap_portability.py:134`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_portability`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_portability.py:135`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_portability`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_portability.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_portability.py:135`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_portability`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_portability, agentinfra.roadmap_records, agentinfra.transaction, json, pathlib, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
