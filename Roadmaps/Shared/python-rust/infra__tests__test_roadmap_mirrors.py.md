# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 376. Inventory digest: `0f05d62b984b64966c3947a12c5aaa9a5fb726fd63e34f395e45bf52d83d1e27`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_mirrors.py::module::root::Module

Source: `infra/tests/test_roadmap_mirrors.py:1`; AST `90c970b60a2ce6660995fbc1aa69b5b29e796b61c3da572c4d4978658cfc494e`.

Rust module: `infra::tests::test_roadmap_mirrors`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: BudgetLedger, ContractError, OSError, Path, SOURCE, TimeoutError, __file__, __name__, all, any, bad, base, canonical, changed, contextmanager, copy, dependency, dict, digest, effects, entry, failed, field, file_binding, i, io, json, later, ledger, len, limits, mirrors, next, next_request, observations, opener, original, p, partial, patch, policy, r, range, read_json, redirect, registry, request, result, retry_limits, self, shutil, spec, str, target, tempfile, third, time, unittest, url, urllib, value. Outputs/bindings: SOURCE, _, bad, base, canonical, changed, dependency, entry, failed, field, i, later, limits, next_request, observations, opener, original, p, partial, policy, r, redirect, registry, request, result, spec, target, third, url, value.
Calls/effect boundaries: (self.directory / 'quarantine').glob, (self.directory / self.entry['filename']).exists, (self.root / 'authorization.json').write_text, (self.root / 'pin.json').write_text, (self.root / 'spec.json').write_text, (self.root / mirrors.POLICY_PATH).write_text, OSError, Path, Path(__file__).resolve, TimeoutError, all, any, canonical.parent.mkdir, canonical.write_text, copy.deepcopy, dependency.write_text, dict, digest, file_binding, io.BytesIO, json.dumps, len, mirrors._MirrorRedirect, mirrors.download_with_mirrors, next, opener.open.assert_not_called, p.read_bytes, partial.read_bytes, partial.write_bytes, patch, patch.object, policy.parent.mkdir, r.get, range, read_json, redirect.redirect_request, registry.parent.mkdir, registry.with_name, result.read_bytes, retry_limits, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.bind, self.delivery, self.directory.glob, self.directory.mkdir, self.observations, self.state, self.subTest, shutil.copyfile, str, target.read_bytes, target.unlink, target.write_bytes, tempfile.TemporaryDirectory, time.monotonic, unittest.main, unittest.mock.Mock, urllib.request.Request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:1`; AST `8ccf1618ec1abd092125bcc7cd1261c9ebe10d68653e30d1f14e9b9c04ae7171`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:4`; AST `a510406c1fa6f159ec004f4ead0d836747696bf4154e0a5daee8abdfbd9829f0`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_mirrors.py:5`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_mirrors.py:6`; AST `eb75a54c5d0d93fbb694f468951613f2f071166afbbe97a52903fa47a7cef914`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_mirrors.py:7`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_mirrors.py:9`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[8]::Import

Source: `infra/tests/test_roadmap_mirrors.py:10`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[9]::Import

Source: `infra/tests/test_roadmap_mirrors.py:11`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[10]::Import

Source: `infra/tests/test_roadmap_mirrors.py:12`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:13`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[12]::Import

Source: `infra/tests/test_roadmap_mirrors.py:14`; AST `6e0f76526c6d4c47fb54fd80b1a9075af18e040d8abcba786757ca55a9676c61`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:16`; AST `aac246ef0454e14a387d9da5f2d4845a61c5ee589642da6f18eae17017391593`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[14]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:17`; AST `e657de9ec2b99303bf42225ce662ea49fee54ea77f9ad24496b3dbbcda2d14c1`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[15]::ImportFrom

Source: `infra/tests/test_roadmap_mirrors.py:18`; AST `3686934cc48da86467bf9d799093d439e9aeb3e452cc3fe452c505661ecb5c09`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[16]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:21`; AST `adcd0b0b3c8419826507e4f938adabf27b650fd32b42ab39cd9f5294fc93005a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: SOURCE.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[16].value.value.value::Call

Source: `infra/tests/test_roadmap_mirrors.py:21`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[16].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_mirrors.py:21`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::root.body[17]::ClassDef

Source: `infra/tests/test_roadmap_mirrors.py:24`; AST `6ead76a956bb7ab0a5f713e99236341cb3246e726ee0c48beff34e76c0816156`.

Rust module: `infra::tests::test_roadmap_mirrors`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, OSError, Path, SOURCE, TimeoutError, all, any, bad, copy, digest, effects, entry, failed, io, json, len, mirrors, next, next_request, observations, opener, p, partial, patch, policy, r, read_json, redirect, request, result, self, shutil, target, tempfile, time, unittest, url, urllib. Outputs/bindings: _, bad, entry, failed, next_request, observations, opener, p, partial, policy, r, redirect, request, result, target, url.
Calls/effect boundaries: (self.directory / 'quarantine').glob, (self.directory / self.entry['filename']).exists, (self.root / mirrors.POLICY_PATH).write_text, OSError, Path, TimeoutError, all, any, copy.deepcopy, digest, io.BytesIO, json.dumps, len, mirrors._MirrorRedirect, mirrors.download_with_mirrors, next, opener.open.assert_not_called, p.read_bytes, partial.read_bytes, partial.write_bytes, patch.object, policy.parent.mkdir, r.get, read_json, redirect.redirect_request, result.read_bytes, self.addCleanup, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaises, self.assertRaisesRegex, self.assertTrue, self.delivery, self.directory.glob, self.directory.mkdir, self.observations, self.subTest, shutil.copyfile, target.read_bytes, target.unlink, target.write_bytes, tempfile.TemporaryDirectory, time.monotonic, unittest.mock.Mock, urllib.request.Request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:25`; AST `fafa9b995147568459b0a980de052061313d0a1b7337708e7ee85ee47a9bc015`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, SOURCE, digest, len, mirrors, policy, self, shutil, tempfile. Outputs/bindings: policy.
Calls/effect boundaries: Path, digest, len, policy.parent.mkdir, self.addCleanup, shutil.copyfile, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:26`; AST `5a297ee9d55f4a5ad5db69390f11e5ff6b29b0e60014cfe9e10a20b6e9789438`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:26`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:27`; AST `a12d3f2c575f32263e699cd5731a2f11f4bc92700e9417bd96671b447f58f305`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:27`; AST `5a2c45b19a614ce704c6b848fb6284c67bd01e2dc59f0560df9787494a37d110`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:28`; AST `771e6485628d563393a4148f597a406433d53eb73a03e4ac91444a38b131ab10`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:28`; AST `b130fb7f3f48af704e9fdced25074dd867fc0b17d3e9dae24a1bfcce79dfe708`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:29`; AST `d2ed0f76cfe3058cf75648466bf0b8af87f79b3b169baf001e44f3b48b301b72`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirrors, self. Outputs/bindings: policy.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:30`; AST `7d213cfc78571d2bcd32e801fcd6d4d247ed0858c14249faf9e093671d8b2577`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:30`; AST `07d5aa2cd51be906e64166f701f66bd131e34e490d087d4497dc588bf56a3fe1`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:31`; AST `1639dc55d8e64bc7bd5bc723e2cd80ec705b3b27f260294b271769207ad27f24`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SOURCE, mirrors, policy, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:31`; AST `be717af6448e32632b0a93c90b5e31249be8222f5b460887fde57083f333fa49`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SOURCE, mirrors, policy, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:32`; AST `768f56f8b594f774f9af7207e8a1f3e0d9eef036e51ece38707743fab51a6fd2`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[7]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:33`; AST `2d4f87721bab8d46c2d64af337c92b9642942d6efe3f7b6b2a5d39877e2cf351`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:34`; AST `9ae70828bad963b466d5b2adb0be41e23b566b4f671211d6f6a8400310f5d9bf`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, len, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[8].value.values[2]::Call

Source: `infra/tests/test_roadmap_mirrors.py:35`; AST `9190f094ea67ec85823fdcbc5a6edca5e65b3ce8201b6a0644f7174602c01218`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[8].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::setUp::root.body[17].body[0].body[8].value.values[3]::Call

Source: `infra/tests/test_roadmap_mirrors.py:35`; AST `8cda29a63f0da348194524c9f217d9616477e2edfd8aab0186e791c59b32e9a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].body[8].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:39`; AST `5370c8b8717097f962268dd2ebd1f3fb850c40e590cc3185e5bf13c34eb9e0d5`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: effects, entry, mirrors, opener, patch, result, self, time, unittest. Outputs/bindings: opener, result.
Calls/effect boundaries: mirrors.download_with_mirrors, patch.object, time.monotonic, unittest.mock.Mock.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:40`; AST `7c85f0b0db5b138f637d0e24832d1742ade2e1e6c1b68965f498c5ee1871d231`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: opener.
Calls/effect boundaries: unittest.mock.Mock.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:40`; AST `7613194d5c2050775a1d15ac64759edcc38d7a808dbae83cf9b5e7c4d9d74705`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.mock.Mock.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:41`; AST `fc552195420866bab6496e12fe6f86ef37cdcbbf803a391fb91a62b116ada6db`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: effects, opener. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[2]::With

Source: `infra/tests/test_roadmap_mirrors.py:42`; AST `f37258081185ebb3dd97addbdc1439939e4c80fbc350374926d1ff338170c339`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: entry, mirrors, opener, patch, self, time. Outputs/bindings: result.
Calls/effect boundaries: mirrors.download_with_mirrors, patch.object, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:42`; AST `735024f387ce83bdc757134a185fbed89694aae1efcfe61b713b0d595551949c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirrors, opener, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:43`; AST `a0edc701675897654fd5124a00346efa510991e8dbdc32a2042d207ed4565ace`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, mirrors, self, time. Outputs/bindings: result.
Calls/effect boundaries: mirrors.download_with_mirrors, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:43`; AST `0c91a9252a0bed5170969a23ad2ef62b2f64f5b3fa0d85b7a2be9a2e33b29e92`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, mirrors, self, time. Outputs/bindings: (none).
Calls/effect boundaries: mirrors.download_with_mirrors, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[2].body[0].value.args[3].left::Call

Source: `infra/tests/test_roadmap_mirrors.py:43`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].body[0].value.args[3].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::delivery::root.body[17].body[1].body[3]::Return

Source: `infra/tests/test_roadmap_mirrors.py:44`; AST `26b54d560cd3d54a35becfed3d1203503db3d18012055fbbfa51a8ee9502dbfd`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: opener, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::observations::root.body[17].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:46`; AST `9d15fe275a7e87ccd00f6d69bd246a7442c4700f7d8f3e02e50471cb0a781526`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: p, read_json, self. Outputs/bindings: p.
Calls/effect boundaries: read_json, self.directory.glob.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::observations::root.body[17].body[2].body[0]::Return

Source: `infra/tests/test_roadmap_mirrors.py:47`; AST `6150c8c48c09f589d5c7c4125889d95ea3a8000f6d918d9d573afbc3c394d9bf`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p, read_json, self. Outputs/bindings: p.
Calls/effect boundaries: read_json, self.directory.glob.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::observations::root.body[17].body[2].body[0].value::ListComp

Source: `infra/tests/test_roadmap_mirrors.py:47`; AST `8c62e13decfe918b7b92fc656cc80eac6a6a90af2ebf3ce5ae267c231ac2a349`.

Rust module: `infra::tests::test_roadmap_mirrors`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: p, read_json, self. Outputs/bindings: p.
Calls/effect boundaries: read_json, self.directory.glob.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::observations::root.body[17].body[2].body[0].value.elt::Call

Source: `infra/tests/test_roadmap_mirrors.py:47`; AST `305d34a37dd76c49732888b7a55e6ca450cec4c40138bd26acfcffff3b642858`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::observations::root.body[17].body[2].body[0].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_mirrors.py:47`; AST `b63cde1267c425ed677d6484649406abc9b0208c77caa912a12bd13301b64262`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.directory.glob.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:49`; AST `732d5d7810c40c24d6a9701ddea7818d63dd9fad54e6ba0436742ed8e34cda2a`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: TimeoutError, all, digest, io, observations, opener, r, result, self. Outputs/bindings: observations, opener, r, result.
Calls/effect boundaries: TimeoutError, all, digest, io.BytesIO, result.read_bytes, self.assertEqual, self.assertTrue, self.delivery, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:50`; AST `3fd0a3bbcdd6140d74fa1434c7af7b8b1b249cd56866b29a579e61c0bbef3044`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TimeoutError, io, self. Outputs/bindings: opener, result.
Calls/effect boundaries: TimeoutError, io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:50`; AST `6676759a529040ad41ccfb4b86ac6c602ddf7fabad73d46388089ccf25350c63`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TimeoutError, io, self. Outputs/bindings: (none).
Calls/effect boundaries: TimeoutError, io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[0].value.args[0].elts[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:50`; AST `8466427f2e8b20ef5539fd24cf337f57d1a856adef36f2069e1de62e99c538aa`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TimeoutError. Outputs/bindings: (none).
Calls/effect boundaries: TimeoutError.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[0].value.args[0].elts[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:50`; AST `b5b3dc1944810ba92d67497036310da64ccc8322c3116349cafa8d869b8d0ac0`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[0].value.args[0].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:51`; AST `7aebdd6734155f08846689a0808fd76d42b399fc096976758b2de786becd3aab`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:51`; AST `1ae23c041b715669a7d69ee2dd7f3c65c6e83300503b6f0cdc36385030086599`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:51`; AST `d0a5b9c6d66f5f89863eca33165b33ed7a4c13e81cbda45d7a9f5d5bec9e5b8a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:52`; AST `b3b3dd0fd4b9b931c75ed01f4cd06f8c04f23c0dd2e32858b70589e85f6d4fd9`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: opener, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:52`; AST `85a0b618472ed571cd3b681555c1e88034ff2617930151e91ddaea938432c4e3`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:53`; AST `0e32fa0bde41675bdcfaceab6cef4f02e6c3cabb8a6b4f599e356be7adc95eda`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: observations.
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:53`; AST `b5b7b202c2e5b083d57470531646e7e825a9d72cdb440b92d9bb0270c274226b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:54`; AST `d62332257d44e846743e5befb11bfeef9757770a151a74a3eacdea6c8b204cfa`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:54`; AST `7e092413a9b0d4f43927e705d90089809fb2204d5d2351b59fdfe1845371badd`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[4].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_mirrors.py:54`; AST `39558a776239f8b49e3e7f9d4717ce9d5ad61962fb6d9ac33ec76eb42f0eae49`.

Rust module: `infra::tests::test_roadmap_mirrors`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: observations, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered SetComp evaluation at root.body[17].body[3].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[5]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:55`; AST `64ad15aa17303d0b416d1246b68af1ed3c16455de363d59c6e768acb24a465de`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, digest, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all, digest, self.assertTrue.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[5].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:55`; AST `33cf95a9bd45764113863f5d5802dc22d6f1d3be914e96278e413e77b54ade51`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, digest, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all, digest, self.assertTrue.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:55`; AST `a4281cc61f0ade934ba3d05c83ad073a9c1ce03c0be9e16baaa2ba24aa180cbf`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, digest, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all, digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[5].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_mirrors.py:55`; AST `1d523eacc91a09c01d8ca7529793f6e1ec27b636e5841c1d7734855985ce2b40`.

Rust module: `infra::tests::test_roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: digest, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[3].body[5].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[5].value.args[0].args[0].elt.values[0].comparators[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:55`; AST `9190f094ea67ec85823fdcbc5a6edca5e65b3ce8201b6a0644f7174602c01218`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[5].value.args[0].args[0].elt.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[6]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:56`; AST `6f02404f012dce997455fda7820a691c4f4edabe7a019244eb834de5ade22cb1`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[6].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:56`; AST `d6430baff1a38e654d97dbb9b2e6dea02dc7be0ef614bfe189a3cc5fa60d4a53`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:56`; AST `d8f822232097139d27d6c076f112fea14dbdf7b1fcc8090799adfaf82312336b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_transport_failure_uses_identical_reviewed_mirror::root.body[17].body[3].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_mirrors.py:56`; AST `1a24cb05ae29a95cb50cf3d1102981ef4ac540292366fe656848a9699a048374`.

Rust module: `infra::tests::test_roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: observations, r, self. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[3].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:58`; AST `239e23009e6b78f188e6b6ea5612bef3c247f6a2059d778de101746128ffdcf2`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: bad, digest, failed, io, len, next, p, r, result, self. Outputs/bindings: _, bad, failed, p, r, result.
Calls/effect boundaries: (self.directory / 'quarantine').glob, digest, io.BytesIO, len, next, p.read_bytes, result.read_bytes, self.assertEqual, self.assertIn, self.delivery, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:59`; AST `2ba167819b71576dd27d09ae5239966638f4698072a164c918108873dd68b3cf`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, self. Outputs/bindings: bad.
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[0].value.right::Call

Source: `infra/tests/test_roadmap_mirrors.py:59`; AST `8cda29a63f0da348194524c9f217d9616477e2edfd8aab0186e791c59b32e9a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:60`; AST `c42eefbcd1ebd7a4d03d8972bdbab10877ea11087405f7101fbb5b5bd277de95`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bad, io, self. Outputs/bindings: _, result.
Calls/effect boundaries: io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:60`; AST `81b38b815db330b7919a7ce54849ab8d37458a3b24b9c359097b7c1572ceaea7`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[1].value.args[0].elts[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:60`; AST `97c03b632498c74101ee56725cf6a5493e7997698edafe8435539dae3a89cc27`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, io. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[1].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[1].value.args[0].elts[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:60`; AST `b5b3dc1944810ba92d67497036310da64ccc8322c3116349cafa8d869b8d0ac0`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[1].value.args[0].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:61`; AST `7aebdd6734155f08846689a0808fd76d42b399fc096976758b2de786becd3aab`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:61`; AST `1ae23c041b715669a7d69ee2dd7f3c65c6e83300503b6f0cdc36385030086599`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:61`; AST `d0a5b9c6d66f5f89863eca33165b33ed7a4c13e81cbda45d7a9f5d5bec9e5b8a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:62`; AST `012272413e8bd59636e1b7c7e4f7ba1cf3ef3c291b1eab88e0fd857ab9d8d686`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bad, p, self. Outputs/bindings: p.
Calls/effect boundaries: (self.directory / 'quarantine').glob, p.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:62`; AST `491bf93893304dc4c82889727c85a57418d3e6d0eee8bfa43eae44895519e578`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, p, self. Outputs/bindings: p.
Calls/effect boundaries: (self.directory / 'quarantine').glob, p.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[3].value.args[0]::ListComp

Source: `infra/tests/test_roadmap_mirrors.py:62`; AST `024fc694aacc6bc1b99446fa6564133d030d5108c9745bdbaa264d2c8757ef2b`.

Rust module: `infra::tests::test_roadmap_mirrors`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: p, self. Outputs/bindings: p.
Calls/effect boundaries: (self.directory / 'quarantine').glob, p.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[4].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[3].value.args[0].elt::Call

Source: `infra/tests/test_roadmap_mirrors.py:62`; AST `6b83dca35b721a6480711503aa48f3d020a7a02c07f5371d07b93bdc3b0800e8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[3].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_mirrors.py:62`; AST `32f6d3db430a7cb210cfaee03d5f23fe456fe738797ecd643ad2b7ad449aef7d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.directory / 'quarantine').glob.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[4]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:63`; AST `4ca76b2b43da7ac163c2ee7b16c7e5655e3a5d4c74f74fccab59406037df44d6`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: next, r, self. Outputs/bindings: failed, r.
Calls/effect boundaries: next, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:63`; AST `2b4d53ae0ffaf075c52110c2aa3c0802a0fe0c2ab14b671e4a4c00c27d524451`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: next, r, self. Outputs/bindings: r.
Calls/effect boundaries: next, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[4].value.args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_mirrors.py:63`; AST `018430ed8e17d03614039338f53440a5c0cda37394233f7a74a56ed310bd423e`.

Rust module: `infra::tests::test_roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: r, self. Outputs/bindings: r.
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[4].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_mirrors.py:63`; AST `b5b7b202c2e5b083d57470531646e7e825a9d72cdb440b92d9bb0270c274226b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:64`; AST `02439d3a158be5bd038e29e0501f3338b90def088cad37c86041231ca363ca20`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bad, digest, failed, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:64`; AST `612a12653661bdd107acbac4781c8496e4196e1672e71d94e93486b14560da7d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, digest, failed, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[5].value.args[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:64`; AST `0fba7b57020775effabac4a0dd05b7ace3d96b29e466b8d32c0138a7ad419754`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bad, digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:65`; AST `ce893ce6634f69741201eb32008be42f67fcb784e9bb885b6288b16b068cbd43`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_wrong_hash_quarantined_before_next_route::root.body[17].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:65`; AST `811a487c98404e6e838da89faa017558222a2903046f919d99892b27cd4a40fa`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:67`; AST `bab1427fe9b9c8b9e4e1888f5fecd8f4b1ecf563e541867c918d8dcf8f20d0d9`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, io, len, r, result, self. Outputs/bindings: _, r, result.
Calls/effect boundaries: any, io.BytesIO, len, r.get, result.read_bytes, self.assertEqual, self.assertTrue, self.delivery, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:68`; AST `afda17fd68c8a2d4afcc192692bc6fba5c77fb962a898ca87de004cb8afdd09b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: io, self. Outputs/bindings: _, result.
Calls/effect boundaries: io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:68`; AST `5c45da8c22b8c29d564c3da61043b555156ad27fbb4ebe70e75e94d688b0752a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[0].value.args[0].elts[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:68`; AST `c89fa00025a3999e69ae6f7fba01bad88e91c6a6b208ed0cefaec17717e44fa9`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[0].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[0].value.args[0].elts[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:68`; AST `b5b3dc1944810ba92d67497036310da64ccc8322c3116349cafa8d869b8d0ac0`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, self. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[0].value.args[0].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:69`; AST `7aebdd6734155f08846689a0808fd76d42b399fc096976758b2de786becd3aab`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:69`; AST `1ae23c041b715669a7d69ee2dd7f3c65c6e83300503b6f0cdc36385030086599`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:69`; AST `d0a5b9c6d66f5f89863eca33165b33ed7a4c13e81cbda45d7a9f5d5bec9e5b8a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `9b02a20af114f28545c5c4f4039626d03effc1bdf547fff82ee5bf8c31d9e0e5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, len, r, self. Outputs/bindings: r.
Calls/effect boundaries: any, len, r.get, self.assertTrue, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `e32c85c025652c09c25c57d49869aac8a60229763da41c1e7e148db0790716d2`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, len, r, self. Outputs/bindings: r.
Calls/effect boundaries: any, len, r.get, self.assertTrue, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `85727e011c872429347d8b4fd78ca63eeca12ed8cff11c4124884c6512ee877e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, len, r, self. Outputs/bindings: r.
Calls/effect boundaries: any, len, r.get, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `88fed57a503f1a2f0aaa50b245078e5315c4af6f70f5a7a95c480d9cc9553b24`.

Rust module: `infra::tests::test_roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: len, r, self. Outputs/bindings: r.
Calls/effect boundaries: len, r.get, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[5].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value.args[0].args[0].elt.left::Call

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `1a4387930cd34930fded6ab18d902a7b3676a8d57334934e162355f56fb06c4c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: r.get.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0].args[0].elt.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value.args[0].args[0].elt.comparators[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `8cda29a63f0da348194524c9f217d9616477e2edfd8aab0186e791c59b32e9a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0].args[0].elt.comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_oversize_source_cannot_be_promoted::root.body[17].body[5].body[2].value.args[0].args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_mirrors.py:70`; AST `b5b7b202c2e5b083d57470531646e7e825a9d72cdb440b92d9bb0270c274226b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].body[2].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:72`; AST `2a8cef927a693ef280193eb699cecf14e4f3db99bf6499c1592c51d021aa72d6`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, OSError, TimeoutError, len, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.directory / self.entry['filename']).exists, OSError, TimeoutError, len, self.assertEqual, self.assertFalse, self.assertRaisesRegex, self.delivery, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0]::With

Source: `infra/tests/test_roadmap_mirrors.py:73`; AST `ff05821e27f0fbacaa8d5ee4cbf0e7d49b8bc83bcf929d2e3fb25dc4f79c7dd5`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, OSError, TimeoutError, self. Outputs/bindings: (none).
Calls/effect boundaries: OSError, TimeoutError, self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:73`; AST `c10e3fe449d8daa212ab542a31e0ee24ba0c553b377475624e996e54d72a2cf1`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:74`; AST `352f10434bd40f6d4befaa24c8a5000084d275a51210ff7fd2ae0716df02c1e3`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: OSError, TimeoutError, self. Outputs/bindings: (none).
Calls/effect boundaries: OSError, TimeoutError, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:74`; AST `88a20f0a4701e0d8f80f1a4d5f8c874f8582fe4cf73b54a86f980717b8d86a76`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError, TimeoutError, self. Outputs/bindings: (none).
Calls/effect boundaries: OSError, TimeoutError, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0].body[0].value.args[0].elts[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:74`; AST `9203c933b22a6cf2a4c1af20c5133efc35a076c4798eb5854d2a2b3a249ff195`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TimeoutError. Outputs/bindings: (none).
Calls/effect boundaries: TimeoutError.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].body[0].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[0].body[0].value.args[0].elts[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:74`; AST `f061966822b953d351860694a7594bfa51ade96c7422070ddc7c252f063152a1`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: OSError. Outputs/bindings: (none).
Calls/effect boundaries: OSError.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[0].body[0].value.args[0].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:75`; AST `9a998597f66f48a44bfd0dc60348baf434db9333e7c4cc5843fad78b202058e8`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.directory / self.entry['filename']).exists, self.assertFalse.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:75`; AST `a28a7cd36398a1158060d83d910ed5364d256d86d8e1d1e387766984e83df351`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.directory / self.entry['filename']).exists, self.assertFalse.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:75`; AST `53761d5e82bc744b971462814c1265af9d27dfacd405edd14671517b457dc8a5`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.directory / self.entry['filename']).exists.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:76`; AST `42fc8255105c22f3b0682f99e587d45730531560841d44b04048e555515b30f7`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:76`; AST `88a70ea958c31e211b030d4ab1e1954f875cfa5d1131394b219cb20b708899a7`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:76`; AST `6a972f89cfb9454813cde6456b147742cd7b66f4ee84d288ffebb38331ec6239`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_exhausted_sources_leave_no_installable_artifact::root.body[17].body[6].body[2].value.args[0].args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:76`; AST `b5b7b202c2e5b083d57470531646e7e825a9d72cdb440b92d9bb0270c274226b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:78`; AST `ee0457eca6736742ee84998d5a2921f8c269f6eb8ee64357a612ffd5d0f00d75`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, copy, entry, self. Outputs/bindings: entry.
Calls/effect boundaries: copy.deepcopy, self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:79`; AST `e3c43636cad00fe91a3aac4b0e5ba390d16d4b540c79a55a4068bc8c92e3fe86`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: entry.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:79`; AST `4ddfde55d369fbc79353e7f17e0c3cb34e2fa19bd622b6dcae9c77e2a0c026aa`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:80`; AST `d308d1d373c02d02ba4a01a67cfbc828df6faeb4c02eea784ff1ce09a2420ba4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[2]::With

Source: `infra/tests/test_roadmap_mirrors.py:81`; AST `d5d843759e8918bb308e55c0a46a9693f11e8baffaf5a435e6fc8cc4ff87830c`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:81`; AST `43b51de499e5ee4d09e0657e18f3e3d6d16d965f3656fedcada1f3d27fa9ea76`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:82`; AST `eff72e815f883cee24ab8d08579ece3bdabf9668fd26ef592ca11840d7950999`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_original_upstream_cannot_be_removed::root.body[17].body[7].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:82`; AST `e5b2a242f7de5eacda5331e0fc2b3cab8317d77db76b8e4bf60385762b078601`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:84`; AST `0d5d743c014c1ad89618ad594cebaa7c6d42e402777767ae971c31730136deba`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, copy, entry, self, url. Outputs/bindings: entry, url.
Calls/effect boundaries: copy.deepcopy, self.assertRaises, self.delivery, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0]::For

Source: `infra/tests/test_roadmap_mirrors.py:85`; AST `9b2135a0b762ef89bbc742c4712c23ab5f7dd4a371d6546639db744b7f5efca0`.

Rust module: `infra::tests::test_roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, copy, entry, self, url. Outputs/bindings: entry, url.
Calls/effect boundaries: copy.deepcopy, self.assertRaises, self.delivery, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[17].body[8].body[0]; no call, error or mutation may be omitted. Iteration: url in ('http://files.pythonhosted.org/x', 'https://user:secret@files.pythonhosted.org/x', 'https://unreviewed.example/x')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:86`; AST `e3c43636cad00fe91a3aac4b0e5ba390d16d4b540c79a55a4068bc8c92e3fe86`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: entry.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:86`; AST `4ddfde55d369fbc79353e7f17e0c3cb34e2fa19bd622b6dcae9c77e2a0c026aa`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:87`; AST `7a6bef6d227b0504251f0380f9de6895a972ae7238353268711eb05190342b9a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, url. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[2]::With

Source: `infra/tests/test_roadmap_mirrors.py:88`; AST `1bc9634b856acfd7fe5962ba64e29a99e2122b5ab8a2421bcc5a23775a7cb535`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, entry, self, url. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, self.delivery, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[8].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:88`; AST `00ed505af5f5993a537b027a3818c9154350efb8b8f127b5ae16b3bee747953c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, url. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[2].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:88`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].body[2].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:89`; AST `eff72e815f883cee24ab8d08579ece3bdabf9668fd26ef592ca11840d7950999`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:89`; AST `e5b2a242f7de5eacda5331e0fc2b3cab8317d77db76b8e4bf60385762b078601`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:90`; AST `e3c43636cad00fe91a3aac4b0e5ba390d16d4b540c79a55a4068bc8c92e3fe86`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: entry.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:90`; AST `4ddfde55d369fbc79353e7f17e0c3cb34e2fa19bd622b6dcae9c77e2a0c026aa`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[2]::AugAssign

Source: `infra/tests/test_roadmap_mirrors.py:91`; AST `5cb51ab59ad733f1d956a8cb749a1c10540205b474aaa3732781d31b485fbf30`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered AugAssign evaluation at root.body[17].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[3]::With

Source: `infra/tests/test_roadmap_mirrors.py:92`; AST `da0ee54376c3e0c5ce338beabb63671bc7d18b3dba06bbb4a3c081723c31a646`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:92`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:93`; AST `eff72e815f883cee24ab8d08579ece3bdabf9668fd26ef592ca11840d7950999`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_credential_http_unknown_host_and_extra_routes_rejected::root.body[17].body[8].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:93`; AST `e5b2a242f7de5eacda5331e0fc2b3cab8317d77db76b8e4bf60385762b078601`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:95`; AST `c613c34487b48df036105c167aecffc1c9ca8e4e43b4185991ed39e90dcf222d`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, mirrors, next_request, redirect, request, self, url, urllib. Outputs/bindings: next_request, redirect, request, url.
Calls/effect boundaries: mirrors._MirrorRedirect, redirect.redirect_request, self.assertEqual, self.assertRaises, self.subTest, urllib.request.Request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:96`; AST `d875d9b91ab9558f13ef19f4ddeb8f0205748b736295b59fa20da72677f3c216`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, urllib. Outputs/bindings: request.
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:96`; AST `ec642e98f4fbf99ea75f9a94f6ad6b99808d849d2bec429a5aaff50d06a6b3be`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:97`; AST `df341ae3e6c7d883386b86fafb835d03990d7f27add64b2fd5b4fa317d341852`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirrors. Outputs/bindings: redirect.
Calls/effect boundaries: mirrors._MirrorRedirect.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:97`; AST `a7a52e4ca2af325b9e04df4186aca2f187c8950fd26580d1f8e8d1caf05ad0c1`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirrors. Outputs/bindings: (none).
Calls/effect boundaries: mirrors._MirrorRedirect.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2]::For

Source: `infra/tests/test_roadmap_mirrors.py:98`; AST `e2231593ba92a95dc030c871024a73d6ba2b9acd9171ab1bfd46732f3e098ecc`.

Rust module: `infra::tests::test_roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, redirect, request, self, url. Outputs/bindings: url.
Calls/effect boundaries: redirect.redirect_request, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[17].body[9].body[2]; no call, error or mutation may be omitted. Iteration: url in ('http://files.pythonhosted.org/x', 'https://unknown.example/x', 'https://user@files.pythonhosted.org/x')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2].body[0]::With

Source: `infra/tests/test_roadmap_mirrors.py:99`; AST `22331633fa5280e6cfdc935d306b9a7bd9d218b120316dd913ad397adcd404ed`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, redirect, request, self, url. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[9].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:99`; AST `00ed505af5f5993a537b027a3818c9154350efb8b8f127b5ae16b3bee747953c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, url. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:99`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[2].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:100`; AST `f3a6b44e5fb998b611dc8810947cc736a6eeb53eedcb6f6c505af9cc9f1a0e66`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: redirect, request, url. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:100`; AST `834f5348314f30765e896c0fea4ee5de9da81b9445f29550284ef08ec651c525`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redirect, request, url. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:101`; AST `684b84f7de36a69ea9b9e2357c52161736b9e48d96a88d2e804c2232b93ba91b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: redirect, request, self. Outputs/bindings: next_request.
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:101`; AST `52e07b54a3bd42af7bd56c2aa2d12cf48b91e21db9335ed218264ad915390284`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redirect, request, self. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[4]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:102`; AST `e80bd3765bdb7217043d3e5cbc72b68e9099b60418d558a2f6543d04f6be7056`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: next_request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:102`; AST `c7608e80cdfe667bcec4f2f7e9c30ac67f643ea22f78e76319b64eabb93d67d6`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: next_request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[5]::With

Source: `infra/tests/test_roadmap_mirrors.py:103`; AST `d4c4997e0ad9a128392bc21db99359d4fb8ba6e60917220434d9d60c6053c27e`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, next_request, redirect, self. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request, self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[9].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:103`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:104`; AST `39645aa86d319de55532c3fe2f6781fd3ff114f988be930dd3836fce0ce9636b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: next_request, redirect, self. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_redirect_scope_and_count_preserve_https::root.body[17].body[9].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:104`; AST `bd40aa213ad03ea55f7867ec18d0b676525287e9119e0b7de835d1c9d377d815`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: next_request, redirect, self. Outputs/bindings: (none).
Calls/effect boundaries: redirect.redirect_request.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:106`; AST `29816c6e9aa3a43be412057012fe27d8daaffcdf91ec2e6fc5893b81d3163b96`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, partial, self, target. Outputs/bindings: partial, target.
Calls/effect boundaries: partial.read_bytes, partial.write_bytes, self.assertEqual, self.assertRaisesRegex, self.delivery, self.directory.mkdir, target.read_bytes, target.unlink, target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:107`; AST `ff7582cb43ed1a0ac13be53b2826ea104d482c549425c520484c66013a53adc5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.directory.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:107`; AST `fe9ad2326786ba4e3985193bbbe402e3363109aa9bbbc0936b5767187069d60e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.directory.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:108`; AST `cf380ac51f65c573c5bc53971f244eb282032c24ac3f756ad6eee3d57c4cf28f`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:109`; AST `5cdf1dc6ba6d5738a5c9f8f49a45fcadc68ce52c2a76c1e897ede9406e9bda9d`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:109`; AST `0bedcba77682505cccd11acfb61341475740387ab2c2dad8de848238b168f12c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[3]::With

Source: `infra/tests/test_roadmap_mirrors.py:110`; AST `a45bc0b24c2bdc2403bf15fdad2505411746a9fdc936b60c7dcce72a51ba1c02`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:110`; AST `1b2f4e7039958ef561c06260c331e69acc57949b1d9da019ea6bf9e0180f5883`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:111`; AST `5ad682c8a7296d302fdacec9b7fb82814c989eed0a5aa7cfb68b1947e6b233d4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:111`; AST `be9db9f083b3f7d49b9fed9587bd2c6c5f5e2b8fb989a5e01d80d8419c55a430`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[4]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:112`; AST `12177bffce71c1965f1ccaa6b766971f45a6a0b5a7edf2f13f757a5d138834d6`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:112`; AST `094c629ecb1e60e6e5ca8c9eb45a4e994abf4b83ffb9d1762e90fc5e9371ec30`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:112`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[5]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:113`; AST `da0c9d43244753f8bc99002568c5d74891060d6aa2585761c49bbf03990159a5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.unlink.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[5].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:113`; AST `605d476c87030b68332db5a5c2badea4df77f0e5150b12c4471e6ebb5fc08840`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.unlink.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[6]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:114`; AST `c3856335fba80128e5f3586afc36ef783fd8444b3db6440d7eff01eaa56507ec`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: partial.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[7]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:115`; AST `91c842282d85f464ee47543f42daa9c85b2a3cf266133f55a08cf079651e1d50`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[7].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:115`; AST `f816d9c50c48eb785956224049b793aab705a6058f07c5f813c5ff1990f71a09`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[8]::With

Source: `infra/tests/test_roadmap_mirrors.py:116`; AST `b0f4044d7d96c776f2f85c960ae6791b194ebdd8002ba6f8761193601ad507fc`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[10].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[8].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:116`; AST `81141b1d9e45026d4573add024e4799ec6dda121e4e1c93acc21d536f994aa64`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:117`; AST `5ad682c8a7296d302fdacec9b7fb82814c989eed0a5aa7cfb68b1947e6b233d4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:117`; AST `be9db9f083b3f7d49b9fed9587bd2c6c5f5e2b8fb989a5e01d80d8419c55a430`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[9]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:118`; AST `825c8189da7d2603adf37014eee7770e9155b528927f4f85c7768848a47f6eed`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, self. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[9].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:118`; AST `38268cb9e2afc3096b7d1d7bdae6bd3f7dd576d0a9cc2cd39860999133ca62a0`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, self. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_cache_tamper_and_partial_bytes_are_preserved::root.body[17].body[10].body[9].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:118`; AST `036cf7dddaf576ab4be59cf3ea4fc55cafb37cfe12cfe42e258ae18502a59d30`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:120`; AST `b347e7224dc8e62b6f7f0d3822347c1539bfcaa7b2a5353b07e55408f25f1537`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: opener, result, self, target. Outputs/bindings: opener, result, target.
Calls/effect boundaries: opener.open.assert_not_called, self.assertEqual, self.delivery, self.directory.mkdir, target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:121`; AST `ff7582cb43ed1a0ac13be53b2826ea104d482c549425c520484c66013a53adc5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.directory.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:121`; AST `fe9ad2326786ba4e3985193bbbe402e3363109aa9bbbc0936b5767187069d60e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.directory.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:122`; AST `cf380ac51f65c573c5bc53971f244eb282032c24ac3f756ad6eee3d57c4cf28f`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:123`; AST `5ae81faee1582898db03fa7cd2ab2cd1d9a3c7a35fcf55543b0085fb3f731953`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:123`; AST `632c9539df748e41458cf4fe332ed6b5d4796091a7b4a8bbf5b17f6d31bb5416`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:124`; AST `ffdc62392e87faa0cd460e4960b38dd67bb8aa685fdd61577c3364451b7b016a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: opener, result.
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:124`; AST `be9db9f083b3f7d49b9fed9587bd2c6c5f5e2b8fb989a5e01d80d8419c55a430`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[4]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:125`; AST `ac09f3b43e63bde054b3434cce7b454d23aa62c5d20ff2e06762f21e9826ee68`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:125`; AST `a4702e4564beb343ab85597fc74e9d06a8511de64d09e3f421dde7091e33d1d5`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[5]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:126`; AST `b94c9ebd273eefa5c323884418931c866d7e80cd3fcddd7adc8e6cabdaaaa29a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: opener. Outputs/bindings: (none).
Calls/effect boundaries: opener.open.assert_not_called.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_valid_cache_reuses_exact_bytes_without_network::root.body[17].body[11].body[5].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:126`; AST `7f9a972562db9f77ae00090a5b96c02e405e40098f8bf26beda8a1198c962d22`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener. Outputs/bindings: (none).
Calls/effect boundaries: opener.open.assert_not_called.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:128`; AST `8138a29df003674c7fe09ff3b452bf3a6f9a96f3d66c7e57b7fa8f9372928dec`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, json, mirrors, policy, read_json, self, time. Outputs/bindings: policy.
Calls/effect boundaries: (self.root / mirrors.POLICY_PATH).write_text, json.dumps, mirrors.download_with_mirrors, read_json, self.assertRaisesRegex, self.delivery, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[0]::With

Source: `infra/tests/test_roadmap_mirrors.py:129`; AST `56dae47bc4bc7536d1c8344089f0bfb1b7750000fc07c9de829e3f7127d452b3`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, mirrors, self, time. Outputs/bindings: (none).
Calls/effect boundaries: mirrors.download_with_mirrors, self.assertRaisesRegex, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:129`; AST `aa7da1624c4867a85d99250e130a38f8da8b1b6d27214304a4d1e7aa396849f6`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:130`; AST `a3897d94142af5b29eb06f2bbd701c6388ae5aa231f2202a88eae25bd5b468d8`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirrors, self, time. Outputs/bindings: (none).
Calls/effect boundaries: mirrors.download_with_mirrors, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:130`; AST `a1f836a24abb45a64a10adc49a69a916233f30de6f34658b0208db29be006884`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirrors, self, time. Outputs/bindings: (none).
Calls/effect boundaries: mirrors.download_with_mirrors, time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[0].body[0].value.args[3].left::Call

Source: `infra/tests/test_roadmap_mirrors.py:130`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[0].body[0].value.args[3].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:131`; AST `a2abc143ed597fc629a5b8a966ede7bc635837ac0746083c5c870c4f814d93f8`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirrors, read_json, self. Outputs/bindings: policy.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:131`; AST `5bf8fd32a2c916d39b7871e88a8cc261a9aa9eff10b21b466a60d5e1c3ec09e1`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirrors, read_json, self. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[2]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:132`; AST `6b067f4520b4c32b301792b7b6a109df1709b742276a4f69068b4eecbe3b57b6`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[3]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:133`; AST `38c6c9764fe6605d292e5f26be12acdcd832ef12cdc45f4e1f1f458f131e9e05`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, mirrors, policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / mirrors.POLICY_PATH).write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:133`; AST `46f8295734a5c45ac0f798fa5c0a6c1468bc67f4186466838ba45a5f8f759128`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, mirrors, policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / mirrors.POLICY_PATH).write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:133`; AST `2e532a55e51e64b912682eff5bf44491f08f9df4c83d13bbb4271dc4cb3e04d5`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, policy. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[4]::With

Source: `infra/tests/test_roadmap_mirrors.py:134`; AST `979ef21241ad9219abf19c58fc5e4e3ec8b0f002f35fc6bb9319eebf32abd959`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:134`; AST `0f58933f5d7e29bc6444325f19c6fd13d279bb83fb2c88fbf8bb3467e9fe557a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:135`; AST `5ad682c8a7296d302fdacec9b7fb82814c989eed0a5aa7cfb68b1947e6b233d4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::MirrorDeliveryTests::test_deadline_and_weakened_policy_are_denied::root.body[17].body[12].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:135`; AST `be9db9f083b3f7d49b9fed9587bd2c6c5f5e2b8fb989a5e01d80d8419c55a430`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.delivery.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::root.body[18]::ClassDef

Source: `infra/tests/test_roadmap_mirrors.py:138`; AST `ba7009ffb2d27c176ee73a0659e29e059c46c7bd0ca97ec03e0fd94712a8f9af`.

Rust module: `infra::tests::test_roadmap_mirrors`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: BudgetLedger, ContractError, Path, SOURCE, base, canonical, changed, contextmanager, copy, dependency, dict, digest, field, file_binding, i, json, later, ledger, limits, original, patch, range, registry, retry_limits, self, shutil, spec, str, tempfile, third, unittest, value. Outputs/bindings: base, canonical, changed, dependency, field, i, later, limits, original, registry, spec, third, value.
Calls/effect boundaries: (self.root / 'authorization.json').write_text, (self.root / 'pin.json').write_text, (self.root / 'spec.json').write_text, Path, canonical.parent.mkdir, canonical.write_text, copy.deepcopy, dependency.write_text, dict, digest, file_binding, json.dumps, patch, patch.object, range, registry.parent.mkdir, registry.with_name, retry_limits, self.addCleanup, self.assertEqual, self.assertRaises, self.assertRaisesRegex, self.bind, self.state, self.subTest, shutil.copyfile, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:139`; AST `86ffac58c9f83cb0189de13792a386a12b8be506eae04487048128743ac1df93`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, SOURCE, canonical, copy, dependency, digest, file_binding, i, json, range, registry, self, shutil, str, tempfile. Outputs/bindings: canonical, dependency, i, registry.
Calls/effect boundaries: Path, canonical.parent.mkdir, canonical.write_text, copy.deepcopy, dependency.write_text, digest, file_binding, json.dumps, range, registry.parent.mkdir, registry.with_name, self.addCleanup, shutil.copyfile, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:140`; AST `5a297ee9d55f4a5ad5db69390f11e5ff6b29b0e60014cfe9e10a20b6e9789438`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:140`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:141`; AST `a12d3f2c575f32263e699cd5731a2f11f4bc92700e9417bd96671b447f58f305`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:141`; AST `5a2c45b19a614ce704c6b848fb6284c67bd01e2dc59f0560df9787494a37d110`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:142`; AST `771e6485628d563393a4148f597a406433d53eb73a03e4ac91444a38b131ab10`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:142`; AST `b130fb7f3f48af704e9fdced25074dd867fc0b17d3e9dae24a1bfcce79dfe708`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:143`; AST `005afbb4875566c2c3a2c8e6001134ca4b4509e8522f7e1312147f4fc54a5de3`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, self, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:143`; AST `2a0f2dd92bcac8d4c69dd2e1555aa8b968d50fdd104a8e170683ba85144517e6`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[3].value.args[0].values[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:143`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:145`; AST `8aea5e0113c2b7d585ee2146a5b8149e7aa39a6cfacb3a57198d6cf98181bef8`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:146`; AST `57f1ed5e2c0add23c1d57260830584e8e3891f93f8f40e2aac214cde621442ce`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:147`; AST `e2a0d1783010f9d80e0d9876f266d071c36fff64f7b83dd51348ab9e751dc99c`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: registry.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:148`; AST `8616051ac12cc101d1e30d8f053fbf58108d0eea2539e3897388cf86159b44ea`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:148`; AST `bbbcb8956e5971894f7308dde45343e8b2aed52c878af27e39a7e7296225ab46`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:149`; AST `0ea8eda1a2f5e32100a0a6056f6f2bf969eba43126a869ca0d3824168df044f6`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SOURCE, registry, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:149`; AST `d90a99d8e5f9140044d6beb5d4178a7e4cf029d627f154cf4ab8d5b282947b16`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SOURCE, registry, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:150`; AST `97f90283382df9a870f03aac67f2a3a1c23d6b868515c111f3c183541ebe3c95`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SOURCE, registry, shutil. Outputs/bindings: (none).
Calls/effect boundaries: registry.with_name, shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:150`; AST `4aeb3857236d446481a2efa9b45f04326a6454be2fe774d2856921b9255d0069`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SOURCE, registry, shutil. Outputs/bindings: (none).
Calls/effect boundaries: registry.with_name, shutil.copyfile.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[9].value.args[1]::Call

Source: `infra/tests/test_roadmap_mirrors.py:150`; AST `4b608903dba2d5c974450cd54936b4b3be09bc0433589b579a2acc31bd5fe7e4`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: registry. Outputs/bindings: (none).
Calls/effect boundaries: registry.with_name.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[9].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[10]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:151`; AST `5b13672ebdd5714b01b41469d45628e553af784f72cafc5902e1bd19fb31edf4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: canonical.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:152`; AST `9dbf2384491d6fa4e703874b1fa041852382e7caffa14c319190ef297f5ede0f`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:152`; AST `0692e7be09e0b6393f780f1ce58379c1a0e8674cf7ac98a5c8ac21cc560f7c4b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical. Outputs/bindings: (none).
Calls/effect boundaries: canonical.parent.mkdir.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[12]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:153`; AST `6d2f20abc82588d3e22e388b2c36109a6d6b065c2ecfc67e50a2f16db94239dd`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: canonical, json, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical.write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[12].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:153`; AST `dd4dbc63a5c0ba6c522047bb9da9ebe08923822b273f1e1370df7172dff5a096`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: canonical, json, self. Outputs/bindings: (none).
Calls/effect boundaries: canonical.write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[12].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:153`; AST `e50e0c411658cbc8c3c10236194792541eb85c1913bb7e343190a640e4fd2743`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[13]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:154`; AST `26019a129481b09e7346df969c3040fcff055c0a7c88e2d2b24c50d91a3b5822`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: i, range, self, str. Outputs/bindings: i.
Calls/effect boundaries: range, str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[13].value::ListComp

Source: `infra/tests/test_roadmap_mirrors.py:154`; AST `d6e9c95982f703030660678c38666a5edba7bb3b51014ccd51c102a6eb6c1b66`.

Rust module: `infra::tests::test_roadmap_mirrors`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: i, range, self, str. Outputs/bindings: i.
Calls/effect boundaries: range, str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[0].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[13].value.elt.values[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:154`; AST `3480c9734dde8ba366f953e1f08b6c8860809f5c547f367960e813792d6cd22a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[13].value.elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[13].value.elt.values[2].right::Call

Source: `infra/tests/test_roadmap_mirrors.py:154`; AST `3480c9734dde8ba366f953e1f08b6c8860809f5c547f367960e813792d6cd22a`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: i, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[13].value.elt.values[2].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[13].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_mirrors.py:155`; AST `b9058450facd2a894ad7d62db84ef68927abe3ab12ed376a9d83992d8f072f8e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[13].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[14]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:156`; AST `24a88d5ce3ae5005137309adb53f4bd7670152ba7928697626845fcac59b3076`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: dependency.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[15]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:157`; AST `e9edbc8b24c46390ee3c7d8d42b173c5f862c7b3063f748b6fd3f8b08f53e47e`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependency.write_text.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[15].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:157`; AST `18e210536f9fcb09bbb6fbbddf7b66b88bfc796e9be55bafb5a4eb3b86930016`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependency. Outputs/bindings: (none).
Calls/effect boundaries: dependency.write_text.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[16]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:158`; AST `b1e73baa8dbff66fb745191e4cf90aec687d3c03a95c308d91244c16e9f76f25`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy, file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[16].value.values[12].elts[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:164`; AST `1ae7a9663ceaa2b35e26d595cc5efe86f81cca40c76769067550fa9ebabfe439`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[16].value.values[12].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::setUp::root.body[18].body[0].body[16].value.values[13]::Call

Source: `infra/tests/test_roadmap_mirrors.py:164`; AST `9e2c0d4a2557e3b68e5b9300089187c0b2b1d76989ecd8eca1546fc24c7aa48e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[16].value.values[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:167`; AST `75fc13cf89dfd3550797cbd2450a23f9fffeb0aa6a674fae36c96ad4080e3205`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: file_binding, json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'authorization.json').write_text, file_binding, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:168`; AST `4cdefd8aebad40e98e74e821b4e8f92abce30abac9f8be755412e58228f53c2b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'authorization.json').write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:168`; AST `8f3fb6cc173114607647e4f2697bbe1b3317c2dd025eb497e7ba0896cde9c99c`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'authorization.json').write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:168`; AST `7e262b8428f31fd5d195ed75f3c1f912757568fa59155937bbb92b981f9a27a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:169`; AST `de074cfd74a86aef64d4c26f138ef01ae4e60da72945cad426ca23c7ee9b9008`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::bind::root.body[18].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:169`; AST `90bd62f985eed28faa1afc6df4b74f3dd8d67a9379b9ee1318d01b07008f5f3b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::state::root.body[18].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:172`; AST `919067789a47ea006c2cf35fbba8d4dd182c2cd9567811860c98e18f853b9643`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: BudgetLedger, contextmanager, ledger, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch, patch.object.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::state::root.body[18].body[2].body[0]::With

Source: `infra/tests/test_roadmap_mirrors.py:173`; AST `791bec5403552014656654d132c95fa6031dc5fc03a87d677e503ce1ecf3aee3`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: BudgetLedger, ledger, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch, patch.object.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::state::root.body[18].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:173`; AST `73ecc03b31b5269adb9e06a415cd97f9b70ec8db4483d55e54400841e14909d7`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::state::root.body[18].body[2].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:174`; AST `121459cb1b434e0f689e40a04e93fab97aa2ed0859d999ece390e9bbeb5fea4d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: BudgetLedger, ledger, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::state::root.body[18].body[2].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:175`; AST `4ef85b91bd2f837cbb619428370c77b4e8f23faa1461fa93120d8bde06a4c480`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:177`; AST `0abbbfe859d6337867e8e5d22342f464cd22e455be4ee59ce2d9d5e11318581e`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.bind, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[0]::With

Source: `infra/tests/test_roadmap_mirrors.py:178`; AST `a446cd505da3a5b042dcc38e54e762160071b8a853e73f414331de25b98c49e6`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:178`; AST `7384beef407ac96ba58c5adcd9579850a1ec2469bed6f3d948566357e5785d03`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:179`; AST `f571671d78d65559236538d721a132413b2a2465074757c409d450448f7e716c`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:179`; AST `b3aab8c6748d24a23338ca7cab0dae871d39e7776db377e574c6d2947c4036d8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:179`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:180`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:180`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[2]::With

Source: `infra/tests/test_roadmap_mirrors.py:181`; AST `f4fdf50e0f32d750670b3f2c78d7c0c6632c01e53716479c5e5ad8d2b3aed219`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:181`; AST `7384beef407ac96ba58c5adcd9579850a1ec2469bed6f3d948566357e5785d03`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:182`; AST `1c370d3ff263c82b36025b3564d3775a926cdd9d42c74248b72ad67cc6a99310`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:182`; AST `1b877c5ec30ecce25bf38e45b88b6a0afce6a99aa53dc7986ff178c274b50ee8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_default_and_other_work_unit_limits_remain_unchanged::root.body[18].body[3].body[2].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:182`; AST `966a751d2c312a9e9c5a3a8eefe5b4546ca5f8fd6cf80e19a6294fc7515409a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].body[2].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:184`; AST `0abce92c06cd8de89ed0bb54e553b253cfc0ba2972bbc742d885ff9049da22fc`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, limits, retry_limits, self, third. Outputs/bindings: limits, third.
Calls/effect boundaries: dict, retry_limits, self.assertEqual, self.bind, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:185`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:185`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[1]::With

Source: `infra/tests/test_roadmap_mirrors.py:186`; AST `65c52c1c596fd6e89421df40e1ac1b89ef2d67a7dab8b5dee546b84063c6d934`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: retry_limits, self. Outputs/bindings: limits.
Calls/effect boundaries: retry_limits, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:186`; AST `7384beef407ac96ba58c5adcd9579850a1ec2469bed6f3d948566357e5785d03`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:187`; AST `2bda2b5a2435b1f0ed64d7fd6221b0fac913d2da95fba7b714cd9a0f540b7c83`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: limits.
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:187`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:188`; AST `12b5a01d663c7d2694e8e1b5644c9ddb6de071ad6ef320ab33fab9ddfc627a0f`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: limits, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:188`; AST `3cfc3182994a0059fd8d934450eb671d5536a0f4a7ffdc79790667f9bb180756`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: limits, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:189`; AST `2d6069e07b7d7e01b598f1936e42d408b0220965904dc2995b38e17dd8089457`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:189`; AST `eb2bda67ee7910f1736fdbde62df56965bad90e5eb98e933728b838563e7ec97`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[4]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:190`; AST `e5310ca5d6ddfed75dac783ef5d3e787bb53042cc045799876cdbf3affea4f95`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: third.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:190`; AST `c25c0e7856b346f567b6f58c2acdc7079aeb0f27a0304cdce3ee96a30c92f665`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[5]::With

Source: `infra/tests/test_roadmap_mirrors.py:191`; AST `5bcbbd0c3fcc0ca470b2c8b7769470e6551ea937bbc63f022d03501884c9c897`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: limits, retry_limits, self, third. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:191`; AST `e043251ef36b7a949e0b5003cfabc7cc862dc5d8057ded71da3987e76c292152`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, third. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:192`; AST `e9fa776ee11d26ea2b55503655c98f29de7f38e6b6b87c7e1ccd74abc2e17342`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: limits, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:192`; AST `9cca6da8c85a43a96f2507a82850d3ed66ef89c097726f5c98d86b4c7233c17b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: limits, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_exact_scope_preserves_two_failed_attempts::root.body[18].body[4].body[5].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:192`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:194`; AST `9393925380ad6a7bb96fcd92af554e8267a428347672c3216bc46e4f57dec055`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, field, original, retry_limits, self, value. Outputs/bindings: field, original, value.
Calls/effect boundaries: (self.root / 'pin.json').write_text, retry_limits, self.assertRaises, self.assertRaisesRegex, self.bind, self.state, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0]::For

Source: `infra/tests/test_roadmap_mirrors.py:195`; AST `b843e42b291d26dac1a1e14253a02b2619af6769fdaa8342c3885a7f50c346b2`.

Rust module: `infra::tests::test_roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, field, original, retry_limits, self, value. Outputs/bindings: field, original, value.
Calls/effect boundaries: retry_limits, self.assertRaises, self.bind, self.state, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[18].body[5].body[0]; no call, error or mutation may be omitted. Iteration: (field, value) in (('goal_created_at', 2), ('recipe', 'original.tests'), ('preserve_attempt_lineage', False), ('source', {'role': 'assistant', 'content': 'approved'}))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:197`; AST `86c927f8c61ef368f28880b35c75a62143bbb0c99189761f34e4b3e44f4a3ab5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, self. Outputs/bindings: original.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:198`; AST `555ae981faba6910a546bdae77d501a05a78b6ce92a750e050e695400edf7255`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, self, value. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:199`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:199`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3]::With

Source: `infra/tests/test_roadmap_mirrors.py:200`; AST `a582b56a9829c69dd73bae27e152ee7883de974618f055e1ee064d11be6a5aa0`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, field, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertRaises, self.state, self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[5].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:200`; AST `474096bacbee8af39b0bd4c78dc9bc54a203c6e3b07cccbd17d19e2efac34c92`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:200`; AST `7384beef407ac96ba58c5adcd9579850a1ec2469bed6f3d948566357e5785d03`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].body[3].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:200`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].body[3].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:201`; AST `f8545f10af5166e8c371ed64bebec8fe181396ecc1935b6e3cbb4703ec36fa47`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:201`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[0].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:202`; AST `9cd0a139903acd974629bb91235b73feaaaa25fe77b0df8a8f0ba982f6b0b369`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, original, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:203`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:203`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[2]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:204`; AST `7c0e6888d460752567e1ba59422f29f4a7f4c3ca1eb4dfec6369c9497569adc4`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:204`; AST `53a7015b3c7e3fe22ad00bfb48af2531603b5c3fdd57468d65277ca594ee9668`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[3]::With

Source: `infra/tests/test_roadmap_mirrors.py:205`; AST `ef3c6cd2fabe77eabd5c037c89ed3a937da782c19bd3a3c9e2d5adefebea77a8`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertRaisesRegex, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:205`; AST `7384beef407ac96ba58c5adcd9579850a1ec2469bed6f3d948566357e5785d03`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[3].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:205`; AST `44e27740e43c984b7cfc40c735cba8bce603860b6f3d4ae4bbc4aac65e0a1b41`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[3].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:206`; AST `f8545f10af5166e8c371ed64bebec8fe181396ecc1935b6e3cbb4703ec36fa47`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_stale_pin_goal_scope_and_false_authority_denied::root.body[18].body[5].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:206`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:208`; AST `4301fada08034fbfa2bb5821f5534c027c61612aaa79ca4faeeafa472c317daa`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, changed, copy, retry_limits, self. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy, retry_limits, self.assertRaises, self.bind, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:209`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:209`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[1]::With

Source: `infra/tests/test_roadmap_mirrors.py:210`; AST `0da86d017d4c135956ebab1a209affd5500ad8ec0e118115cc21b5d94daf4f29`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertRaises, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:210`; AST `76e726a4cffcc21b3ac75695d162bca231eef62e0a46dfbf97749e6489f6c634`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[1].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:210`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[1].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:211`; AST `f8545f10af5166e8c371ed64bebec8fe181396ecc1935b6e3cbb4703ec36fa47`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:211`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[2]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:212`; AST `f0b94f349a68c9caf2d79b6ee63845048e99cb87d0a7cf87dae795ced48890db`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: changed.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:212`; AST `9e2c0d4a2557e3b68e5b9300089187c0b2b1d76989ecd8eca1546fc24c7aa48e`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[3]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:213`; AST `5e4848fcbefff134ba8fa184236a4d2491de6faf87eff19f09de8e29e5af74be`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changed. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[4]::With

Source: `infra/tests/test_roadmap_mirrors.py:214`; AST `2943a0127bbd93b361506dfb231d71be417135fcb468c51195489935235399e6`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, changed, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertRaises, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:214`; AST `7fa477e170a1d50bd7109c76c35b08ba69d90e463da983081be51479e593cfb3`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[4].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:214`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[4].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:215`; AST `f8545f10af5166e8c371ed64bebec8fe181396ecc1935b6e3cbb4703ec36fa47`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_missing_or_modified_failed_history_denied::root.body[18].body[6].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:215`; AST `17a502995e419634b9b4feca503e221e70145c61944506c6ea42ddc7ba1c2c79`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_mirrors.py:217`; AST `e0c917bf5cfc48c7d50472c847ddd066486310c3d54218a2451e171f8e45691d`.

Rust module: `infra::tests::test_roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: base, dict, digest, file_binding, json, later, retry_limits, self, spec, third. Outputs/bindings: base, later, spec, third.
Calls/effect boundaries: (self.root / 'spec.json').write_text, dict, digest, file_binding, json.dumps, retry_limits, self.assertEqual, self.bind, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:218`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:218`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[1]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:219`; AST `db172352af416bfddd6549a3f9131dc9b5d860d294caad254401935bbf17f752`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: spec.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[2]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:220`; AST `2fd38bd13293afa7a3cce5bad26275cdab9853d3dd4191ac9488761c0b53be6a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[2].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:220`; AST `3254329772b6922735f4ec217b2980d09b0fc6afc04d7da3cfb886c9cb23f6e6`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[3]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:221`; AST `d68cff25adf30b6017d9ff84a31e3e18415711aa3338b2a6159eb03e5a315936`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[3].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:221`; AST `d5f8d3347a3e0a08813cdcf34fc7a8351dd56f2d86ba1c8a2a31dd188823626b`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / 'spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:221`; AST `ce6786d296b3d003b2100e46234b9b78eb236599129eb107d286cbb31d047e76`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, spec. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[4]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:222`; AST `24f628b0a754a33549cc3fe6ee3ffb7844d34b709c20e1a1275949bf0c51e7ee`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, file_binding, self, spec. Outputs/bindings: third.
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[4].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:222`; AST `32731614b2d592b4e637f8f2b2be0dad56ea6c5dc5347e69cd39b92e970b4ceb`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, file_binding, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[4].value.keywords[3].value.values[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:223`; AST `76e4ecdc9e9ac2279120797d420a1364d889a563436fda4e36716aec874c9246`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, self. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[4].value.keywords[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[5]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:224`; AST `31eadcacc7d4a2bd32a20170ecd76f5d2deeba62d71ff5b302498bf758cf382a`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: base.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6]::With

Source: `infra/tests/test_roadmap_mirrors.py:225`; AST `1b851f0762ff94e331d0aa4ea1fec74dddd4b6ee6b4f71dd6b0297e888a2daf8`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: base, retry_limits, self, third. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:225`; AST `e043251ef36b7a949e0b5003cfabc7cc862dc5d8057ded71da3987e76c292152`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, third. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:226`; AST `a19c51e1c9c23fb2f17e973685c5cc5c158dc338075d08dbea0dab60dc190d8e`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:226`; AST `894fb7ad0457ccd7479d75cf7736c8a1b544a8e2da0b4f12420a68adc6b35758`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:226`; AST `51e2c9756bf8c24a5108561d9fde71c05dbb8dc1508ac3ba8d42a1d942032765`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[1]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:227`; AST `3d8c1af4bc95d1629ceb1028ce45f72f602a8062f21932aabf4731d9c3de72d5`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[1].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:227`; AST `24cf633221e5cdaf097d76da9959f942ea1a04169aefd1d39d3df378aa384649`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[6].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[6].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:227`; AST `7e7645dd2e3a2774b44815d473b4296f3c5a01296672501a597ac3a9cba8a148`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[6].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[7]::Assign

Source: `infra/tests/test_roadmap_mirrors.py:229`; AST `61c0b46d504e963ba464ae9cf894042a92fb242ab1a5bd5a3ab9d5e11e0ae109`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, third. Outputs/bindings: later.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[7].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:229`; AST `0a48088cb3741feaa11b7e90c2a5cc62820a6bc369abe66c5fffac71a1ae82de`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, third. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[8]::With

Source: `infra/tests/test_roadmap_mirrors.py:230`; AST `c5fbb56352504376ebb04e22a1f024d08f83a2101be48847c02c4ac23f6caa08`.

Rust module: `infra::tests::test_roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: base, later, retry_limits, self, third. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[18].body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[8].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_mirrors.py:230`; AST `958d82d8e6f909d6ea016e2c43ec542193c0af829a181d0e4efcf979394671ec`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: later, self, third. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:231`; AST `a19c51e1c9c23fb2f17e973685c5cc5c158dc338075d08dbea0dab60dc190d8e`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:231`; AST `894fb7ad0457ccd7479d75cf7736c8a1b544a8e2da0b4f12420a68adc6b35758`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::RetryScopeTests::test_consumed_retry_cannot_expand_a_later_candidate_or_generation::root.body[18].body[7].body[8].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_mirrors.py:231`; AST `51e2c9756bf8c24a5108561d9fde71c05dbb8dc1508ac3ba8d42a1d942032765`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[19]::If

Source: `infra/tests/test_roadmap_mirrors.py:234`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[19]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[19].body[0]::Expr

Source: `infra/tests/test_roadmap_mirrors.py:235`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_mirrors.py::module::root.body[19].body[0].value::Call

Source: `infra/tests/test_roadmap_mirrors.py:235`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, io, json, pathlib, shutil, tempfile, time, unittest, unittest.mock, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
