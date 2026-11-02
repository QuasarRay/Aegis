# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 58. Inventory digest: `970c3eadcf96469c0e1ea5385a7613f9f4554a12e8d99756e064ea632c0e48ad`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_locks.py::module::root::Module

Source: `infra/tests/test_locks.py:1`; AST `47a87d9666b444baeb4944ac9510eda13505494d760b5bbe19aa721632acd3a1`.

Rust module: `infra::tests::test_locks`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: FileLock, Path, PermissionError, __file__, calls, info, json, lock, original, os, owner, p, patch, payload, self, socket, str, sys, td, tempfile, transient, unittest. Outputs/bindings: calls, info, lock, original, owner, p, td.
Calls/effect boundaries: FileLock, Path, Path(__file__).resolve, PermissionError, json.dumps, lock.acquire, lock.release, original, os.getpid, p.write_text, patch.object, self.assertEqual, socket.gethostname, str, sys.path.insert, tempfile.TemporaryDirectory, unittest.skipUnless.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[0]::Import

Source: `infra/tests/test_locks.py:1`; AST `43f4e34ee7fca4f32413abaa700f266598a996461148e5c9d4c73aad6700308a`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_locks.py:2`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[2]::Import

Source: `infra/tests/test_locks.py:3`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[3]::ImportFrom

Source: `infra/tests/test_locks.py:4`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[4]::Expr

Source: `infra/tests/test_locks.py:5`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[4].value::Call

Source: `infra/tests/test_locks.py:5`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[4].value.args[1]::Call

Source: `infra/tests/test_locks.py:5`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[4].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_locks.py:5`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[4].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_locks.py:5`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_locks.py:6`; AST `a19e166d00b3c1a61d7380c876517d3c1ed89a4f59fc21e765e78f1c68e4e8e9`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::root.body[6]::ClassDef

Source: `infra/tests/test_locks.py:8`; AST `09b073cb7d6f86489578e44cd7b94bf236406f1fed46bdd5ad6d4f0999820ca5`.

Rust module: `infra::tests::test_locks`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: FileLock, Path, PermissionError, calls, info, json, lock, original, os, owner, p, patch, payload, self, socket, td, tempfile, transient, unittest. Outputs/bindings: calls, info, lock, original, owner, p, td.
Calls/effect boundaries: FileLock, Path, PermissionError, json.dumps, lock.acquire, lock.release, original, os.getpid, p.write_text, patch.object, self.assertEqual, socket.gethostname, tempfile.TemporaryDirectory, unittest.skipUnless.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0]::FunctionDef

Source: `infra/tests/test_locks.py:10`; AST `caa0a72cfa5f0c41a647509add7283e2f77d4addfb75f345a0ca0b202a4768f4`.

Rust module: `infra::tests::test_locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, Path, PermissionError, calls, lock, original, os, owner, patch, payload, self, td, tempfile, transient, unittest. Outputs/bindings: calls, lock, original, owner, td.
Calls/effect boundaries: FileLock, Path, PermissionError, lock.acquire, lock.release, original, os.getpid, patch.object, self.assertEqual, tempfile.TemporaryDirectory, unittest.skipUnless.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0]::With

Source: `infra/tests/test_locks.py:11`; AST `32557d83ff45ec657983274a11cc0e74271e1bee570f032d995e55bb9c05e719`.

Rust module: `infra::tests::test_locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileLock, Path, PermissionError, calls, lock, original, os, owner, patch, payload, self, td, tempfile, transient. Outputs/bindings: calls, lock, original, owner, td.
Calls/effect boundaries: FileLock, Path, PermissionError, lock.acquire, lock.release, original, os.getpid, patch.object, self.assertEqual, tempfile.TemporaryDirectory.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_locks.py:11`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_locks.py:12`; AST `ec9e1cc923d828939b38fcc49a4412bdc2cfa1c699c016476de64165fa8809b6`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, Path, td. Outputs/bindings: lock.
Calls/effect boundaries: FileLock, Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_locks.py:12`; AST `30627a83ad31e824a35c6c307e35f7cd4d0cdac54e25b5448b7c2149eb5d24de`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, Path, td. Outputs/bindings: (none).
Calls/effect boundaries: FileLock, Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[0].value.args[0].left::Call

Source: `infra/tests/test_locks.py:12`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[1]::Assign

Source: `infra/tests/test_locks.py:13`; AST `c3c470e3eaaf583348413e75ef7d3b8a72e6e9a3a68d27f64c9c932a4e6c00dd`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: original.
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[2]::Assign

Source: `infra/tests/test_locks.py:14`; AST `ea758fc917a6b4e922bd51abc7dcc71234b7b830a643c25f92ef27fbe64b8fc1`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: calls.
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3]::FunctionDef

Source: `infra/tests/test_locks.py:15`; AST `e8c85db24089cc6558b1c7278ed8a386aac5d566e1c3f0b914ea657dec2ced41`.

Rust module: `infra::tests::test_locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: PermissionError, calls, original, payload. Outputs/bindings: calls.
Calls/effect boundaries: PermissionError, original.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[0]::Nonlocal

Source: `infra/tests/test_locks.py:16`; AST `c5539003e0db0ebedac566426df17741bcc6f80e9d2a9ec08e30f6a300b5e75a`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Nonlocal evaluation at root.body[6].body[0].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[1]::AugAssign

Source: `infra/tests/test_locks.py:17`; AST `44c61467ea12e0027fb3c0a954809fc03c5dbe618c3bfc8602508170bc09840b`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: calls.
Calls/effect boundaries: (none).
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered AugAssign evaluation at root.body[6].body[0].body[0].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[2]::If

Source: `infra/tests/test_locks.py:18`; AST `9c6d94abb858ee8f1c4d66cb699bd27f07ad5022d9bf902fc08c904942f34c0b`.

Rust module: `infra::tests::test_locks`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: PermissionError, calls. Outputs/bindings: (none).
Calls/effect boundaries: PermissionError.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[6].body[0].body[0].body[3].body[2]; no call, error or mutation may be omitted. Condition: calls == 1
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[2].body[0]::Raise

Source: `infra/tests/test_locks.py:19`; AST `b67fe3a17a4be01e929d28a566b1ecabb57c1549c47cce01ffdc35316cbc117a`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PermissionError. Outputs/bindings: (none).
Calls/effect boundaries: PermissionError.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Raise evaluation at root.body[6].body[0].body[0].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[2].body[0].exc::Call

Source: `infra/tests/test_locks.py:19`; AST `4bc8697a56471151478fa0996828a5150a38a9dfd9003a452ef062538031a62e`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PermissionError. Outputs/bindings: (none).
Calls/effect boundaries: PermissionError.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[3].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[3]::Return

Source: `infra/tests/test_locks.py:20`; AST `73f935ec75d41f96d3cd8ad26b740a688bf5bfd3ed79c4b977083d47feb65737`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, payload. Outputs/bindings: (none).
Calls/effect boundaries: original.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[6].body[0].body[0].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::transient::root.body[6].body[0].body[0].body[3].body[3].value::Call

Source: `infra/tests/test_locks.py:20`; AST `665cbd1e1d873a861e84992a022b0585e056d0b69263cb68dae6d51ffaae1e0e`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, payload. Outputs/bindings: (none).
Calls/effect boundaries: original.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[4]::With

Source: `infra/tests/test_locks.py:21`; AST `7c14a8f2e72351f8c2ee008cfa4b8ae533538269da749a705df87c1d6291d3fc`.

Rust module: `infra::tests::test_locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: lock, patch, transient. Outputs/bindings: owner.
Calls/effect boundaries: lock.acquire, patch.object.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[6].body[0].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[4].items[0].context_expr::Call

Source: `infra/tests/test_locks.py:21`; AST `dd168cf23fc4a8b63c6ac449c2607747188d1a852645c07a0f341954befd055e`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock, patch, transient. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[4].body[0]::Assign

Source: `infra/tests/test_locks.py:22`; AST `2815c11ff09920006a8966a685712ac2be8bb5ee7b3a4cbfa009b8ca90e2d255`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: owner.
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0].body[0].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[4].body[0].value::Call

Source: `infra/tests/test_locks.py:22`; AST `5794adcdacc7a23bccb173be114be44d3481c0b5f8ec7ac61ee6627cd0575003`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[5]::Expr

Source: `infra/tests/test_locks.py:23`; AST `6ccc0325961fff9e50b5cc531c7e8ea8a14d0b4848d7b15e91fafcff38fc2ebd`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: calls, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[0].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[5].value::Call

Source: `infra/tests/test_locks.py:23`; AST `f16b731261d8978fb7991c867aaf075c7d058d2b7e269af86d93ee5f82e503bb`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: calls, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[6]::Expr

Source: `infra/tests/test_locks.py:24`; AST `5fd9c6e5b6742f3739b2719dd65c4d29de8ff7e5d5c0c2cdcd93c5512f8c6ffc`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid, self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[0].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[6].value::Call

Source: `infra/tests/test_locks.py:24`; AST `7acf7ac41965746b86e8918e02066ea78c4e97590c639ac736b6482a7d052c0e`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, owner, self. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid, self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[6].value.args[1]::Call

Source: `infra/tests/test_locks.py:24`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[6].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[7]::Expr

Source: `infra/tests/test_locks.py:25`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[0].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].body[0].body[7].value::Call

Source: `infra/tests/test_locks.py:25`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_transient_permission_error_during_create_is_bounded_contention::root.body[6].body[0].decorator_list[0]::Call

Source: `infra/tests/test_locks.py:9`; AST `f3b5f2d8d113e13da26c450d0af66bc25d50270732937ff48dcb2f72aead5535`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.skipUnless.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[0].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1]::FunctionDef

Source: `infra/tests/test_locks.py:27`; AST `82fc96dc5bf5a9bb98b23e65a877a81b564016a5878a3b53e7eb1c7d071db229`.

Rust module: `infra::tests::test_locks`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, Path, info, json, lock, os, p, self, socket, td, tempfile. Outputs/bindings: info, lock, p, td.
Calls/effect boundaries: FileLock, Path, json.dumps, lock.acquire, lock.release, os.getpid, p.write_text, self.assertEqual, socket.gethostname, tempfile.TemporaryDirectory.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0]::With

Source: `infra/tests/test_locks.py:28`; AST `a2e81622934754121f3bf2cd7c235f22e145652a401c1d3d7fb08f0e7db4cbf7`.

Rust module: `infra::tests::test_locks`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileLock, Path, info, json, lock, os, p, self, socket, td, tempfile. Outputs/bindings: info, lock, p, td.
Calls/effect boundaries: FileLock, Path, json.dumps, lock.acquire, lock.release, os.getpid, p.write_text, self.assertEqual, socket.gethostname, tempfile.TemporaryDirectory.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_locks.py:28`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_locks.py:29`; AST `55783bb176ed4ce7d0b991a51328905eb0b78ddeace767841d0e2c09fe2fcfc8`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: p.
Calls/effect boundaries: Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[0].value.left::Call

Source: `infra/tests/test_locks.py:29`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[1]::Expr

Source: `infra/tests/test_locks.py:29`; AST `5905db0bd1b802c1150eb785f486d007cf8bf749e6d02dc76faf93a0014f5aba`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, p, socket. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, p.write_text, socket.gethostname.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[1].value::Call

Source: `infra/tests/test_locks.py:29`; AST `386af1b7ba22e03db6aeaee520e4ac791feab0e42b164d81858b937b28cde9ab`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, p, socket. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, p.write_text, socket.gethostname.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[1].value.args[0]::Call

Source: `infra/tests/test_locks.py:29`; AST `d1bdb6ceceee230a94e229cfa79ee26649445ed29215bd334c6537079b63eae6`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, socket. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, socket.gethostname.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[1].value.args[0].args[0].values[4]::Call

Source: `infra/tests/test_locks.py:29`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[1].value.args[0].args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[2]::Assign

Source: `infra/tests/test_locks.py:30`; AST `4c7cb84cb2c9f0a8b40febe6572870da6ed4c419b5c624fe507a38249db2134a`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, p. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_locks.py:30`; AST `9f1c68fd97f6c95f56fbdba3a5de218d2e51feac00cc338d031ba5cbd7b63d7e`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, p. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[3]::Assign

Source: `infra/tests/test_locks.py:30`; AST `45aa71cb97bb1fad27df16677e2b8807435b16b0f4ab19a08aa7bf3234567d0d`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: info.
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_locks.py:30`; AST `19f113b1ff996d6a4e1349d4f629dcb1414895f291ae11a26e3a1c7c22771cf0`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[4]::Expr

Source: `infra/tests/test_locks.py:30`; AST `30deb05c6baad0f3a83f0aa611d1090d821268225e119ddb4ecdf610574661a7`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: info, os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid, self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[4].value::Call

Source: `infra/tests/test_locks.py:30`; AST `a3862ebc0d549c75b3ae609bbdef1b79ecbd58432882de53164c9feed1206df9`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: info, os, self. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid, self.assertEqual.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[4].value.args[1]::Call

Source: `infra/tests/test_locks.py:30`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_locks.py:30`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `infra::tests::test_locks`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_locks.py::module::TestProcessLock::test_reclaims_proven_dead_same_host_lock::root.body[6].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_locks.py:30`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `infra::tests::test_locks`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.locks, json, os, pathlib, socket, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
