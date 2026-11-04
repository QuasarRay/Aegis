# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 190. Inventory digest: `f4216c779135c7bc95c4126ea5b72f8a29829707b30c22e37996b1172cf99e3d`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python_esbmc.py::module::root::Module

Source: `infra/tests/test_roadmap_python_esbmc.py:1`; AST `563ce01be615f087f2632828f678187e9713c41d9f57d45ce642cb84777472fb`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, SPEC, SUPPORT, __file__, all, archive, argv, classify_esbmc, consumed, content, dict, entries, entry, esbmc_arguments, esbmc_link_state, fixture, importlib, json, later, link, marker, mirror_support, mode, name, negative, retry_limits, run, self, set, stat, str, tempfile, tool, unittest, update, x, zipfile. Outputs/bindings: ROOT, SPEC, SUPPORT, archive, argv, consumed, content, entries, entry, fixture, later, link, marker, mode, name, negative, run, tool, update, x.
Calls/effect boundaries: (fixture.root / 'pin.json').write_text, (self.destination / 'aegis-release-identity.json').read_text, (self.destination / 'pkg/bin/esbmc').read_bytes, (self.destination / 'pkg/bin/esbmc').stat, Path, Path(__file__).resolve, SPEC.loader.exec_module, SUPPORT.extract_release, all, archive.writestr, argv.index, classify_esbmc, dict, esbmc_arguments, esbmc_link_state, fixture.bind, fixture.setUp, fixture.state, importlib.util.module_from_spec, importlib.util.spec_from_file_location, json.loads, link.symlink_to, link.unlink, mirror_support.RetryScopeTests, negative.index, retry_limits, self.addCleanup, self.archive_entries, self.assertEqual, self.assertFalse, self.assertIn, self.assertNotEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.destination.exists, self.destination.with_name, self.destination.with_name('release.staging').exists, self.subTest, set, str, tempfile.TemporaryDirectory, zipfile.ZipFile, zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:1`; AST `6d23f8b9f13a417227a9a348cc653cb751cf1d5b27aeb8c1b211193db0fc90b6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_esbmc.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:4`; AST `866a97c0a29d398dc2bf8a74409548dccd9bb5221f4bf0f58ad1a37ef83e5260`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_roadmap_python_esbmc.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:7`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[8]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:10`; AST `4123c8e546e07497699149dda363dc8539207c3974a8a7d70400f73212c30178`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_python_esbmc.py:12`; AST `be90747db7cd55e5cb043e9a153e2624c317c9eff08138e6b64ef65865daaec0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_python_esbmc.py:13`; AST `f03d490df75c7330951b5ce75380b297979b688b88c1f26364ab52e4c8a2c0af`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_python_esbmc.py:14`; AST `18c1b1c6aadc865085e026ffcf29ae444829cf09b6d0fe5d6efd294e6571ed28`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[12]::Import

Source: `infra/tests/test_roadmap_python_esbmc.py:15`; AST `36e094ecb2ba48db55b3ecc5a98be436670268bd7b8ab9111b5a1f8f0d9f8304`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[13]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:18`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[13].value.value.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:18`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[13].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[13].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:18`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[13].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[14]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:19`; AST `6e3a7ea09b184e96bb093ae38c890893bf86ba1a8c0c44c4ad1f58be8d54a2db`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, importlib. Outputs/bindings: SPEC.
Calls/effect boundaries: importlib.util.spec_from_file_location.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[14].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:19`; AST `7ae454fc779a62f973049fb23a7275da189a0370471782d09d9e50b48c1a0c3a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, importlib. Outputs/bindings: (none).
Calls/effect boundaries: importlib.util.spec_from_file_location.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[15]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:20`; AST `8aee733e7cee1355eda0da35cda7154dd63fba9f7a0d043c43b8a53639060151`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SPEC, importlib. Outputs/bindings: SUPPORT.
Calls/effect boundaries: importlib.util.module_from_spec.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[15].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:20`; AST `2a7fa4e533fcfa927b274eaaab69bf15b8c33bc8e2245b81970345e5757f7f38`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SPEC, importlib. Outputs/bindings: (none).
Calls/effect boundaries: importlib.util.module_from_spec.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[16]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:21`; AST `7ca69c28bb419562a6473d91b1663f7c9e22db8c3d0225f825e21b38da0bea22`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SPEC, SUPPORT. Outputs/bindings: (none).
Calls/effect boundaries: SPEC.loader.exec_module.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::root.body[16].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:21`; AST `2fae639b60aefb85c8d4374612e9e254cd30a5a1b1c1a8709a4a8ff55fb9cdd3`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SPEC, SUPPORT. Outputs/bindings: (none).
Calls/effect boundaries: SPEC.loader.exec_module.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[16].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::root.body[17]::ClassDef

Source: `infra/tests/test_roadmap_python_esbmc.py:24`; AST `8c6af131d0d4414897c8a560a617b407f3dbe98a3b43acb75c69785dbf935292`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, ROOT, argv, classify_esbmc, consumed, dict, esbmc_arguments, fixture, later, mirror_support, negative, retry_limits, run, self, set, str, tool, unittest, update. Outputs/bindings: argv, consumed, fixture, later, negative, run, tool, update.
Calls/effect boundaries: (fixture.root / 'pin.json').write_text, argv.index, classify_esbmc, dict, esbmc_arguments, fixture.bind, fixture.setUp, fixture.state, mirror_support.RetryScopeTests, negative.index, retry_limits, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaises, self.assertRaisesRegex, set, str.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:25`; AST `fcc84640a11df0fd1c68bfa4ac705ff6e5c1ab5bc4e48c48f2371950ad5ee8d9`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, ROOT, argv, esbmc_arguments, fixture, negative, self, set, str, tool. Outputs/bindings: argv, fixture, negative, tool.
Calls/effect boundaries: argv.index, esbmc_arguments, negative.index, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaises, set, str.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:26`; AST `8522612c38c367440c51d10e675f4c659fb11ec84e595ce5c6e2ef0f272c2338`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: tool.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:27`; AST `6e284938a2d67c2a8e70dbed2d726192ec7775caca42c7d92a20ac5be1a20b49`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: fixture.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:28`; AST `628fae1dbeba3180f55c13ad937603b6463d0ed32b80c1e7692cbb486e08ca82`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, esbmc_arguments, fixture, tool. Outputs/bindings: argv.
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:28`; AST `7a4b5f52773e2ded4f3ef765e535df6c35335fc819eed4d06566433a7f5fdb01`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, esbmc_arguments, fixture, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:29`; AST `22ed6a808e00111cf061893ad82a749c533695591ba9a4835310883899281fdd`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, argv, fixture, self, str, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, str.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:29`; AST `e038813656d1734bdb9901639c55007e84e3d3ccc2012344cb621c355fc13e23`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, argv, fixture, self, str, tool. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, str.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[3].value.args[1].elts[1]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:29`; AST `4636f9824dd8a3a9daa97dcc922e6441f1e2b34f5e4bd1d38618588c29f4c5a4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, fixture, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[3].value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:30`; AST `712c482452947ab0055e1b4fb3362626b3012be7abd1471210f307011838f454`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:30`; AST `c23d8ee00ac50ac19f818938e573a2f3bbcfc36c849401ab48cc1e67a9363815`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[4].value.args[0].slice.left::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:30`; AST `2ccc7862dfb743d3f3d90dcf5cd24e324afe8940580f6f58c5dd4ef3f055f571`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.index.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[4].value.args[0].slice.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:31`; AST `bce004dd6d0a6a84a23a69f98bd087715617c63d08f2726cae5f127eb288264d`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:31`; AST `293e57f79ac384460df65f33035476ffb52162625729961ea74b9629982bb20b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: argv.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[5].value.args[0].slice.left::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:31`; AST `bbb372e1ff285d8de1aef8b76c4fbb2f9f90450be3b63e4a071e4745a84aa206`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv. Outputs/bindings: (none).
Calls/effect boundaries: argv.index.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[5].value.args[0].slice.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:32`; AST `575ac388a1cb7b583329cd21f8a701422cfc6a551e540a310c52f14dda474a55`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:32`; AST `199e5706f7a633095ea8389f9c7d5a3fc2e3d1a2586f8e2a64c32fd32c9f8e7e`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:33`; AST `a06d75e5f816a0302816ae36b4f900fd21242576faea0db4dd9d3ecdd88a415e`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:33`; AST `a2032ada676000458e534ffa7ca726fab51287823a902ddab1fca9b366ad9c1e`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:34`; AST `f5ea582d1a24a12712bf2b985113b2f47bcd8cf5456b5ea5772096f1bba28225`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, set.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:34`; AST `bf08232855bee94e855272542782175f03abe0749d1966e21934429510d4fb7b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, self, set. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, set.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[8].value.args[0].left::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:34`; AST `3b95ba1f138a5ed62ad11f905e9f213c39ce2e958091598ac53e65aaa57bae4f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[8].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[9]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:35`; AST `0243a14697e90433ffa8749c892c20ba241a4c7a9d8eece82105d4e23ae146ea`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, esbmc_arguments, tool. Outputs/bindings: negative.
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:35`; AST `7d1a218c30de1e29803cc5752a5f4b3b5cbeecb9c4b8aa5df7936374e1606f59`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, esbmc_arguments, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[10]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:36`; AST `10e4ad357a2dfb72aff33a8a7eaf63fe291c7535cd77a8542c6161ad29fb7866`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: negative, self. Outputs/bindings: (none).
Calls/effect boundaries: negative.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:36`; AST `c7fa9bea6a50a4a11ba3c67635436ebdbeece89edf140e18bf3b8dc3dc1ec8d0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: negative, self. Outputs/bindings: (none).
Calls/effect boundaries: negative.index, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[10].value.args[0].slice.left::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:36`; AST `93d6d4a51d253deaae0e828d8c1f67df1de51d9198d75c3833109442b9e3a202`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: negative. Outputs/bindings: (none).
Calls/effect boundaries: negative.index.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[10].value.args[0].slice.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:37`; AST `6b2b159a753e91203ad7676eeae3a6d5ba70601341f7ac9d1b9a304a66efb79f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, esbmc_arguments, fixture, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:37`; AST `ba1e02efb2d06600627382921fb4f4b9a0d31aaba8118e58511aa1c242052164`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, esbmc_arguments, fixture, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[11].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:37`; AST `763d44b3263d6bfd129db338f4747fd848194de555754f898da2f3753d52a02c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, esbmc_arguments, fixture, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[11].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[12]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:38`; AST `12031c0a9885fa62c1fad10b6181b756f359fe8e0d6bb88e59b4cc254425e08a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, ROOT, esbmc_arguments, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[17].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[12].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:38`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[12].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[12].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:39`; AST `41134d4460284a422e8205e567a4ec2fb620f8d275464a9955befcf64a172624`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, esbmc_arguments, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_fixed_command_selects_original_function_and_keeps_assertion_and_domain_checks::root.body[17].body[0].body[12].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:39`; AST `8ebf2492779f166b9f587763d2d7be62ac564a3d50efea4ce032227101b6698a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, esbmc_arguments, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:41`; AST `fa4953270f0c9256e2ac8bbcd82bbda388d1a9e076ed207f7eaa4b181396a3dc`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_esbmc, dict, run, self. Outputs/bindings: run.
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:42`; AST `27f10d36a31f3571cdc6493be3f75b9a39c63a138d1a98ebba774dc95d1c05e4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: run.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[1]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:43`; AST `f43491b37d6573a0562b5b14702cfcb1397f757fa7b32b42dcd0ce38856566d0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_esbmc, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:43`; AST `4ec6d5b08f34c21f2bcfd9386455f1cced9b04c640827653b84f8b1d8e8bd72e`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:43`; AST `1a6ae20283f90582c33920503561f83c10f1b037c290cbe3edcd8b82ddd3ecc0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:44`; AST `06a8b8b8bf4ac8ea47df0b09de608c04ad03e085b6206e73ea784f5ff377d028`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_esbmc, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:44`; AST `7bc113bb988034effdfa3d617a1ee3247d9f3bccca6699175bf0e95b11c18b01`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[2].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:44`; AST `b14f023a778732e8079623188644dc04bae6898b363bf708d6f8ada668adec08`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[2].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:44`; AST `fac3a8a1ac54ec887e997964a54f72b3958b67a18c8c3ba1ada21a478b8d4e16`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, run. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[3]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:45`; AST `bfd59a3be6a2829a6146dfb000c041dbf5dd97f1a0361e0cb3aa02436aae55c8`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_esbmc, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:45`; AST `4c329f48e1099c9e53be14003bb8397a46e6f597f87459fbf1423be9b08d3910`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[3].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:45`; AST `b16e642e3718c53a28093ce6cc65e83c0315189cc5a73cc945889f5804969a81`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_cli_success_without_property_model_review_cannot_become_proof::root.body[17].body[1].body[3].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:45`; AST `95adeb63036880bebb459d57a42fe6838b0716f908bc03ca2872850e6bf95124`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, run. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[3].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:47`; AST `5bbd208a577faf390746b708341d92de36fd7389c6b69815b44b75a95b3a7c43`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_esbmc, dict, run, self, update. Outputs/bindings: run, update.
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:48`; AST `30ea44de98bbdd6793b69bf6c3b300d814dc7af924b70e8dd2e60b095a75e5d2`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: run.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:49`; AST `b190d545af3e9a237feafbe78aeec81f4100ec0cdd852039dd1d40e8b2491472`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_esbmc, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:49`; AST `33e810d6fd70912cb6952aa56994ebc5f6ed27eef1a0fd8321ea8861f842e15a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:49`; AST `1a6ae20283f90582c33920503561f83c10f1b037c290cbe3edcd8b82ddd3ecc0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[2]::For

Source: `infra/tests/test_roadmap_python_esbmc.py:50`; AST `273173ba7387173207949791d79f471588a369ce08e88b8527e7870ce2105ab8`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: classify_esbmc, dict, run, self, update. Outputs/bindings: update.
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered For evaluation at root.body[17].body[2].body[2]; no call, error or mutation may be omitted. Iteration: update in ({'timed_out': True}, {'stdout_truncated': True}, {'stderr_truncated': True}, {'stdout': 'Timed out'})
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:51`; AST `e8580682293223221ae6d6757b1c733e5a92e128353aec089f459d23e052a2f3`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_esbmc, dict, run, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:51`; AST `1e76b95e3eb113fb691cab7551446f55cf0382188b50e21ba7eb8b8c24d68dcb`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run, self, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[2].body[0].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:51`; AST `639ebd16c4a7262cbacf716d4f62ffeb78d7173a887ca17c4bea7aee6696691e`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_esbmc, dict, run, update. Outputs/bindings: (none).
Calls/effect boundaries: classify_esbmc, dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_negative_verdict_timeout_and_truncation_cannot_claim_original_assertion_detection::root.body[17].body[2].body[2].body[0].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:51`; AST `4cf079f46defaf2346170231a6669ae3256d0e70b3f9663c656e9334983e8c8d`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, run, update. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[2].body[0].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:53`; AST `2ab7479f64a8cc5a5cfcd4d26a6ce50145961c14d767c099c818161ae4809ff6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, consumed, dict, fixture, later, mirror_support, retry_limits, self. Outputs/bindings: consumed, fixture, later.
Calls/effect boundaries: (fixture.root / 'pin.json').write_text, dict, fixture.bind, fixture.setUp, fixture.state, mirror_support.RetryScopeTests, retry_limits, self.addCleanup, self.assertEqual, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:54`; AST `4aee2c4d3ff1ed2c37df62e17aeedbf368fe92c47ba658e65eb889cb442f35fc`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirror_support. Outputs/bindings: fixture.
Calls/effect boundaries: mirror_support.RetryScopeTests.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:54`; AST `bda9b07c51bc032fc8f34e063fa32c9a6744104bfcf98a296cf5d4bbcf838c8c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirror_support. Outputs/bindings: (none).
Calls/effect boundaries: mirror_support.RetryScopeTests.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:55`; AST `c23f518b24b63e1c7ea771e6b3bbae2c0086e30f1725e66f0dd8208a4e09df7b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:55`; AST `432b5a84ee42d25a6727758a1d460cb34803d67d35c84891d1143720d6fbe26f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:56`; AST `37465cd8d7159b1d1e3671ed4a801a6aeb980355ee91512cce1b6fa95967f3d4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:56`; AST `e8ffd4aebefe271d9f9a096a10acc910c53b50c00bd352d5715d7a1e660672e4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:57`; AST `e858c6df796fc0d4e39eb93913b2332c8d72e433211275f20a7260979f4ae679`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: fixture.bind.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:57`; AST `1091872019abbaedd0ad08db31fbb1363818887a97a38fe6615c915185be8eac`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: fixture.bind.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:58`; AST `0ac5e2842ca4ab545e38dce7a77fc83eea06a193b2cc31176370857ed28ed2eb`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: (fixture.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:58`; AST `d7d2e91227a508baecb70f0637828d21cf6817b52aece5b474b846bb41677ea0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: (fixture.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[5]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:59`; AST `5bbf1136138786f57728360e7c2593fc361b730f459df5cbf2655027e37e11a7`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, fixture, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture.state, retry_limits, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[17].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:59`; AST `fe86f1bd8ea1282fcc7bdfb0255e68b4fb9833ef3dd0ff13d11441c55fb8d8c4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture. Outputs/bindings: (none).
Calls/effect boundaries: fixture.state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[5].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:59`; AST `44e27740e43c984b7cfc40c735cba8bce603860b6f3d4ae4bbc4aac65e0a1b41`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:60`; AST `91fb42ebc4a6cb4d9c282c80aee20ff9cc2c30057aba9fedcf2f069a3a6cf7e7`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, retry_limits. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:60`; AST `1d52fb5c79c68c6ffc62c1fb72a2e4e3c2a115c7dfff0d1359d17ed0d9a75ee2`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, retry_limits. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[6]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:61`; AST `2ce34fa9b2e04e92a86df2bd7d0a151a61277175670ff1270d6156a974ee5bb0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, fixture. Outputs/bindings: consumed.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[6].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:61`; AST `36503a489984a45e280c0c258b9f9ed2bbbfcb5d93f1c54dbe128e7c85477798`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, fixture. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[7]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:62`; AST `f199a254f0e2c3a8da73e8a5077ce1e43ad6fe38c9029cb33ee2d0d285ff77be`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: consumed, dict. Outputs/bindings: later.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[7].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:62`; AST `9fa95ee203d28628170c5259ff986e1c9aac6dca3f02ca6fcfdb07824bb2afbd`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consumed, dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[8]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:63`; AST `93c4c368680c4f9efea2a6b4d7eeb77bed092211acceabe828ce2454d7396dde`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: consumed, fixture, later, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: fixture.state, retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[17].body[3].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[8].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:63`; AST `4b6379af2527eceb2a967f9c9973c6740e39e15926679ce574c56a79190ff02a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consumed, fixture, later. Outputs/bindings: (none).
Calls/effect boundaries: fixture.state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:64`; AST `6388fa2cab2c5aa8792446403f48bdf55d1531d2819577f660f497b7935461fe`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:64`; AST `18142992d2a0289d4086251eeccf1cdb1759b4b02b863e659b7603dc1ad5d6e2`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[8].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:64`; AST `509b00f1113b70d20cea16b8fd7a0a8fb251fb985f29a40d00067f84a5719226`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, retry_limits. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[9]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:66`; AST `4ea7ae5f0da5de5bcceb7920fbe4f92eb5455544a8533f50d2219547e2c0c7b1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fixture, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcQualificationTests::test_consumed_amendment_preserves_failed_history_without_freezing_later_policy::root.body[17].body[3].body[9].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:66`; AST `bc38f0d0f346f070805bd80f0d1e9cdbbe8b53d36077f344bbbf784dfb30c2ed`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fixture, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::root.body[18]::ClassDef

Source: `infra/tests/test_roadmap_python_esbmc.py:69`; AST `e14938916476679225380f5f751b0a7bd8c6f6413f70799f36ac085fcf41a24f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, SUPPORT, all, archive, content, entries, entry, esbmc_link_state, json, link, marker, mode, name, self, stat, tempfile, tool, unittest, x, zipfile. Outputs/bindings: archive, content, entries, entry, link, marker, mode, name, tool, x.
Calls/effect boundaries: (self.destination / 'aegis-release-identity.json').read_text, (self.destination / 'pkg/bin/esbmc').read_bytes, (self.destination / 'pkg/bin/esbmc').stat, Path, SUPPORT.extract_release, all, archive.writestr, esbmc_link_state, json.loads, link.symlink_to, link.unlink, self.addCleanup, self.archive_entries, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.destination.exists, self.destination.with_name, self.destination.with_name('release.staging').exists, self.subTest, tempfile.TemporaryDirectory, zipfile.ZipFile, zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered ClassDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:70`; AST `378c9ca50fa07c92e9ef31639b8e3927056bfff50446f7cdab82d91150ba1584`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: Path, self.addCleanup, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:71`; AST `5a297ee9d55f4a5ad5db69390f11e5ff6b29b0e60014cfe9e10a20b6e9789438`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:71`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:72`; AST `a12d3f2c575f32263e699cd5731a2f11f4bc92700e9417bd96671b447f58f305`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:72`; AST `5a2c45b19a614ce704c6b848fb6284c67bd01e2dc59f0560df9787494a37d110`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:73`; AST `771e6485628d563393a4148f597a406433d53eb73a03e4ac91444a38b131ab10`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:73`; AST `b130fb7f3f48af704e9fdced25074dd867fc0b17d3e9dae24a1bfcce79dfe708`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:74`; AST `eba81544313ecc7a1d0ead4d77c536f3fe5af262f2a17e7797f3ed8f9bcfefed`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::setUp::root.body[18].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:75`; AST `4c508ed1e68d68e0d5bcfe4b42e5da5461bf79d851b19829a104f085aecc502c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:77`; AST `fdc0e59e8dbfcdeccd97af1750ae05711c28b5769dd710429e3d8b53f018b225`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: archive, content, entries, entry, mode, name, self, zipfile. Outputs/bindings: archive, content, entry, mode, name.
Calls/effect boundaries: archive.writestr, zipfile.ZipFile, zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:78`; AST `5aba83cbca84d5a18068dca23bbbc1e935b4b46da242d7b647296abf9ed588bb`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: archive, content, entries, entry, mode, name, self, zipfile. Outputs/bindings: archive, content, entry, mode, name.
Calls/effect boundaries: archive.writestr, zipfile.ZipFile, zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:78`; AST `699d371b1c52c9988e8157508f63af9b269699b30999a5e78d881b973f1782d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, zipfile. Outputs/bindings: (none).
Calls/effect boundaries: zipfile.ZipFile.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0]::For

Source: `infra/tests/test_roadmap_python_esbmc.py:79`; AST `e9fb411e461f509ded719964ce5e6aca3c62e94eb2e0a4bd2b8c84148192dbae`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: archive, content, entries, entry, mode, name, zipfile. Outputs/bindings: content, entry, mode, name.
Calls/effect boundaries: archive.writestr, zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered For evaluation at root.body[18].body[1].body[0].body[0]; no call, error or mutation may be omitted. Iteration: (name, content, mode) in entries
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:80`; AST `bd5b2a3380e8210e33a76d81d6596991e2c4180110dc1207e21f2f99ed8ba4e9`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, zipfile. Outputs/bindings: entry.
Calls/effect boundaries: zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:80`; AST `87f595cf5acfe3dcbc8e378a42d69de2b8bd5aa48a537ee55e4f67ad1120e610`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, zipfile. Outputs/bindings: (none).
Calls/effect boundaries: zipfile.ZipInfo.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:81`; AST `4eb377e32bd8cdf4f52423fcd12197009a96cfc46b9214519c343c281e6801b9`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:82`; AST `666e336d58c992c84523832bdba00803aebc1c9e6d1073e99a82f3a5fed8a13d`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, mode. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:83`; AST `f5485ff7ed9015bd561b720d947e73767bfd861446d8d1bff2bcb1c21c2a4b9d`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, content, entry. Outputs/bindings: (none).
Calls/effect boundaries: archive.writestr.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::archive_entries::root.body[18].body[1].body[0].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:83`; AST `f01821e86cfb1fdb5a8f22e0bbafe08a29fea9e3e1f6020b87b567bb36724cad`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, content, entry. Outputs/bindings: (none).
Calls/effect boundaries: archive.writestr.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:85`; AST `c0ffb5b0afc4de25fafd4d63591a217d5100f20e031426ad09f394ff8dab743f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, SUPPORT, all, esbmc_link_state, json, link, marker, self, stat, tool, x. Outputs/bindings: link, marker, tool, x.
Calls/effect boundaries: (self.destination / 'aegis-release-identity.json').read_text, (self.destination / 'pkg/bin/esbmc').read_bytes, (self.destination / 'pkg/bin/esbmc').stat, SUPPORT.extract_release, all, esbmc_link_state, json.loads, link.symlink_to, link.unlink, self.archive_entries, self.assertEqual, self.assertNotEqual, self.assertRaisesRegex, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:86`; AST `c2ad82957091bf53c8487cd392cc1a1b220b868333fbe2601308bc442aeb5b5f`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:86`; AST `ed89e433b9bfc9f75b3802a3b66a9a7e877deb363dd7a97a351c25e2b3b63bea`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:89`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:89`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:90`; AST `612b93fa8bbc8d603f3c0d214e444b9e8e25059490bd59c01f124073f5e2674a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:90`; AST `925170cd28bbd1547151b6260cf8296c4764830214e436dc3f9e38e45d9f5f4a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:90`; AST `cbec8b673a29219b5cde80f9ac27311869e30d574b1c38e47ca1ef6df8bb00b0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').read_bytes.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:91`; AST `46793612378c147ca0dd0704ee57a58a75b33ef89f14015a85819bfebaf6d2c6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').stat, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:91`; AST `b933de71bb349a165ae5b28349d6b3fbbc692e3b0ce396354250cd4bc89cdb78`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').stat, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[3].value.args[0].left.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:91`; AST `02998a3705a6a09d5ebddaa6c48dce00ee2173d0f55408b9da4e0f9f9dca92e8`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'pkg/bin/esbmc').stat.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[3].value.args[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[4]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:92`; AST `211a3e81e4cc9a1e66895704f71291d24af37f8db268862c6468235ad273e709`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: marker.
Calls/effect boundaries: (self.destination / 'aegis-release-identity.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:92`; AST `ebc7947c7ce11b8f24b0f54570b673b5fe956fa6f9bddfba6454daf9188d68d0`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'aegis-release-identity.json').read_text, json.loads.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:92`; AST `df41d5f989f9b64b5fe39d1db8ac07b416d476fb0bc08ecffcf134077c8585dd`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.destination / 'aegis-release-identity.json').read_text.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[5]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:93`; AST `063cbbbde299aaa3f1f9e27c419c4b2356960596cf6205e63b6cc6c3ee82b86a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: marker. Outputs/bindings: tool.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[6]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:94`; AST `829fc7aef7df8c4fa296e4ab8296b523f5d0837f8583c3a8323a17a87304aab4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, esbmc_link_state, self, tool, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[6].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:94`; AST `d1fecea822705891edabe6f0dd9cd76dab31ee06c3b8df4edcb15f4466ac0f41`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, esbmc_link_state, self, tool, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:94`; AST `364ff04efaee62fdff2edfb2e5cd537403ccb4a9b6c0c4c3a0f1c1dd63801dc4`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, esbmc_link_state, self, tool, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_python_esbmc.py:94`; AST `6e06a3d74868c741de141cb61e7bc4b3d21f3da62b1e8bcaf0f10d87692d0013`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: esbmc_link_state, self, tool, x. Outputs/bindings: x.
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[2].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[6].value.args[0].args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:94`; AST `b511563c119f6860351924c3aed7da9fb2cf56462147273659bcde693f4e0eb6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_link_state, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[6].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[7]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:95`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[7].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:95`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[8]::Assign

Source: `infra/tests/test_roadmap_python_esbmc.py:96`; AST `b898b6ac834e63180258d01d51b29630d5252b184cf09c0a9fb6928787ba1e87`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: link.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[9]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:97`; AST `14544be7e699ffc9b0a4c838b0cd8d2388b31de19462db3520ab1c07fede2979`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link. Outputs/bindings: (none).
Calls/effect boundaries: link.unlink.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[9].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:97`; AST `2db2249bb6e89e89f07f360cbcc6ad6b208eda1ac8700a1831ba787794690bff`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link. Outputs/bindings: (none).
Calls/effect boundaries: link.unlink.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[10]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:98`; AST `a855d764216f80e66f8744096ba48f4c161aeb94a581f27e9d615e7990476794`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link. Outputs/bindings: (none).
Calls/effect boundaries: link.symlink_to.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[10].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:98`; AST `687e2cc9f8c0a230b75149d437684d54e956c45b8f389aa0b47c69a147299126`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link. Outputs/bindings: (none).
Calls/effect boundaries: link.symlink_to.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[11]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:99`; AST `f66e0a6cbc851467a75af1ca8c2d59ca1bea9d6e6b482ea829824e3e03404afa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: esbmc_link_state, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[11].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:99`; AST `13d9db3058ff8a4cae50c164e9baf3f120b2d8b497a59ff647c9830de9c606aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_link_state, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state, self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[11].value.args[0].value.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:99`; AST `b511563c119f6860351924c3aed7da9fb2cf56462147273659bcde693f4e0eb6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_link_state, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[11].value.args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[11].value.args[1].value.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:99`; AST `b511563c119f6860351924c3aed7da9fb2cf56462147273659bcde693f4e0eb6`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_link_state, self, tool. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[11].value.args[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[12]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:100`; AST `b24cb97ed786af9ffaab6a3122504250ea54aaa4e8f31eed56c8e6be1577d5cd`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[2].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[12].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:100`; AST `de781f870effc68ac723b08d019f9061e65de0649b6bf4c55a9506c89eb1d33a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[12].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[12].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:101`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_regular_bytes_exec_permissions_and_internal_link_identity_are_preserved::root.body[18].body[2].body[12].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:101`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:103`; AST `4d3eadc663673002cb3e7dc1f61e6a87badfedbabd3ec470a3b12d3922ca7826`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, SUPPORT, entries, self, stat. Outputs/bindings: entries.
Calls/effect boundaries: SUPPORT.extract_release, self.archive_entries, self.assertFalse, self.assertRaises, self.destination.exists, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0]::For

Source: `infra/tests/test_roadmap_python_esbmc.py:104`; AST `79d5e1e026178b126159102e814a50a2959b0cf05c89b33c3b3dd99ab1086c1b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, SUPPORT, entries, self, stat. Outputs/bindings: entries.
Calls/effect boundaries: SUPPORT.extract_release, self.archive_entries, self.assertFalse, self.assertRaises, self.destination.exists, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered For evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted. Iteration: entries in ([('../outside', b'x', stat.S_IFREG | 420)], [('device', b'x', stat.S_IFCHR | 384)], [('same', b'x', stat.S_IFREG | 420), ('same', b'y', stat.S_IFREG | 420)])
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:107`; AST `af38174d5f43ae9a55298772814e17285bbb2dc990ccb6ae346560636d9ab51c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, SUPPORT, entries, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.archive_entries, self.assertFalse, self.assertRaises, self.destination.exists, self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:107`; AST `9279b4e57a66bf18baa07168113637a047871e1dce5c2a43b14e8e1c2018c550`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:108`; AST `bb6b18b3088f8ce7176d4dc251cb7bbc6b857eaf673da5d5f75a356d8ee32e73`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, self. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:108`; AST `089dd33ce5376f7527c5b52614dee215652c79ea5fe425df0eb0d0cb60c86c29`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, self. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[1]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:109`; AST `06c2e296b0581e75bdc85435cd663f8c8611a83e9725dcf799bf02b497e24dbf`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[3].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:109`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:110`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[0].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:110`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:111`; AST `26362ef954877c737d91338e9042b4664aaa7dfd5ac46a0b7758607ade07859d`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, self.destination.exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:111`; AST `4460b475608891cce24f5c7105afde63f8974f90a71404e2b4aa44dc416bf7f1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse, self.destination.exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_traversal_special_files_and_duplicates_are_rejected::root.body[18].body[3].body[0].body[0].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:111`; AST `3735fba093c243675a36cbf90f13d2a352c68d1865962d7133b830004b251527`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.destination.exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_python_esbmc.py:113`; AST `86c859138cede2a5aeb45a3f588d8b7255bc8780959e9b52416cc0343f5faf88`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, SUPPORT, self, stat. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.archive_entries, self.assertRaisesRegex, self.assertTrue, self.destination.with_name, self.destination.with_name('release.staging').exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:114`; AST `8a02adcd56c1c5b1895aaf0c269f2c72a35fa7d2a70a8a8f352e0bef34ddaf7a`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:114`; AST `f5aecf3691fbc310f58e78bf755bf48792fda2ee06bb8c2d67f66028886604e5`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.archive_entries.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[1]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:115`; AST `c7eb11544296bdcc1a79e4560548a332be2acbe20f10f54f5bde4723ab58a6fb`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:115`; AST `a95956f94544590e69441a05c6776be8107c5ab9a9e55d696b621c7f8f17efc8`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:116`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:116`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:117`; AST `fbe734dbf879395c92173ae84054a8bc8d7e64aa10c1709ef0b8668ecacde193`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue, self.destination.with_name, self.destination.with_name('release.staging').exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:117`; AST `9ec43925cb82a1fa6a04fde556116c0110cdfcb925b4cadb56a514a9d35d1407`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue, self.destination.with_name, self.destination.with_name('release.staging').exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:117`; AST `3f079440fcc243eec6834f599b437f8bcc0146bba6d9e8b6bf201a7d0a4ba87b`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.destination.with_name, self.destination.with_name('release.staging').exists.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[2].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:117`; AST `133b154342a30d19bca6ade7daa958922ad7ec07af98da28e38b43c728289b5c`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.destination.with_name.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[2].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[3]::With

Source: `infra/tests/test_roadmap_python_esbmc.py:118`; AST `b824e2dfe1e4ef6257405be4cf441ac836c8bf5587770bdd43ef52684a895892`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered With evaluation at root.body[18].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:118`; AST `cff6ad231986a8322b92feca985c3a3fbaef7aa93adcc73647038ff028f3ec06`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_python_esbmc.py:119`; AST `c5db0dd2953149a4ceb3e7cd40ce686cc1232c3de62a9c7d635c76f347f4b4d1`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_esbmc.py::module::EsbmcArchiveTests::test_escaping_link_and_interrupted_staging_require_recovery::root.body[18].body[4].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_esbmc.py:119`; AST `8acdf5488333a57505996aaae3643d3e8758b37037f789fde3e3543093dd71aa`.

Rust module: `infra::tests::test_roadmap_python_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SUPPORT, self. Outputs/bindings: (none).
Calls/effect boundaries: SUPPORT.extract_release.
Dependencies: __future__, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.roadmap_runtime, importlib.util, json, pathlib, stat, tempfile, test_roadmap_mirrors, unittest, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
