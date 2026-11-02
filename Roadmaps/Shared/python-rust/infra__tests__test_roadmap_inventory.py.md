# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 330. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_inventory.py::module::root::Module

Source: `infra/tests/test_roadmap_inventory.py:1`; AST `0b1e4a7d9c6dd277f11f871d61a7b05e6622280d61ca70509fa5a10e4f9bd0d1`.

Rust module: `infra::tests::test_roadmap_inventory`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, __file__, __name__, all, args, authority_inventory, before, c, canonical, classmethod, cls, component, components, d, definitions, destination, f, files, first, h, inspect_python, json, len, link, nested, next, path, r, raw, read_json, reconcile_inventory, record, reference, remote, result, root, s, same, save_inventory, second, self, shutil, source, sources, staged_first, staged_second, staticmethod, str, subprocess, sys, tempfile, unittest. Outputs/bindings: ROOT, before, c, component, components, d, definitions, destination, f, files, first, h, link, nested, path, r, raw, record, reference, remote, result, s, same, second, source, sources, staged_first, staged_second.
Calls/effect boundaries: (cls.base / '.gitignore').write_text, (cls.base / 'Roadmaps/Shared/sources.json').write_bytes, (cls.base / 'example.py').write_text, (nested / 'kept.py').write_text, (nested / 'user.py').write_text, (reference / 'kept.py').write_text, (self.root / 'example.py').exists, (self.root / 'example.py').unlink, (self.root / 'example.py').write_text, (self.root / 'link').symlink_to, (self.root / 'old.py').write_bytes, (self.root / 'user work.bin').read_bytes, (self.root / 'user work.bin').write_bytes, Path, Path(__file__).resolve, all, authority_inventory, canonical, cls.base_temp.cleanup, cls.git, destination.write_text, inspect_python, json.dumps, len, next, path.parent.mkdir, path.read_bytes, path.write_text, read_json, reconcile_inventory, record['requirements'].pop, reference.mkdir, s['path'].lower, s['path'].lower().endswith, save_inventory, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.git, self.temp.cleanup, shutil.copyfile, shutil.copytree, shutil.ignore_patterns, str, subprocess.run, sys.path.insert, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[0]::ImportFrom

Source: `infra/tests/test_roadmap_inventory.py:1`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[1]::Import

Source: `infra/tests/test_roadmap_inventory.py:3`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_inventory.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_inventory.py:5`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_inventory.py:6`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_inventory.py:7`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_inventory.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_inventory.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[8]::Assign

Source: `infra/tests/test_roadmap_inventory.py:11`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[8].value.value.value::Call

Source: `infra/tests/test_roadmap_inventory.py:11`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[8].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_inventory.py:11`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[8].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[9]::Expr

Source: `infra/tests/test_roadmap_inventory.py:12`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[9].value::Call

Source: `infra/tests/test_roadmap_inventory.py:12`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[9].value.args[1]::Call

Source: `infra/tests/test_roadmap_inventory.py:12`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[9].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_inventory.py:14`; AST `7a1502e836c1f6bcb8cf36995ff61f6629fcad7ceac1598a82094014a6a6e9d4`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_inventory.py:15`; AST `87159b510b50762decaa971103b2845f828cb761ded5e73e727c915bf0b2194b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_inventory.py:18`; AST `6a9ca80163d897a383ce7672a5d1ac9ac102db5e4ef36e5ec3eab15b4682e08b`.

Rust module: `infra::tests::test_roadmap_inventory`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, ROOT, all, args, authority_inventory, before, c, canonical, classmethod, cls, component, components, d, definitions, destination, f, files, first, h, inspect_python, json, len, link, nested, next, path, r, raw, read_json, reconcile_inventory, record, reference, remote, result, root, s, same, save_inventory, second, self, shutil, source, sources, staged_first, staged_second, staticmethod, str, subprocess, tempfile, unittest. Outputs/bindings: before, c, component, components, d, definitions, destination, f, files, first, h, link, nested, path, r, raw, record, reference, remote, result, s, same, second, source, sources, staged_first, staged_second.
Calls/effect boundaries: (cls.base / '.gitignore').write_text, (cls.base / 'Roadmaps/Shared/sources.json').write_bytes, (cls.base / 'example.py').write_text, (nested / 'kept.py').write_text, (nested / 'user.py').write_text, (reference / 'kept.py').write_text, (self.root / 'example.py').exists, (self.root / 'example.py').unlink, (self.root / 'example.py').write_text, (self.root / 'link').symlink_to, (self.root / 'old.py').write_bytes, (self.root / 'user work.bin').read_bytes, (self.root / 'user work.bin').write_bytes, Path, all, authority_inventory, canonical, cls.base_temp.cleanup, cls.git, destination.write_text, inspect_python, json.dumps, len, next, path.parent.mkdir, path.read_bytes, path.write_text, read_json, reconcile_inventory, record['requirements'].pop, reference.mkdir, s['path'].lower, s['path'].lower().endswith, save_inventory, self.assertEqual, self.assertFalse, self.assertIsNone, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue, self.git, self.temp.cleanup, shutil.copyfile, shutil.copytree, shutil.ignore_patterns, str, subprocess.run, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:20`; AST `44a9e68e70fe20d638913b45ee92b7c839d6a383cb270a4d81aaf198d8c44893`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, canonical, classmethod, cls, path, read_json, s, shutil, source, sources, tempfile. Outputs/bindings: path, s, source, sources.
Calls/effect boundaries: (cls.base / '.gitignore').write_text, (cls.base / 'Roadmaps/Shared/sources.json').write_bytes, (cls.base / 'example.py').write_text, Path, canonical, cls.git, path.parent.mkdir, read_json, s['path'].lower, s['path'].lower().endswith, shutil.copyfile, shutil.copytree, shutil.ignore_patterns, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:21`; AST `aec18fcd4e8926e38c1abfbd25e790dc71d479e325dd6132e1667c69a4e6a4cf`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:21`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_inventory.py:22`; AST `ea0e23d643d6b4ce2ca320c08fb2930b9f492b0ed4dc5edfa5f338185ccfb6c7`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, cls. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:22`; AST `a41f56fa47ef155c1ee4ff65478fb9771f6266038f60e61b51896c51d98b94ef`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, cls. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:23`; AST `09474f799e10a5a84ddd84877596d9155b37f172f559cbbbdfde6391fc0dfc90`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, cls, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copytree, shutil.ignore_patterns.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:23`; AST `2890d61e3c11031d260a0ede792f3c15d2ab13e851d556e69c6fbf44317f2bf4`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, cls, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copytree, shutil.ignore_patterns.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[2].value.keywords[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:23`; AST `1df4555504c9a93b27ea34926e4905d37ea064de19ece238944fff40452bb37a`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.ignore_patterns.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_inventory.py:24`; AST `8a5e8543cb5d4c3307756b357f3b914a0d90d39594d34a2bf6752c47a22959ce`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, read_json. Outputs/bindings: sources.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:24`; AST `48e15fe6e311c5175358ea7b09c683a20a2e650ca991f77628f547b0eb854d0a`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_inventory.py:25`; AST `d5e2fe4c95a6a8c7e51650467e8d9bccafaeb2631f585e1bb114b5b8aaa300e2`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: s, sources. Outputs/bindings: s.
Calls/effect boundaries: s['path'].lower, s['path'].lower().endswith.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[4].value::ListComp

Source: `infra/tests/test_roadmap_inventory.py:25`; AST `4dee95778751f0d48f2ca93a00bd2cfe31a57c3bf0a67cc6efcec37f8b99b1d0`.

Rust module: `infra::tests::test_roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: s, sources. Outputs/bindings: s.
Calls/effect boundaries: s['path'].lower, s['path'].lower().endswith.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[4].value.generators[0].ifs[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:25`; AST `6bbef3a2bc751acf3351d67f86e303650235efbd04a0b3133a50adcf57967607`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s. Outputs/bindings: (none).
Calls/effect boundaries: s['path'].lower, s['path'].lower().endswith.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[4].value.generators[0].ifs[0].func.value::Call

Source: `infra/tests/test_roadmap_inventory.py:25`; AST `2771ee17cb2a62a5786414eb85d6b6296d9f00b43243cf1c0d8c25d8f7b5acee`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: s. Outputs/bindings: (none).
Calls/effect boundaries: s['path'].lower.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.generators[0].ifs[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5]::For

Source: `infra/tests/test_roadmap_inventory.py:26`; AST `81de86f7e738d614f3f094957ea68d0033e70183b035a03302467fa2cfd55d73`.

Rust module: `infra::tests::test_roadmap_inventory`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, cls, path, shutil, source, sources. Outputs/bindings: path, source.
Calls/effect boundaries: path.parent.mkdir, shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted. Iteration: source in sources['files']
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:27`; AST `fdf48138a4753b80f713647aa54984e24be62257d251b23eaa2e266188a0dd09`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls, source. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:28`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:28`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:29`; AST `005c67252f14a79a9a38ddccc5cedd68a1185a13af6d668e6dbad7cf5c30a7c0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, path, shutil, source. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:29`; AST `739d8a578a26c58d4b349a868fe0e6722b78ae3af86bd3c9d3c2f2a23407b643`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, path, shutil, source. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:30`; AST `082469985bbc0d8be07b7e28a69097717cb6ac3a1e501754181fffd86a8a390e`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, cls, sources. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / 'Roadmaps/Shared/sources.json').write_bytes, canonical.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:30`; AST `1f9d1f539ed6ef8a50c4aa8197881ba72000727308d07d0b102859a1c2eebcbe`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, cls, sources. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / 'Roadmaps/Shared/sources.json').write_bytes, canonical.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:30`; AST `0743d071075568e47fb869751ca94d88a0f1f6e560c2803f97c713d5b1a0ced2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, sources. Outputs/bindings: (none).
Calls/effect boundaries: canonical.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:31`; AST `deb5099c177252e6b7c32d575ffbe8c03f133847af8742369be482591d637da7`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / '.gitignore').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:31`; AST `33f6c6bfccecf7dc9299b6bb1be6aee9c1f751450811f9761da5f62014f54df9`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / '.gitignore').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_inventory.py:32`; AST `25e56b279853f0fd9b926c1f6fa5484d833366656b85c3bd38f82447493df45b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / 'example.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_inventory.py:32`; AST `883311eacb6fc8fd4a4797ce18598b87ac95bd3239a8c169c0c218c771e74517`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: (cls.base / 'example.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_inventory.py:33`; AST `be4b3ff1e138605834e011f6c59dc50f7991e408a1f9fc8b9820357dc61673be`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_inventory.py:33`; AST `39d754fd9188573212c5e147b8e228746086680f2a46c978e7fc91f6e1e2f0bc`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[10]::Expr

Source: `infra/tests/test_roadmap_inventory.py:34`; AST `f1a03fa8aa832a02a079d98685d267dbe39ef3ab7728391327184fa6940c2a9e`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_inventory.py:34`; AST `1836db2a2e36d338747d9675c5b3cc9c1008d7234219ca6f3cbd13e641a97b77`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_inventory.py:35`; AST `ac2f5cdd0c087c5634cb8b962c1463c0b21095392f8d32c4070fe2540df0dfb7`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUpClass::root.body[12].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_inventory.py:35`; AST `3ffa6dd0d6c8c13e0877edd9f29758de6062de11fb334be260916b67e4d9b643`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::git::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:38`; AST `6213d1b9cdca8e3c2d924887815a001091297796bcbbd74f9d8eaccbee59529f`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: args, root, staticmethod, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::git::root.body[12].body[1].body[0]::Return

Source: `infra/tests/test_roadmap_inventory.py:39`; AST `1e304720b3540f6997b6d35083fa548c2095bd5c287aedefdf4e9bc4ecbb48f0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, root, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::git::root.body[12].body[1].body[0].value.value::Call

Source: `infra/tests/test_roadmap_inventory.py:39`; AST `ce49fa5319e2d12142ab62589998ff5a75dd7ca9e985dc249a3ea9658a1e53bd`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, root, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDownClass::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:44`; AST `057b3a016b8baed7ba704bb699f1490554b75b10e51aeae36eaf3dc77a78310f`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classmethod, cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.base_temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDownClass::root.body[12].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:45`; AST `b22f5a9c974da8cd11cef057594e60bf7155bbc0ecedcfbc4f0d63aa07fc0200`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.base_temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDownClass::root.body[12].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:45`; AST `161aeccd9a1a11fa340df6c65f2f4ee636feb3078655542074ce2644ce6a4315`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cls. Outputs/bindings: (none).
Calls/effect boundaries: cls.base_temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:47`; AST `1b090b19f68d708a9e66d97663dea2e19e83a2b4dd1a52ac6bb53c606d26cfe3`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, str, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.git, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:48`; AST `76bde1458ae912172e4121d6d32a40d02cf372c4db6ead9b5af171facc2865c2`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:48`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[1]::Assign

Source: `infra/tests/test_roadmap_inventory.py:49`; AST `4ba37218189bdf6064e63e96fa347f672e8aa2d6bf7fe4ff7e82d905261317c1`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[1].value.left::Call

Source: `infra/tests/test_roadmap_inventory.py:49`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:50`; AST `5d28bd0f8f0ca82019f41ade1ebf84929234e9f712159902b18ec091b6fc5220`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:50`; AST `0aabd793b7fb4370983c5fb44e5f0e13914c6a0ff1279d9357381fafcbd01ab2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:50`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[2].value.args[3]::Call

Source: `infra/tests/test_roadmap_inventory.py:50`; AST `9ec05a5b4d248f22dc8675f590543c5671aef3324ea6279e825b23c9980a3834`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::setUp::root.body[12].body[3].body[2].value.args[4]::Call

Source: `infra/tests/test_roadmap_inventory.py:50`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[2].value.args[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDown::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:52`; AST `13fc628cded8f8def9f296b061b0d1b4f129ada0770d009511b176b914c63004`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDown::root.body[12].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:53`; AST `03b3f025b568ce93e3252b0f1f4a5ce0348dbf2ecebaae9a0913927af51d7b24`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::tearDown::root.body[12].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:53`; AST `467d2c9d775dc88f51613c917ddb5ec5487d5c87293666d9c9c5f9a88375b66b`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.temp.cleanup.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:55`; AST `02f77e094da1040ff0a4659ebb1177953c7144f03ed9aefe59327385e72168f9`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, all, authority_inventory, c, components, len, r, reconcile_inventory, record, self. Outputs/bindings: c, components, r, record.
Calls/effect boundaries: (self.root / 'example.py').write_text, all, authority_inventory, len, reconcile_inventory, record['requirements'].pop, self.assertEqual, self.assertRaisesRegex, self.assertTrue, self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:56`; AST `2166e72926205400e0fbb1e636d335f7235bb336e750aeb7cb0a48bcf6d99c81`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:56`; AST `9fd21f3be5fcdafa23d6ba79bf10264b7fc2775b899161dd3f6f881afa50ef7f`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:57`; AST `46ceb3a0f8d4be7a0ea48dcaceae578e198caf273471b0353df0033289b23d52`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:57`; AST `87abb55e4c6fb42d5b0542965f763f515cf10e3dc2903d3beeb991e5cd80abff`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:58`; AST `c4d7c18faba0d184f3178dda4499a7bd8d8c7a0250dc4df1b72d30bca1f65e41`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:58`; AST `a77f359e992ba9a9b22949c7027b7954ae8e21b62330d41b764be1c3bb090f01`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:59`; AST `ab7218a031eccd2aefe9b34742200ac166d83b0156e720196d0d43855ef2ae3f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:59`; AST `e1b7e1a3cb0f611166a2978d9f60399552ced6e5e7399da41bfe87941110066e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:60`; AST `e64198654331a2a24a0a6551fbb51bb85795f4d5cd4532bfdaaa0b57a8d1fc13`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:60`; AST `236efa27453f38697d731d99a68e1082e2973f64668af884433b0e5ddc2c7e55`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[5]::Assign

Source: `infra/tests/test_roadmap_inventory.py:61`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:61`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:62`; AST `677726a11af72ade1d3224d5028561a853aa2a9d2666f216e9bc4d1ee0a2c89d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:62`; AST `c213182ca19c982e897b2875e929c71f070d2943e37863438372feab5087582c`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[6].value.args[1]::Call

Source: `infra/tests/test_roadmap_inventory.py:62`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[6].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:63`; AST `e3f39e28bbc1b24e39054dccbec971a4cb7dc10e25fa754ac2fd22644df15a2f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, record, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:63`; AST `a5eb044501ae7d7132fe2f7d2cbd0b7fe41083acb35fe99b1b4ff06fd8865df9`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r, record, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[7].value.args[0].comparators[0]::SetComp

Source: `infra/tests/test_roadmap_inventory.py:64`; AST `65778f61108d2afd1f0f0a108c92524639329482dcd542ef0be9a2524daefe1a`.

Rust module: `infra::tests::test_roadmap_inventory`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: r, record. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[5].body[7].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[8]::Assign

Source: `infra/tests/test_roadmap_inventory.py:65`; AST `5ade18151f65eb219020312edba3bd592ffeecc2563f4a54350e901f27d9ea98`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, record. Outputs/bindings: c, components.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[8].value::ListComp

Source: `infra/tests/test_roadmap_inventory.py:65`; AST `9604f58adef77ff7195a43db99417aafe41ce8884fb95978d4e33a990dd9d81c`.

Rust module: `infra::tests::test_roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: c, record. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[5].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[9]::Expr

Source: `infra/tests/test_roadmap_inventory.py:66`; AST `227eb081bb02403475262302308a8acff350a88ca7695faa4495e843b75ea8a6`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: components, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[9].value::Call

Source: `infra/tests/test_roadmap_inventory.py:66`; AST `c4a8c3419f199233b88f0c874ae86d58f39bd09bdfc25af8d8fcbb944de3a118`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: components, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[9].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:66`; AST `6fe60750d2c58edcb5164fbf387edc9f62045c5ed459ffe53ba715ccc5f9d288`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: components, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[10]::Expr

Source: `infra/tests/test_roadmap_inventory.py:67`; AST `9bd59cde786086a35a3fb9432386612103113930eafd493b617791d56d2d0111`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, components, self. Outputs/bindings: c.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[10].value::Call

Source: `infra/tests/test_roadmap_inventory.py:67`; AST `b772d5365f6f797d60e22d36291f03b43209625a12ad37e4377740c47384b7d2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, components, self. Outputs/bindings: c.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[10].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_inventory.py:67`; AST `c545fb525c88c1926ed62a001a2db68d1f694045d2671c3e922868d2385e004d`.

Rust module: `infra::tests::test_roadmap_inventory`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: c, components. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[5].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[11]::Expr

Source: `infra/tests/test_roadmap_inventory.py:69`; AST `6378e46df2d8d163001c4cb3ed7e39e350199cb6ad98dac80589e8dc0a21ac28`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, c, components, self. Outputs/bindings: c.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[11].value::Call

Source: `infra/tests/test_roadmap_inventory.py:69`; AST `d31776ba1d74117fc33f0eaa3292e6c88f7245533679e301e47473797aa5a224`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, components, self. Outputs/bindings: c.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[11].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:69`; AST `ffa551ffab5864d88a36159b31ccb09238a6eadc0cb99e9a50fefe86c6472114`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, components. Outputs/bindings: c.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[11].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_inventory.py:69`; AST `8c779efe5c6f276b3b8043c02033bf5b547ca0ccdc5efa3b76540fcae0b47722`.

Rust module: `infra::tests::test_roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, components. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[5].body[11].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[12]::Expr

Source: `infra/tests/test_roadmap_inventory.py:70`; AST `4a3b882bc1d97db6b9fd064e03a08660e4769bb7a34e8fcc478bbc7f9cadc8dc`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[12].value::Call

Source: `infra/tests/test_roadmap_inventory.py:70`; AST `ae1d73461ca1c8a57c54d0b9c826bcece0c99b6be04020d8a0c4ddcd5d58c2d2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[12].value.args[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:70`; AST `c706f91ec15b969fd78561b7c08bc2afc4f322b46e343a2ebcddc381303daa14`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[12].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[13]::Expr

Source: `infra/tests/test_roadmap_inventory.py:71`; AST `a51c94a9a7d1385f758765542f2e673f65c6c98c00bc82ba849e93703a1d1e2d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['requirements'].pop.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[13].value::Call

Source: `infra/tests/test_roadmap_inventory.py:71`; AST `de97e901147ec725124e5e479733ce3cb5124c1dfe9ae8016219662af467ef77`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: record['requirements'].pop.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[14]::With

Source: `infra/tests/test_roadmap_inventory.py:72`; AST `fd57c4649a52a47e9a95badf4b5744c535fa03fda7d45ecf74a9b53653119e45`.

Rust module: `infra::tests::test_roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[14].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_inventory.py:72`; AST `af79ea81888a102e5ab2213b4bb361c6ef69838d9e70bb9919cafaa99fb1895e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[14].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[14].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:73`; AST `dfccb520c35dbf53eb1c8a92751b77ce0c27eb01c1982700b751983691dbf4a8`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_every_branch_and_duplicate_blob_preserved_without_duplicate_inspection::root.body[12].body[5].body[14].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:73`; AST `c706f91ec15b969fd78561b7c08bc2afc4f322b46e343a2ebcddc381303daa14`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reconcile_inventory, record, self. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:75`; AST `5d97a8a0d9458620f9c8d6318f3f02865bbe9897ca76c0516fbce0253eb5dc73`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: authority_inventory, f, files, json, path, read_json, record, result, save_inventory, self. Outputs/bindings: f, files, path, record, result.
Calls/effect boundaries: (self.root / 'example.py').exists, (self.root / 'example.py').unlink, (self.root / 'user work.bin').read_bytes, (self.root / 'user work.bin').write_bytes, authority_inventory, json.dumps, path.parent.mkdir, path.write_text, read_json, save_inventory, self.assertEqual, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:76`; AST `c067e74eccea53697efada8b6578c82ebd5c18fde14e7a14d421a46d9ba6fec3`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').unlink.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:76`; AST `0ba261013226ae1a9938467a7be3589326d43b5aef67a0a00b1c1950548c73ab`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').unlink.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:77`; AST `91c1ffa48dcf640877b62dd18f5a484b7d5401467ecf98e0fd0eda451cf4d504`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'user work.bin').write_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:77`; AST `4372343fbb1ec6de6c08609db32cf4ff8ebdb0e353546908ffc0d1c020854fb5`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'user work.bin').write_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[2]::Assign

Source: `infra/tests/test_roadmap_inventory.py:78`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:78`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[3]::Assign

Source: `infra/tests/test_roadmap_inventory.py:79`; AST `313e12607eb36eee3e0d78dba629e3b4ca610c6b9257b7fa96aed342ae981e71`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, record. Outputs/bindings: f, files.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[3].value::DictComp

Source: `infra/tests/test_roadmap_inventory.py:79`; AST `971994b4cc63504990018aaf31ad9d2fde50fd3cefd7a64730bfc6b2eaae2862`.

Rust module: `infra::tests::test_roadmap_inventory`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: f, record. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[6].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:80`; AST `f964a321b0cc3a515b5b45a94249493c62d71c8f948bf282aba7c1bbabb95c6b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:80`; AST `124810aeffe0ef370e2da9d06d5c6f67604019634ce93a3e042f1f6d692a3ca5`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[5]::Expr

Source: `infra/tests/test_roadmap_inventory.py:81`; AST `323b3a0d5dca8cc7057269d19277bb6009511ffed1543c6b87dd8d15bccccfe3`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: files, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:81`; AST `9201a621a2b4807f207c372bb43e48d1ea45b8bf6e7648acb5796e3df329e626`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: files, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[6]::Assign

Source: `infra/tests/test_roadmap_inventory.py:82`; AST `21b2a0755d4d416aa5f58d075d8fb3eed7b04c9edfe92ef106097bf655d22490`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:83`; AST `25c20efa4fbad90a153f0e793ada673958816dd9017c0417b75539e96f3b141f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:83`; AST `f1c35542a1672ea2823dea77568dffcaed21b59391fecadcce39de4ba26f8b33`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[8]::Expr

Source: `infra/tests/test_roadmap_inventory.py:84`; AST `904dbb0cda25f62f22e8da77ed5b7141e41bc95e0b575032779cb0a9057061bf`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[8].value::Call

Source: `infra/tests/test_roadmap_inventory.py:84`; AST `2ede1eed868aeddee70daf4aeef2fc73ec38235d0f1b95d525d0b65e298ae5ee`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:84`; AST `6dbe030c1229e21b7347ada56d0328cb9827e3a3874f6f416add229cc504bfc7`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[9]::Assign

Source: `infra/tests/test_roadmap_inventory.py:85`; AST `a24efe82e6f0c3a6efa51dd4f34b2c77d6a2a2348adc87457aca77ab0df9c299`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, save_inventory, self. Outputs/bindings: result.
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[9].value::Call

Source: `infra/tests/test_roadmap_inventory.py:85`; AST `b77954f58d709d5ddfd8a50f60d4a787b8792dc37942b6d6c307f78cb4032f86`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[10]::Expr

Source: `infra/tests/test_roadmap_inventory.py:86`; AST `15c8bfc8aeb43890770d36a52c908187f439dc4b3114719ece91de6d093e4d6d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[10].value::Call

Source: `infra/tests/test_roadmap_inventory.py:86`; AST `a741a7a95d5ad3f0392835b71bbb2111b98106e486ad4eff37fd3b409171eaff`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[11]::Expr

Source: `infra/tests/test_roadmap_inventory.py:87`; AST `11f1c368d855de5d7f0e59a8d581b3d32d8b9e9b96bf6422cdae5650290215b5`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[11].value::Call

Source: `infra/tests/test_roadmap_inventory.py:87`; AST `61f49c9216cd5f9d2f7e962fdc390bf968805f3eb685d2587a429d1fad634740`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[11].value.args[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:87`; AST `ca2a99ec0b14545aba864c1e6b22415e5a02ad33955de7320b863aa9c805bfcd`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[11].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[12]::Expr

Source: `infra/tests/test_roadmap_inventory.py:88`; AST `2a2835a627d90b64b0906b5c63041b80e84df6d1c00d48c7352885f39aae7d0a`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[12].value::Call

Source: `infra/tests/test_roadmap_inventory.py:88`; AST `472d3816fd2eac76175f2e791b1a35d0b2fcec7d4aa8295ff6483bb71925264e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[12].value.args[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:88`; AST `b77954f58d709d5ddfd8a50f60d4a787b8792dc37942b6d6c307f78cb4032f86`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[12].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[13]::Expr

Source: `infra/tests/test_roadmap_inventory.py:89`; AST `b857ba8c78eaffda3663615556d897b93c19efcb3beb880e6f9f1bfe1687b850`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'user work.bin').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[13].value::Call

Source: `infra/tests/test_roadmap_inventory.py:89`; AST `1cd0997717b4cf360e2c8cf513b7d58bb01e335e0880e1bd5f41079d5caa29da`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'user work.bin').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[13].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:89`; AST `a4c935315e4c1b0b07ec44cd5d020fbab57d82b9551c0c4c97231a1d6b21ea8d`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'user work.bin').read_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[13].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[14]::Expr

Source: `infra/tests/test_roadmap_inventory.py:90`; AST `4e20f7e363ce860dd54ac5e65012ece24c358574815fab29a3665f2b323066b1`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[14].value::Call

Source: `infra/tests/test_roadmap_inventory.py:90`; AST `37bc4e427bbb1766acab9b3c91bdd03431730bf4c6f42a4e4d0a7721a0235b18`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_dirty_addition_deletion_and_binary_bytes_survive_recording::root.body[12].body[6].body[14].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:90`; AST `755d450ba32a935b6da08a72f7dc2d77cd3a32606f2050ae09c5e562a7e0c660`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'example.py').exists.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[14].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:92`; AST `f146f8af94c53fa41f3d7e7ed657916f64940e50784d442a17ad0bb868d46650`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, authority_inventory, path, record, save_inventory, self. Outputs/bindings: path, record.
Calls/effect boundaries: authority_inventory, path.write_text, save_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:93`; AST `88f657eb68b618a4ba0ff1aa13888daf155a6b941a4de3c49d5da320e2914901`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:94`; AST `f2c96a0d4869a35f684b2f5647c56af32ed48af1383e3ea497cf644a1634c02f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:94`; AST `cb167ed86645b6102dafd17f5fbcf114cbdfbfaec962d4a54dc00e723a55149c`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[2]::Assign

Source: `infra/tests/test_roadmap_inventory.py:95`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:95`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:96`; AST `d095b0e640c2245c2ee41c8d5348bec3a7ba7411e17ff8dbed678cebabae0236`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:96`; AST `ce6df1951cc09493c096b80ea60171c637e345dafa2c455748fde88768354193`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[4]::With

Source: `infra/tests/test_roadmap_inventory.py:97`; AST `fab1a1862be62113385b362cbf5be4d076f23620fada1f184a4807c4bde7d39e`.

Rust module: `infra::tests::test_roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_inventory.py:97`; AST `b0b897b4b8a3058f6d7fae3e301eb590042b08cb993db3579c7f8720c50679de`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:98`; AST `4941343051862855c4f9ea87daa5cdb02afe70c2842e9cd28875f51dff0209d1`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_content_edits_with_same_status_invalidate_publication::root.body[12].body[7].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:98`; AST `b77954f58d709d5ddfd8a50f60d4a787b8792dc37942b6d6c307f78cb4032f86`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:100`; AST `13a9bc14fd6c4cc817a6faf29a0ce7beba2e52ffca7924d04d2ff17d1a324b1a`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, authority_inventory, record, save_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory, save_inventory, self.assertRaisesRegex, self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:101`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:101`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:102`; AST `7da53676f5c1796c7566f9aa75ecf1a549bc11eb92f1a6fb3038c5525691d865`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:102`; AST `d91cf73ba869174e02dcacfa60fffe76b2250cce3d0a9390f5772fcf1238f503`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[2]::With

Source: `infra/tests/test_roadmap_inventory.py:103`; AST `fab1a1862be62113385b362cbf5be4d076f23620fada1f184a4807c4bde7d39e`.

Rust module: `infra::tests::test_roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_inventory.py:103`; AST `b0b897b4b8a3058f6d7fae3e301eb590042b08cb993db3579c7f8720c50679de`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:104`; AST `4941343051862855c4f9ea87daa5cdb02afe70c2842e9cd28875f51dff0209d1`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_new_ref_invalidates_snapshot_even_when_tree_is_identical::root.body[12].body[8].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:104`; AST `b77954f58d709d5ddfd8a50f60d4a787b8792dc37942b6d6c307f78cb4032f86`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:106`; AST `d1d37bf56875ca297922000dd9769c11873019105750dae724edd773024cb08b`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, authority_inventory, before, path, record, save_inventory, self. Outputs/bindings: before, path, record.
Calls/effect boundaries: authority_inventory, path.parent.mkdir, path.read_bytes, path.write_text, save_inventory, self.assertEqual, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:107`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:107`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[1]::Assign

Source: `infra/tests/test_roadmap_inventory.py:108`; AST `21b2a0755d4d416aa5f58d075d8fb3eed7b04c9edfe92ef106097bf655d22490`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:109`; AST `25c20efa4fbad90a153f0e793ada673958816dd9017c0417b75539e96f3b141f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:109`; AST `f1c35542a1672ea2823dea77568dffcaed21b59391fecadcce39de4ba26f8b33`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:110`; AST `2c374bafe95392f9d494e5e38f6f6b9b868b060fc26aa31f3c0243f2ff1ef35c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:110`; AST `148b3afcf1d2df6ec438c385160c0cd6b70299b1a03abd486ba4ad380596d675`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[4]::Assign

Source: `infra/tests/test_roadmap_inventory.py:111`; AST `7be2c3931aa069b4d490b975d00dcc6fda3e361647bf2bec6a22f528d37d0897`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: before.
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:111`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[5]::With

Source: `infra/tests/test_roadmap_inventory.py:112`; AST `d8cd921ee2f4d2f3370acd40f1d4ef5b048ce4aa7e3596e700ac4a1ae805904b`.

Rust module: `infra::tests::test_roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_inventory.py:112`; AST `f0b7b7ba5f892996d744c54ce66c4c5b4e1c34aa02425c560d75e89a52e9e793`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:113`; AST `4941343051862855c4f9ea87daa5cdb02afe70c2842e9cd28875f51dff0209d1`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:113`; AST `b77954f58d709d5ddfd8a50f60d4a787b8792dc37942b6d6c307f78cb4032f86`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:114`; AST `42c88e9cd5b261e9d53f8010a597ed26949ea0b52744950f44e3cfaf0b2133f9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[9].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:114`; AST `5ca0d971b1a61c0727bb77dd1b4a92521d9badb136b4d40681096ec1032a4ac5`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, path, self. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unknown_canonical_record_is_not_overwritten::root.body[12].body[9].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:114`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[9].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:116`; AST `1f289e0e7b6726d1659cb8369e227bd903bda90a14f920e1476c68d771bb2fd0`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, authority_inventory, destination, f, first, link, next, second, self. Outputs/bindings: destination, f, first, link, second.
Calls/effect boundaries: (self.root / 'link').symlink_to, Path, authority_inventory, destination.write_text, next, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:117`; AST `94d5d82123804442b05618066d92183e189dd932cd4c74c881c28746f776d48a`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: destination.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[0].value.left::Call

Source: `infra/tests/test_roadmap_inventory.py:117`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:118`; AST `30b33ef5dcd648435ec2c36a2b7efb243504de563845ce48b9dc236f368233c2`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:118`; AST `1c2653e175d626d623817c1b3d828c4f32d5857c911a7412748ca08cb920ee07`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:119`; AST `fa8ed0c8e5aa8716ab524094c53a745a5743f956a540c8df02adc3c4e02981e3`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'link').symlink_to.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:119`; AST `7c929ba7084e12ef9fa1495f374f97cf73c73cfa002663c3ad368c05902e95ac`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'link').symlink_to.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[3]::Assign

Source: `infra/tests/test_roadmap_inventory.py:120`; AST `c1ed0a69f5c1aed1e6854ceaa733760296c8a29d6af3eb40a2815ca9fc423d2d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: first.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:120`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:121`; AST `864166b3f635590530a51071937cd5134e25abb1664bee26ab04ad01a48c4409`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:121`; AST `da0861b49829c6d14b6c8c0f07e61dab7714789f88cb48eeabc88b1d38771cad`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[5]::Assign

Source: `infra/tests/test_roadmap_inventory.py:122`; AST `1c8e65fee786168c8a41fbdaaf5f6acfcb6f96a15c7d7856baaa0fd6c79b6fb9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: second.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:122`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:123`; AST `da9bd068ad06b387c70c98bc183249a7f1092bafbc9504da5101e82312a2c54b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:123`; AST `4547e07b5ae6faef9b2873386f89cd351cafde8543f8c60a119f98fbcba2a23e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[7]::Assign

Source: `infra/tests/test_roadmap_inventory.py:124`; AST `0476f6a6c6b0f896dd85d8d1324c34bbd1d74bf5bdd3c8196d61dc8022661f71`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, first, next. Outputs/bindings: f, link.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:124`; AST `5c3eb5def63931f9feaaca4eb628692d74f643909510c16887b5fcd48e4825d4`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, first, next. Outputs/bindings: f.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[7].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_inventory.py:124`; AST `bc296e1d3a4c026360bee51950fbcc14e3a9cdd5543c34532240831cb65912fb`.

Rust module: `infra::tests::test_roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: f, first. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[10].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[8]::Expr

Source: `infra/tests/test_roadmap_inventory.py:125`; AST `1342f1ce2d0b46a731e96a30087d4033ec0018be1a1902b49a356afa5cbecf85`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_reference_symlink_preserves_link_bytes_without_following_destination::root.body[12].body[10].body[8].value::Call

Source: `infra/tests/test_roadmap_inventory.py:125`; AST `7e12d76fe6b679e8d26e9dfe14b79d520e557e6896551e514fabb4ccb007b885`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[10].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:127`; AST `c6d75395ebff5860d8ac60cb5cb17ddaa7fecf4503752bf6f1d20eea3d40e98f`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: authority_inventory, c, component, next, record, self. Outputs/bindings: c, component, record.
Calls/effect boundaries: (self.root / 'old.py').write_bytes, authority_inventory, next, self.assertEqual, self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:128`; AST `6632ae5a7f16bb3f472d533451618aedf508d1be3fc526c6d3d88f9004cd0c85`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:128`; AST `48bebb59ec5459c35b303e9f4cae1c1e42698e84b69f27acf5fc66dd89da3646`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:129`; AST `0924fef5cbce9c112993a8a104a38f5e1334ce805a4d8451fbe07f27e308fc3d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'old.py').write_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:129`; AST `79c636e93f1811534fb5a9f16af1ea363e73d3f21a720d85350cafba6d4a7137`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'old.py').write_bytes.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:130`; AST `f124a8f49ed509b71169718577312ebd24a863f4a0dac396447943d196723355`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:130`; AST `8b3034d3b3b1ac1274ca50294f89b6a66ee77fc34fd3904e403353372cb5355b`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:131`; AST `a4d21e0a4c0369acbc42481be8d91decb8cc9c4bd99dc47d15591f89390de88a`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:131`; AST `c627cf6844fad04f7076fbe0f85525225a58ae747b8b6358acc0ba84d603ca98`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:132`; AST `e64198654331a2a24a0a6551fbb51bb85795f4d5cd4532bfdaaa0b57a8d1fc13`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:132`; AST `236efa27453f38697d731d99a68e1082e2973f64668af884433b0e5ddc2c7e55`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[5]::Assign

Source: `infra/tests/test_roadmap_inventory.py:133`; AST `c6e2f0e3aa1c03cb9843405e352c80a8b0b82c7cfcb716847f80d8227aee2a9c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:133`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[6]::Assign

Source: `infra/tests/test_roadmap_inventory.py:134`; AST `5246e31d9dc3cc43e33e28bd1caa6eab61a1dbec079cbca2f5174fa52fbd9538`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, next, record. Outputs/bindings: c, component.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[11].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:134`; AST `63d39738aeb43b06b59b3c8da1960d04eca60403a0ac8cde045f71a3a7dd958f`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, next, record. Outputs/bindings: c.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[6].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_inventory.py:134`; AST `f696d5d59baaab5bfec36692dc4038644871d9963803e8def98bfb661e98c336`.

Rust module: `infra::tests::test_roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, record. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[11].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:135`; AST `96db87382a836d1af85fc9a6c3bafa83e690f9f164c8e3e079f9c3e070f21234`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: component, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:135`; AST `f6d18b6e9aa94bfbe3310d5e9fd3ba16ec73584ab2e61cf1bd7469fb4f08fe24`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: component, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[8]::Expr

Source: `infra/tests/test_roadmap_inventory.py:136`; AST `6b0e7616c6a0725c90e13322e896218ce967a7826cca0309ea20ef1558ea177d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: component, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[11].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_unparseable_historical_source_remains_an_explicit_obligation::root.body[12].body[11].body[8].value::Call

Source: `infra/tests/test_roadmap_inventory.py:136`; AST `609f30daa8b6dea4fec5cf77f4d470eebf762758136916c705154f4e0e806624`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: component, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[11].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:138`; AST `6fefe4d6ed6f12ccb07c138b50334e309bee2a81b81845e88a7ce71496ec285d`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, Path, authority_inventory, f, first, link, nested, next, reference, save_inventory, second, self, staged_first, staged_second, str. Outputs/bindings: f, first, link, nested, reference, second, staged_first, staged_second.
Calls/effect boundaries: (nested / 'kept.py').write_text, (nested / 'user.py').write_text, (reference / 'kept.py').write_text, Path, authority_inventory, next, reference.mkdir, save_inventory, self.assertEqual, self.assertIsNone, self.assertNotEqual, self.assertRaisesRegex, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:139`; AST `81613c72003f6d278dc3975d592015a886db068a16215abd1db860678507b78d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: reference.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[0].value.left::Call

Source: `infra/tests/test_roadmap_inventory.py:139`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:140`; AST `1d0f1aa228eae7d56c6bd93ca269e7d2f63edebb4a446f98c4c5c12841cf0f99`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference. Outputs/bindings: (none).
Calls/effect boundaries: reference.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:140`; AST `d40c9c47b056d583dff4905094b55f83c05db0385142af583f47a0b2dad49863`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference. Outputs/bindings: (none).
Calls/effect boundaries: reference.mkdir.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:141`; AST `2b82a05366270dde0aa0112bfeaffceeecb9f688aa76d6f5c8f877975968af5b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:141`; AST `cb3a72e9c77209721612325c1104491ca740697f2cfa2298748bd1ea2b3303e2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:142`; AST `7c006ac2a257d1eb1d19da37328816233de70d03cf32f88744a7ce4acaf8fdd8`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference. Outputs/bindings: (none).
Calls/effect boundaries: (reference / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:142`; AST `b0b00753c0b4438ede74e606aff10f0f699252da4cb4fa312d31ad981fe48743`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference. Outputs/bindings: (none).
Calls/effect boundaries: (reference / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:143`; AST `1cda48740b255718fba6b6210bbd4cf0dae93bb5e8d6b9d61681b15c7115f8cb`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:143`; AST `8f8150048165d63db66835a52d5768df6e374def0fff445d68b001c9379c0c5e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[5]::Expr

Source: `infra/tests/test_roadmap_inventory.py:144`; AST `a94ce94c46a28c28cacb32f55901776f4be5c4add98a55600f500b21835844d9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:144`; AST `d7ee66663d92aabe1d5843e293e908990814f6e85c7cfcdd4b6656aa3f47b1de`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:145`; AST `7c23c741b16b0dee420d313bb43906875515bff5886ad95fab2a7ea66eac53ea`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reference, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:145`; AST `7a86fa4bc309b17e86627ae117953adf01e944bf7722bd3ea54576b35ede99d3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[6].value.args[5]::Call

Source: `infra/tests/test_roadmap_inventory.py:145`; AST `04d17bb12e3ee28096a351a9b6def7f5a8ef04d2672a4304e739a18f58e22c44`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reference, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[6].value.args[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:146`; AST `3514f6dafe9e23906c46b1e99b690525ac44df743530682b72091900e6fb8364`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:146`; AST `fc2117d317a33565fe3f33d990769c62ca3eba3ded09052eb879bcb73c4bc11b`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[8]::Assign

Source: `infra/tests/test_roadmap_inventory.py:147`; AST `ae0b029b41f0e6da6d0cf9534fb1355bd52a812881c8f0db2339854df3b177a3`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: nested.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[9]::Expr

Source: `infra/tests/test_roadmap_inventory.py:148`; AST `4022f2bfaf1d8f74544f2801f4737a5961f1750db17940ac737fa4a6f3bb77a0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[9].value::Call

Source: `infra/tests/test_roadmap_inventory.py:148`; AST `bc3288c55f0196dd1b4bf6cb14fad11c97cea0981b532273606d7cd5941b1b7f`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[10]::Expr

Source: `infra/tests/test_roadmap_inventory.py:149`; AST `8261206e978e79660bc96dcb4205e93f0f26ae90747025209264e6b6f5bb70c6`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'user.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[10].value::Call

Source: `infra/tests/test_roadmap_inventory.py:149`; AST `312a11474cf4c2dce79166f45f2fcac3f0661571785e936d793d03f692302492`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'user.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[11]::Assign

Source: `infra/tests/test_roadmap_inventory.py:150`; AST `c1ed0a69f5c1aed1e6854ceaa733760296c8a29d6af3eb40a2815ca9fc423d2d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: first.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[11].value::Call

Source: `infra/tests/test_roadmap_inventory.py:150`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[12]::Expr

Source: `infra/tests/test_roadmap_inventory.py:151`; AST `f9677fb457766e91634c0fe9ba21746750923324cfd1bbc924381493ad54dd45`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'user.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[12].value::Call

Source: `infra/tests/test_roadmap_inventory.py:151`; AST `cb83234b1b20267f25f144e05a20ebe99d1dbb6a12696a8df0fe6d1f5352f251`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'user.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[13]::Assign

Source: `infra/tests/test_roadmap_inventory.py:152`; AST `1c8e65fee786168c8a41fbdaaf5f6acfcb6f96a15c7d7856baaa0fd6c79b6fb9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: second.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[13].value::Call

Source: `infra/tests/test_roadmap_inventory.py:152`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[14]::Expr

Source: `infra/tests/test_roadmap_inventory.py:153`; AST `954d7d40bfbb3027c12b8072862e03c793d8eda27188f28336999f2b7e8d8b43`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[14].value::Call

Source: `infra/tests/test_roadmap_inventory.py:153`; AST `ad0e6ff76ff098510b46ff8d993218f1c4629175f372c1ee4ad884c1f9b19d75`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[15]::Expr

Source: `infra/tests/test_roadmap_inventory.py:154`; AST `1c546881432f47e9dbf7ed1be27c51b2205880238c14f859e49cef47952d62f6`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[15].value::Call

Source: `infra/tests/test_roadmap_inventory.py:154`; AST `be2564a27f1d8980c7c7a720c5c783534841fa684f2484593c38cd0b63c5547c`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[16]::Assign

Source: `infra/tests/test_roadmap_inventory.py:155`; AST `5add792e0bbaa40e809423365e6ae6225d2ca9b0ab92e026e078e1b153801839`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, next, second. Outputs/bindings: f, link.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[16].value::Call

Source: `infra/tests/test_roadmap_inventory.py:155`; AST `d65c0979204699986b87e53f08ff4efeda78f67b8cf80c9cacb8129050e4862d`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, next, second. Outputs/bindings: f.
Calls/effect boundaries: next.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[16].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_inventory.py:155`; AST `4af0112ab880d790911955bf74a226e48d381ca6f8ca6123722906caab4fc0a3`.

Rust module: `infra::tests::test_roadmap_inventory`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: f, second. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[12].body[16].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[17]::Expr

Source: `infra/tests/test_roadmap_inventory.py:156`; AST `df7b49b2a4a0d44cb0c2198f60c31af324758e97673849f9cc2278a8dc9dfee3`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[17].value::Call

Source: `infra/tests/test_roadmap_inventory.py:156`; AST `2471cd6c68740ff3bc7195b4e96da6ac92a03cb893c05a719ebc966694dfb1b8`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[17].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[18]::Expr

Source: `infra/tests/test_roadmap_inventory.py:157`; AST `6c1fe16727fb31da9414cb211b374815a5824a18b15f633b03f316dc9bb9db4b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, link, self. Outputs/bindings: f.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[18].value::Call

Source: `infra/tests/test_roadmap_inventory.py:157`; AST `0e6ecf6c2251306d0b55867e4ae3321016fd56d2fdc79eb61a124ed3a0ad2b07`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, link, self. Outputs/bindings: f.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[18].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_inventory.py:157`; AST `916e2ab65b9d8dadd8ad6b9f7dea835253cc91f4d6df3c977ce62182f1ed5385`.

Rust module: `infra::tests::test_roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: f, link. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[12].body[18].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[19]::With

Source: `infra/tests/test_roadmap_inventory.py:158`; AST `592eba9cdfb006a963ff621d64e7f18a281ee9285a74ff06554cce70a2e5b59f`.

Rust module: `infra::tests::test_roadmap_inventory`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, first, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[12].body[12].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[19].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_inventory.py:158`; AST `b0b897b4b8a3058f6d7fae3e301eb590042b08cb993db3579c7f8720c50679de`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[19].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[19].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:159`; AST `63c0b64dea7d8fdb906f0fa5123e97516a95de0cf38b741b2daca05400a7fc41`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[19].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:159`; AST `7b935f6477967311277e033c28647ac507a92d443634d7df5ad56e54b02b899f`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, save_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[20]::Expr

Source: `infra/tests/test_roadmap_inventory.py:160`; AST `11e33492ed82200c40a8a91b5b202caf0031b7e924ddbe0e6db8992bbbfd167e`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[20].value::Call

Source: `infra/tests/test_roadmap_inventory.py:160`; AST `e6e2687c23dcab8c366312a24c46d25bd080f779ca39ecf2817434b4d5792a2c`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[21]::Expr

Source: `infra/tests/test_roadmap_inventory.py:161`; AST `30899cf36f635ca7e7de776f26f7a72a329b333301eed7e1bee3f1cfe5d834d9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[21].value::Call

Source: `infra/tests/test_roadmap_inventory.py:161`; AST `f82a69b059f8cabb691f9841d03c708f322561d7c602fc3ab5c12d53e0faf760`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[22]::Expr

Source: `infra/tests/test_roadmap_inventory.py:162`; AST `cc948e177135827d4f6dd687c308d80deb464cd7fd6401b43ba62e203d122e90`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[22].value::Call

Source: `infra/tests/test_roadmap_inventory.py:162`; AST `558d3f688f244d7a692d812954d53f3e66eaf8017a8f9c47a351fa369d171b29`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[23]::Assign

Source: `infra/tests/test_roadmap_inventory.py:163`; AST `dcae1e38f24cf860a34265b7ca6169a211e2a4e29c47c06d8743741d63e25593`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: staged_first.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[23].value::Call

Source: `infra/tests/test_roadmap_inventory.py:163`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[24]::Expr

Source: `infra/tests/test_roadmap_inventory.py:164`; AST `33faa06bf47856f374925357c09415c7500e22804bd81bc710f4c194a9f6cf2d`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[24].value::Call

Source: `infra/tests/test_roadmap_inventory.py:164`; AST `1bfae75b240750daa9cbf51855cff57c5a5a64471c4045ab3c9512a138b4b2c2`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[25]::Expr

Source: `infra/tests/test_roadmap_inventory.py:165`; AST `30899cf36f635ca7e7de776f26f7a72a329b333301eed7e1bee3f1cfe5d834d9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[25].value::Call

Source: `infra/tests/test_roadmap_inventory.py:165`; AST `f82a69b059f8cabb691f9841d03c708f322561d7c602fc3ab5c12d53e0faf760`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[25].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[26]::Expr

Source: `infra/tests/test_roadmap_inventory.py:166`; AST `cc948e177135827d4f6dd687c308d80deb464cd7fd6401b43ba62e203d122e90`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[26].value::Call

Source: `infra/tests/test_roadmap_inventory.py:166`; AST `558d3f688f244d7a692d812954d53f3e66eaf8017a8f9c47a351fa369d171b29`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nested. Outputs/bindings: (none).
Calls/effect boundaries: (nested / 'kept.py').write_text.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[27]::Assign

Source: `infra/tests/test_roadmap_inventory.py:167`; AST `859d943384f570257155be1a6f12926719ce1bbbcad5bc1f110f55e9898cc62b`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: staged_second.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[12].body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[27].value::Call

Source: `infra/tests/test_roadmap_inventory.py:167`; AST `bf626373d22cd4d89803f0d5b697488acc62b305619fe06d9905067a46152836`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[27].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[28]::Expr

Source: `infra/tests/test_roadmap_inventory.py:168`; AST `b9a162ac85c88c00050b886da0a3adec90ae3903dfe53eac15c70a8a3355fa65`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, staged_first, staged_second. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[28]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[28].value::Call

Source: `infra/tests/test_roadmap_inventory.py:168`; AST `dc5b4d66c6e6ec6d74ea73733f8f934a177a818ebb1d833079585825aacacbdc`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, staged_first, staged_second. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[29]::Expr

Source: `infra/tests/test_roadmap_inventory.py:169`; AST `243d466e194ce945136aa49e159a54f9c7d35b4c3dcd36c2e708b52cae216d18`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, staged_first, staged_second. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[12].body[29]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_gitlink_untracked_content_changes_invalidate_inventory::root.body[12].body[12].body[29].value::Call

Source: `infra/tests/test_roadmap_inventory.py:169`; AST `1660c815ee71dcce15641fe2372c0f25283cdabf3867c34a1de1354e8fee9890`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, staged_first, staged_second. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[12].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:171`; AST `5e656a0632323955510faf0bc397b0f1019bde1e1f96203c51be205732b2dd87`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, authority_inventory, h, record, remote, self, str. Outputs/bindings: h, record, remote.
Calls/effect boundaries: Path, authority_inventory, self.assertEqual, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:172`; AST `5c724d871d7ccd6bd06263e0550e9c9480bf80e70651a706aabf14f0a33c2f75`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: remote.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[0].value.left::Call

Source: `infra/tests/test_roadmap_inventory.py:172`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[1]::Expr

Source: `infra/tests/test_roadmap_inventory.py:173`; AST `54185ccb4f76552c4f09a28c3d8aa742281a68dc299f31affd37ba88addb0f18`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, remote, self, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:173`; AST `1d723cfcfafc6108102977d03bcafd8785f4039e90090a0b0be5ba3e2e7c8ba7`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, remote, self, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:173`; AST `e86048b48fb089033b58411cb826119b13eb421e1eeb13103d6c16148810abd3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[1].value.args[3]::Call

Source: `infra/tests/test_roadmap_inventory.py:173`; AST `a36854e96c7049be44a6940ffbb614829a0114cdd227a679af357813d1aba7e8`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remote, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[1].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[2]::Expr

Source: `infra/tests/test_roadmap_inventory.py:174`; AST `ac9cf722ffe71c419ac878827665aaf89cd6887d7fc3a31af8092a1009018e78`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remote, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[2].value::Call

Source: `infra/tests/test_roadmap_inventory.py:174`; AST `9a531675fdfc64e91fc6e01d1e3c2c28c907239feb34b3a5b74e425876f1bc5e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remote, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.git, str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[2].value.args[4]::Call

Source: `infra/tests/test_roadmap_inventory.py:174`; AST `a36854e96c7049be44a6940ffbb614829a0114cdd227a679af357813d1aba7e8`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remote, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[2].value.args[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:175`; AST `dc40cd79178afded425b090175f150830622d09ef060987dc73d6023cec2b4b4`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:175`; AST `4c2c1bd0e2a276946989bdacba7d116e19f8e073a53b250715e3eae4c71be689`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[4]::Expr

Source: `infra/tests/test_roadmap_inventory.py:176`; AST `c62119959c012c27f596d63633ff885eee0aa123087611554a1b5af86af23e1a`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remote, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[4].value::Call

Source: `infra/tests/test_roadmap_inventory.py:176`; AST `677906183ab549576e4be750897311d09fd970ad55fce353f593f8cf82fe3de3`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remote, self. Outputs/bindings: (none).
Calls/effect boundaries: self.git.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[5]::Assign

Source: `infra/tests/test_roadmap_inventory.py:177`; AST `d72667bcfaac2272ad28aa5b87c3b85638fd610fcffb6cbe3e549020eeb385ce`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authority_inventory, self. Outputs/bindings: record.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:177`; AST `7d03f6af624b2044ebf61b1e2da84cf0d4aefb0522d61ed3a495aca26af2f8ab`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authority_inventory, self. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:178`; AST `376caed10829d9804b4fe9e625d10e73d5fb4fe23f2003041345f0dbe9996a3c`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: h, record, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:178`; AST `734db5760f2dd9f29a73e2813559a72cdb9ed3e0e98c17b1f96994cf614e3790`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: h, record, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[6].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_inventory.py:178`; AST `d0df7fd9f56e43c606d2aea76cd15c51439c5a85fddabff3b3b4c68477e4ebbc`.

Rust module: `infra::tests::test_roadmap_inventory`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: h, record. Outputs/bindings: h.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[12].body[13].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:180`; AST `bbbba2f79d4a2dd52b309a766f0cd56270019b65a80ef251b182d2ca107ca6ff`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: h, record, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:180`; AST `e6244d863288f0034394695a5df0ecce099f797bef7c10f73af08f3547d18a33`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: h, record, self. Outputs/bindings: h.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_remote_heads_are_live_and_unfetched_work_is_visible::root.body[12].body[13].body[7].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_inventory.py:180`; AST `15d1d1ddd38406cb7c313380c9cb3aa18972a9e43afe27a3fdad427e4523b14a`.

Rust module: `infra::tests::test_roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: h, record. Outputs/bindings: h.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[13].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14]::FunctionDef

Source: `infra/tests/test_roadmap_inventory.py:182`; AST `5257affbf8ef3112833d1d8809b9204449be49f7f86fd87d68c3053d736f9635`.

Rust module: `infra::tests::test_roadmap_inventory`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: d, definitions, inspect_python, len, raw, result, same, self. Outputs/bindings: d, definitions, raw, result, same.
Calls/effect boundaries: inspect_python, len, self.assertEqual, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[0]::Assign

Source: `infra/tests/test_roadmap_inventory.py:183`; AST `d5095514ab20f83f78992c2c0c53c3096aa355920d347db47a493f4a61bb5d48`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: raw.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[1]::Assign

Source: `infra/tests/test_roadmap_inventory.py:184`; AST `1cd162cff7c7f225127aa8b2251ef097e45e183e2101c7c4a504160d5f0c6c87`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: inspect_python, raw. Outputs/bindings: result.
Calls/effect boundaries: inspect_python.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[1].value::Call

Source: `infra/tests/test_roadmap_inventory.py:184`; AST `aa93d73be0c8d8b815c62c8e50fe7d8b4805a64391e07be6fd4855fa762d4a4d`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: inspect_python, raw. Outputs/bindings: (none).
Calls/effect boundaries: inspect_python.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[2]::Assign

Source: `infra/tests/test_roadmap_inventory.py:185`; AST `5ef7e3a24f1d63fa595f0b572d61628c742202b29df863d149d8e7a049ee61b0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: definitions.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[3]::Expr

Source: `infra/tests/test_roadmap_inventory.py:186`; AST `8a026921fe5ecc1ffd8629c1973cc9c007b4eb5479ba1a3beb683726d689c40a`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: definitions, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[3].value::Call

Source: `infra/tests/test_roadmap_inventory.py:186`; AST `e324614a2946c752a2c8468635474abc6404e3a06e0a268b068ed53bdcc071ea`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: definitions, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:186`; AST `9a985714e8d31ffb294406c660192ce0ce1472b7173d4e7755f89d3c31b1a9f6`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: definitions, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[4]::Assign

Source: `infra/tests/test_roadmap_inventory.py:187`; AST `0d756fcbd5f14816489893a0d1e657e4ec73151f2e77dffa323b36e76a0f49cd`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: d, definitions. Outputs/bindings: d, same.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[4].value::ListComp

Source: `infra/tests/test_roadmap_inventory.py:187`; AST `1b4e15b006fbe5418d6b2a073da1b71550112c01ae4efd6b977a0d90b59c23ee`.

Rust module: `infra::tests::test_roadmap_inventory`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: d, definitions. Outputs/bindings: d.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[5]::Expr

Source: `infra/tests/test_roadmap_inventory.py:188`; AST `503426c3afce4833fd92eb7d02f767c9e651c755a31ed520689d55d327cb966f`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, same, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[5].value::Call

Source: `infra/tests/test_roadmap_inventory.py:188`; AST `995300584b864b1e10ac4f45a00d5ae946da3ee93b24c67aa533421f65eee283`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, same, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_inventory.py:188`; AST `e747ac7e29faa3c7aebebae6f57de21e463fd8a32ed1d3671d1f101be78ca04b`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, same. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[6]::Expr

Source: `infra/tests/test_roadmap_inventory.py:189`; AST `b6e3921c46388ea52e5fa93c751855cdf2b77c289b1daf6942f2d1872eb9c0b0`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: same, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[6].value::Call

Source: `infra/tests/test_roadmap_inventory.py:189`; AST `06e44701167755d9a1d0e88e2f5f7ce74b6bfba07dcc9aceda115f8a8c309a4e`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: same, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[7]::Expr

Source: `infra/tests/test_roadmap_inventory.py:190`; AST `9e6f8b79bf4b4ff29ad50033606030147b89c9ced9e2025194d19bbaf50298c9`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: same, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::AuthorityInventoryTests::test_nested_and_shadowed_definitions_have_distinct_body_identities::root.body[12].body[14].body[7].value::Call

Source: `infra/tests/test_roadmap_inventory.py:190`; AST `12950c5eda988982d2618de1d17639a8c925941f692d5235eb2fca70e4919e0f`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: same, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[12].body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[13]::If

Source: `infra/tests/test_roadmap_inventory.py:193`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_inventory`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_inventory.py:194`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_inventory`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_inventory.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_inventory.py:194`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_inventory`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_inventory, agentinfra.roadmap_records, json, pathlib, shutil, subprocess, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
