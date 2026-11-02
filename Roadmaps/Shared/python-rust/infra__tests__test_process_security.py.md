# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 138. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_process_security.py::module::root::Module

Source: `infra/tests/test_process_security.py:1`; AST `6c7fbf6f907173e699bb34a56fb15937fb2f699c63cb19a6f226eb774323ffca`.

Rust module: `infra::tests::test_process_security`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, Result, SecurityError, WorldWritableControl, __file__, child_home, code, ensure_private_control_file, env, failed, json, len, minimal_subprocess_env, old, os, patch, payload, raw, redact_text, redacted, result, root, run_process, self, stat, str, sys, td, tempfile, timed, unittest, values. Outputs/bindings: child_home, code, env, failed, old, payload, raw, redacted, result, root, st_mode, td, timed, values.
Calls/effect boundaries: (root / '~').exists, Path, Path(__file__).resolve, Result, WorldWritableControl, child_home.exists, ensure_private_control_file, env.values, json.loads, len, minimal_subprocess_env, os.environ.get, os.environ.pop, patch, redact_text, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertNotIn, self.assertRaises, self.assertTrue, str, sys.path.insert, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[0]::Import

Source: `infra/tests/test_process_security.py:1`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[1]::Import

Source: `infra/tests/test_process_security.py:2`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[2]::Import

Source: `infra/tests/test_process_security.py:3`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[3]::Import

Source: `infra/tests/test_process_security.py:4`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_process_security.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[5]::Import

Source: `infra/tests/test_process_security.py:6`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_process_security.py:7`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[7]::Expr

Source: `infra/tests/test_process_security.py:9`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[7].value::Call

Source: `infra/tests/test_process_security.py:9`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[7].value.args[1]::Call

Source: `infra/tests/test_process_security.py:9`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[7].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_process_security.py:9`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[7].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_process_security.py:9`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_process_security.py:11`; AST `255dfec4d6ff7dfa92dc78e143e11e331797115bca3317171a233bfe87c5edad`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_process_security.py:12`; AST `e0d658bdbbfe96d5e3d69cef2b913b8594b86e1e1596aa3585eeff94f76da4e4`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::root.body[10]::ClassDef

Source: `infra/tests/test_process_security.py:15`; AST `4644d11bb0869e55fded77d1026af7a7c2e3df4a9d957e8052bb3a3e2e720054`.

Rust module: `infra::tests::test_process_security`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, Result, SecurityError, WorldWritableControl, child_home, code, ensure_private_control_file, env, failed, json, len, minimal_subprocess_env, old, os, patch, payload, raw, redact_text, redacted, result, root, run_process, self, stat, sys, td, tempfile, timed, unittest, values. Outputs/bindings: child_home, code, env, failed, old, payload, raw, redacted, result, root, st_mode, td, timed, values.
Calls/effect boundaries: (root / '~').exists, Path, Result, WorldWritableControl, child_home.exists, ensure_private_control_file, env.values, json.loads, len, minimal_subprocess_env, os.environ.get, os.environ.pop, patch, redact_text, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertNotIn, self.assertRaises, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0]::FunctionDef

Source: `infra/tests/test_process_security.py:16`; AST `afcb393cda830f4514688d68842518d58f243ddaff9dafa1577715750be4650c`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Result, SecurityError, WorldWritableControl, ensure_private_control_file, patch, self, stat. Outputs/bindings: st_mode.
Calls/effect boundaries: Result, WorldWritableControl, ensure_private_control_file, patch, self.assertRaises.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::root.body[10].body[0].body[0]::ClassDef

Source: `infra/tests/test_process_security.py:17`; AST `09d4a5d0633dfa4831000785a2d1911ed4fe421155c4fc23d26a2bd60fefba3f`.

Rust module: `infra::tests::test_process_security`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Result, stat. Outputs/bindings: st_mode.
Calls/effect boundaries: Result.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::is_symlink::root.body[10].body[0].body[0].body[0]::FunctionDef

Source: `infra/tests/test_process_security.py:18`; AST `001d40726349f41eec9b758fa1fcdef633b416083de2b75f324e5e922ab069d3`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::is_symlink::root.body[10].body[0].body[0].body[0].body[0]::Return

Source: `infra/tests/test_process_security.py:19`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[0].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::exists::root.body[10].body[0].body[0].body[1]::FunctionDef

Source: `infra/tests/test_process_security.py:21`; AST `e2468ea02d655157f430692e695fec28d9e614c9d2e6102fc82bbcf742b0ba20`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::exists::root.body[10].body[0].body[0].body[1].body[0]::Return

Source: `infra/tests/test_process_security.py:22`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[0].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::stat::root.body[10].body[0].body[0].body[2]::FunctionDef

Source: `infra/tests/test_process_security.py:24`; AST `3d5b3a31da46a0863b5615f47de58ddfcf7bd655d516292c0f7132cd279e22e6`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Result, stat. Outputs/bindings: st_mode.
Calls/effect boundaries: Result.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::stat::Result::root.body[10].body[0].body[0].body[2].body[0]::ClassDef

Source: `infra/tests/test_process_security.py:25`; AST `8fae4b4fab8d07b28bc1471e10dc36bef370d246b8ec66afce24f4c7f68286c7`.

Rust module: `infra::tests::test_process_security`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: stat. Outputs/bindings: st_mode.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[10].body[0].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::stat::Result::root.body[10].body[0].body[0].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_process_security.py:26`; AST `5b3e8418e8d9986e90feb55fb1458df62a9e4045ead99cb90b95ad09ac9a7649`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stat. Outputs/bindings: st_mode.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0].body[0].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::stat::root.body[10].body[0].body[0].body[2].body[1]::Return

Source: `infra/tests/test_process_security.py:28`; AST `fdae68fdf21a4a2a22d58f35e332a8b32cb5d0437e2a7e0df9c1fbd3f8df8b91`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Result. Outputs/bindings: (none).
Calls/effect boundaries: Result.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[0].body[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::stat::root.body[10].body[0].body[0].body[2].body[1].value::Call

Source: `infra/tests/test_process_security.py:28`; AST `7d1fcb04c603dda39f08bcb355eb17a4ccf931195db8a4bf578a142ef3b50ca4`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Result. Outputs/bindings: (none).
Calls/effect boundaries: Result.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[0].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::__str__::root.body[10].body[0].body[0].body[3]::FunctionDef

Source: `infra/tests/test_process_security.py:30`; AST `3ee5d87821d39047181f461cd82cada1a0d58f9f1a2823f7d357cab8c0697a92`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::WorldWritableControl::__str__::root.body[10].body[0].body[0].body[3].body[0]::Return

Source: `infra/tests/test_process_security.py:31`; AST `03a38a19db662f4f8eb5eb5af3680adb4c9d95b0253a1a7a22b8d97dd9f3ee94`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[10].body[0].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1]::With

Source: `infra/tests/test_process_security.py:33`; AST `7851f8cab5ccbe06402ad705dfa2dd8c094b77ed6cc141db1c33672555d34d29`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: SecurityError, WorldWritableControl, ensure_private_control_file, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: WorldWritableControl, ensure_private_control_file, patch, self.assertRaises.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:33`; AST `be2f67cf88e822258fc07b746af0580fa9ecadd0faa64240acd33c74182252d5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].body[0]::With

Source: `infra/tests/test_process_security.py:34`; AST `db3f905b340663b1a5e02392513aef1d433dbbc2b7aaae45f30b9216a7fc3637`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: SecurityError, WorldWritableControl, ensure_private_control_file, self. Outputs/bindings: (none).
Calls/effect boundaries: WorldWritableControl, ensure_private_control_file, self.assertRaises.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:34`; AST `37c3ccbce2c953510ab1894eab4f5998b7f5c801b36bf166ddcff7f35be57d6a`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SecurityError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].body[0].body[0]::Expr

Source: `infra/tests/test_process_security.py:35`; AST `59670b40b8dae79c6ea35c517e000f44607e7677c919568ae214ed9c9f4df822`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: WorldWritableControl, ensure_private_control_file. Outputs/bindings: (none).
Calls/effect boundaries: WorldWritableControl, ensure_private_control_file.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[0].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_process_security.py:35`; AST `c5877bc6c2fa5a0cf451abba9ee2e1428dcab2ae5aa4869b1b468bab73d0557a`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorldWritableControl, ensure_private_control_file. Outputs/bindings: (none).
Calls/effect boundaries: WorldWritableControl, ensure_private_control_file.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_posix_world_writable_control_adapter_is_rejected_before_use::root.body[10].body[0].body[1].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_process_security.py:35`; AST `8596fdfcda129e64529706e2a4c996d4224065a692bdf75fe9556c2219c5db1d`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorldWritableControl. Outputs/bindings: (none).
Calls/effect boundaries: WorldWritableControl.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].body[1].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1]::FunctionDef

Source: `infra/tests/test_process_security.py:37`; AST `3df232b7d6619e8d2a79620b1128201a3f91a40fbb6a9c306ba33256f7c9248c`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, code, json, result, run_process, self, sys, td, tempfile, values. Outputs/bindings: code, result, td, values.
Calls/effect boundaries: Path, json.loads, run_process, self.assertEqual, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0]::With

Source: `infra/tests/test_process_security.py:38`; AST `3408f4389fbb51714b86274acfcc5f9da2cfc86a38ae1b24fb8ca0ef9e778342`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, code, json, result, run_process, self, sys, td, tempfile, values. Outputs/bindings: code, result, td, values.
Calls/effect boundaries: Path, json.loads, run_process, self.assertEqual, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:38`; AST `ecb94cae50f264bbcdf4a17051065d3fa077b8f40f0517a7c9fed96ab7cc3de6`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_process_security.py:39`; AST `125a81e557cbbc9973c6836cffe8e0d82758dafbd03858ce67a3842702bdec54`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: values.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[1]::Assign

Source: `infra/tests/test_process_security.py:40`; AST `6e976bcda686d0c25080bede9afd18c0d64dbb57fd251d27350e8783b03b44e4`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: code.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[2]::Assign

Source: `infra/tests/test_process_security.py:41`; AST `8fff5bfc0d11bccea81f52c2057d72a768e0a3d0a54a8ed8f47a422dc2546ea3`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, code, run_process, sys, td, values. Outputs/bindings: result.
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_process_security.py:41`; AST `074b2c4440b20b97d310d1026fae7d0dc2773610590223b8347288c953183a18`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, code, run_process, sys, td, values. Outputs/bindings: (none).
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[2].value.keywords[0].value::Call

Source: `infra/tests/test_process_security.py:41`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].body[2].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[3]::Expr

Source: `infra/tests/test_process_security.py:42`; AST `59aae7089c22d105c70dff53ce788d3fa4fed34efa000f6d4f28d500dfbb94af`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_process_security.py:42`; AST `35f0fb4b182fab5acba42128bb38dfdb1c03f7993c872856fba2dc8c91adaa89`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[4]::Import

Source: `infra/tests/test_process_security.py:43`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[10].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_process_security.py:45`; AST `e911435311e6b656d00e3ca7f70f5a5469d0bd1d11488ef82d0e6b93cb6731af`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, result, self, values. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_process_security.py:45`; AST `381b06949a879da0c4e51723868c201e25557be1a4087044d1152ea9c1e3b4f3`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result, self, values. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_preserves_argv_boundaries_for_spaces_quotes_unicode_and_metacharacters::root.body[10].body[1].body[0].body[5].value.args[0]::Call

Source: `infra/tests/test_process_security.py:45`; AST `43380d64825738a41395f7ecc09149833b4f8026530d29a3c377de1e3a236eb8`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].body[0].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2]::FunctionDef

Source: `infra/tests/test_process_security.py:47`; AST `e3f9430439ea4aacef2d6e4f2be5193450b97515cecf80fca60e94298ae77a38`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, len, result, run_process, self, sys, td, tempfile. Outputs/bindings: result, td.
Calls/effect boundaries: Path, len, run_process, self.assertEqual, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0]::With

Source: `infra/tests/test_process_security.py:48`; AST `4f31c965dedcf3074a6b06a61290828bd32d4e2263b29f84be7b0d82487a2b6d`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, len, result, run_process, self, sys, td, tempfile. Outputs/bindings: result, td.
Calls/effect boundaries: Path, len, run_process, self.assertEqual, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:48`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[0]::Assign

Source: `infra/tests/test_process_security.py:49`; AST `9fa65758f2fc0567fe056d383f415a7dc4132ab8300237147defbd43f61434c3`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, run_process, sys, td. Outputs/bindings: result.
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_process_security.py:49`; AST `6a677a71e8ad1b38c3af265c46768a85dc0d85f9c6045a1deaaf12278f312f68`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, run_process, sys, td. Outputs/bindings: (none).
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_process_security.py:51`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[1]::Expr

Source: `infra/tests/test_process_security.py:54`; AST `bea27b90dc939fafb7ce2aa017244b4088d6fac695b3ce6c1e12789ed55e08c1`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, result, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[1].value::Call

Source: `infra/tests/test_process_security.py:54`; AST `bdb5c12078388075afe3252c9fe4001f9a974c8437561317babcf6a5f0dc533f`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, result, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[1].value.args[0]::Call

Source: `infra/tests/test_process_security.py:54`; AST `81502d7507b3e8a2ef41698c37d1d301af8abc5347ae1abb2bdde43405883c37`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, result. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[2]::Expr

Source: `infra/tests/test_process_security.py:55`; AST `bde3999d7251baa7f338c6fcaa9946b355fa15e6b0f19d3092e7d49308701ab9`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, result, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[2].value::Call

Source: `infra/tests/test_process_security.py:55`; AST `af10223124fb6d92093a18b14d9497a59bb21c084bde7c4413ba362ab7297d9f`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, result, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[2].value.args[0]::Call

Source: `infra/tests/test_process_security.py:55`; AST `3c5b8f49d94ca36b0a6f9aa7aa513e833e7218182d079775cd9a7b5c4faa6a2a`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, result. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[3]::Expr

Source: `infra/tests/test_process_security.py:56`; AST `32da1ede5b4439ab00ccf239e4570759c22603911d475347a30e2f31dca99bd2`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[3].value::Call

Source: `infra/tests/test_process_security.py:56`; AST `3145c303a5a661b14402da3659b6be6249a8f1797aadd2c5197fe7322efa132b`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[4]::Expr

Source: `infra/tests/test_process_security.py:57`; AST `8a855687f65948a81f6911e80359efc0f306cae64feb18d29a010ad30fa03c22`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[4].value::Call

Source: `infra/tests/test_process_security.py:57`; AST `f51f6b9a23f2e49fe1e3ccf60bd2b75e92bbdcc84dacc86671d4f86bc47424cf`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[5]::Expr

Source: `infra/tests/test_process_security.py:58`; AST `d6ca9879b6762ad14bc173a6ed3414990c1ff282cf4848a13bf2bf3c8c1b84a3`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[5].value::Call

Source: `infra/tests/test_process_security.py:58`; AST `564dfee15044ff63ae059d9f682d8c14d7555877b453ee76fb5cb5b453dd962f`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[6]::Expr

Source: `infra/tests/test_process_security.py:59`; AST `36d8a682b0827cbb114c25e37457b76fd9327c2f0dc9a8134424fde40df3297f`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[2].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_stdout_and_stderr_capture_is_bounded::root.body[10].body[2].body[0].body[6].value::Call

Source: `infra/tests/test_process_security.py:59`; AST `08e2e401bfed1235de1ff686fff7b28502c8135e3b397daa9e99578f1d4a4738`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3]::FunctionDef

Source: `infra/tests/test_process_security.py:61`; AST `3dd4c137fa070ede37b7d2f35ecaf24ddee5501ea980d2b05c6db14f26594aa7`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, failed, run_process, self, sys, td, tempfile, timed. Outputs/bindings: failed, td, timed.
Calls/effect boundaries: Path, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0]::With

Source: `infra/tests/test_process_security.py:62`; AST `2704c0522bf424fc55188de0f2dd8a9d2cf40127cea7535851d4e8ab51c4084c`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, failed, run_process, self, sys, td, tempfile, timed. Outputs/bindings: failed, td, timed.
Calls/effect boundaries: Path, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:62`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[0]::Assign

Source: `infra/tests/test_process_security.py:63`; AST `fc7733541e19b8b4205ffe2489e3d6df4806250a60acc53c6ec7b2b6fdb3cb8a`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, run_process, sys, td. Outputs/bindings: failed.
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_process_security.py:63`; AST `d06253a1d36cd5dbcd0acea08dc992ee54cdf060f8c780684c26de863b0f6307`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, run_process, sys, td. Outputs/bindings: (none).
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[0].value.keywords[0].value::Call

Source: `infra/tests/test_process_security.py:63`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[1]::Expr

Source: `infra/tests/test_process_security.py:64`; AST `856bc80f9c1c5bcf398a93573d0d64126cbb1939e2b10300c5b2ce2df353dd5e`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[1].value::Call

Source: `infra/tests/test_process_security.py:64`; AST `6312686b1039b2203de5968cda18c1edd6cd6e214a3523f710a9657cfecc7a71`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[2]::Expr

Source: `infra/tests/test_process_security.py:65`; AST `2ddd11bd597372037bf5dee1a9884119a16230190e635fa632937f3752a86806`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[2].value::Call

Source: `infra/tests/test_process_security.py:65`; AST `c26fa1251d5827f36bda1517e8217bc6544b4fc05c2d10a2a4acd402981311bb`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: failed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[3]::Assign

Source: `infra/tests/test_process_security.py:66`; AST `007d781a04be7518f4effeddef1572c15cf280175f3a84bdcdf3f6d69d640006`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, run_process, sys, td. Outputs/bindings: timed.
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[3].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[3].value::Call

Source: `infra/tests/test_process_security.py:66`; AST `f013d2e90afe0f126588ec62b5e8f0d713c2ea048eb949bc8b21acd58ca625bb`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, run_process, sys, td. Outputs/bindings: (none).
Calls/effect boundaries: Path, run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[3].value.keywords[0].value::Call

Source: `infra/tests/test_process_security.py:66`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[3].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[4]::Expr

Source: `infra/tests/test_process_security.py:67`; AST `da59682f0fc91911ad3f6af4d87e4c075cb7fc786c42bff252257d9db44ecf65`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, timed. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[4].value::Call

Source: `infra/tests/test_process_security.py:67`; AST `7543e4e2604ae873d1aecf721a13973626fc19821dc88ef8ac62d7cdd4612e33`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, timed. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[5]::Expr

Source: `infra/tests/test_process_security.py:68`; AST `42628db063a9c123366c02229970f710322b883098d7cdfebf048d386e568cce`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, timed. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[3].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_law_runner_reports_exact_exit_code_and_timeout_status::root.body[10].body[3].body[0].body[5].value::Call

Source: `infra/tests/test_process_security.py:68`; AST `d8378554d56ee240f8f39018987416176b8b7807ba4d327956ce9e3d0dfa2d8c`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, timed. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4]::FunctionDef

Source: `infra/tests/test_process_security.py:70`; AST `12936b74e6be128f653ba3cf0fd66245148d15d8194ca46113287f5a2ba8ea02`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: raw, redact_text, redacted, self. Outputs/bindings: raw, redacted.
Calls/effect boundaries: redact_text, self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[0]::Assign

Source: `infra/tests/test_process_security.py:71`; AST `ff282496cbaa7a334d2d06d87b48cafbad2f336dfe1fc3670a4ec10c81080c0a`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: raw.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[1]::Assign

Source: `infra/tests/test_process_security.py:72`; AST `9869a3a374e6a2c8604a48528b96ceeda25df6196ef5e77ac59ecac937e22c52`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: raw, redact_text. Outputs/bindings: redacted.
Calls/effect boundaries: redact_text.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[1].value::Call

Source: `infra/tests/test_process_security.py:72`; AST `6cebb20c43b565e606f6b51c4b71d81d6178ef835784cab5fda233c233b09e27`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, redact_text. Outputs/bindings: (none).
Calls/effect boundaries: redact_text.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[2]::Expr

Source: `infra/tests/test_process_security.py:73`; AST `fa238b0978acfa6dc12aca7ad4b638619edea9cf1131c00caadc67291c800250`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[2].value::Call

Source: `infra/tests/test_process_security.py:73`; AST `9a8e35e055c3bbdca3bc67ce56f17fa254dd19612f55beef646a959eb5a0295f`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[3]::Expr

Source: `infra/tests/test_process_security.py:74`; AST `8e967766505f35f2a5b6b9f4115c2010b56849ce07071ceddf405106ebb03f32`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[3].value::Call

Source: `infra/tests/test_process_security.py:74`; AST `5533048046281bfc4a03664b09f3525687a366d68371423d2b6f24a32b37de83`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[4]::Expr

Source: `infra/tests/test_process_security.py:75`; AST `0d5e5135fdae43d98d7d0b15da7864ac7d950ffb0a133a51ad2540962f196c4e`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_framework_redacts_common_token_key_password_and_private_key_patterns::root.body[10].body[4].body[4].value::Call

Source: `infra/tests/test_process_security.py:75`; AST `0ece0faf2bfba3cd28e97042e446b4657da3b5c29b5a47482e9b3872f4a9ab4d`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: redacted, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5]::FunctionDef

Source: `infra/tests/test_process_security.py:77`; AST `7d604f0de250729938e2d19f637fbf4f634aac976f59af5d889fa7d261979100`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: env, minimal_subprocess_env, old, os, self. Outputs/bindings: env, old.
Calls/effect boundaries: env.values, minimal_subprocess_env, os.environ.get, os.environ.pop, self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[0]::Assign

Source: `infra/tests/test_process_security.py:78`; AST `2813896cbe9b91bb90f80df7137acf89b9cf0772b87cb6aec01185348cafb857`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: old.
Calls/effect boundaries: os.environ.get.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[0].value::Call

Source: `infra/tests/test_process_security.py:78`; AST `8583fe87c5d39f6c9713e31dfe19664ba1b26eacf6cbd9f801c1934214411f11`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.get.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[1]::Assign

Source: `infra/tests/test_process_security.py:79`; AST `a6696bfe004bc4e0109b803c51648f3fbf0e53f24d6ad4f12857a741f0f327dc`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2]::Try

Source: `infra/tests/test_process_security.py:80`; AST `80ab09b096e7e2db58681b5e2d77c2fd0c065662fdbf9feef769a65fb568bede`.

Rust module: `infra::tests::test_process_security`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: env, minimal_subprocess_env, old, os, self. Outputs/bindings: env.
Calls/effect boundaries: env.values, minimal_subprocess_env, os.environ.pop, self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Try evaluation at root.body[10].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[0]::Assign

Source: `infra/tests/test_process_security.py:81`; AST `337e4aa95533ab9f4eca881f6517c678e514c860f6253c1b26eadc4f751a805f`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: minimal_subprocess_env. Outputs/bindings: env.
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_process_security.py:81`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[1]::Expr

Source: `infra/tests/test_process_security.py:82`; AST `9a778441998ab5f51d6d4e1cc638f1ca42736351ab57e6c5dc135e3faea99ffc`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[1].value::Call

Source: `infra/tests/test_process_security.py:82`; AST `e07a17fc76517e72691145847f175e5cf2072cc262d1b21ce306552faa1086df`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[2]::Expr

Source: `infra/tests/test_process_security.py:83`; AST `c95dd4538150be13629df8d268c0855e6dae0d6ed8ce60c31ef1da9b683c9081`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, self. Outputs/bindings: (none).
Calls/effect boundaries: env.values, self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[2].value::Call

Source: `infra/tests/test_process_security.py:83`; AST `fd79aa4053ada5d0008d665c05918d31e6138c08169446481b4ee9017acdaef6`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, self. Outputs/bindings: (none).
Calls/effect boundaries: env.values, self.assertNotIn.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].body[2].value.args[1]::Call

Source: `infra/tests/test_process_security.py:83`; AST `7f85b7f4014db12a29b91e84015a80cf99e51d83e9df2ce6a2b3c9212fba4364`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env. Outputs/bindings: (none).
Calls/effect boundaries: env.values.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].finalbody[0]::If

Source: `infra/tests/test_process_security.py:85`; AST `81c236ae35ce6d7d2350242ed94b1b6fc33ad050e2025009bb21e9b36afaf93c`.

Rust module: `infra::tests::test_process_security`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: old, os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.pop.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[10].body[5].body[2].finalbody[0]; no call, error or mutation may be omitted. Condition: old is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].finalbody[0].body[0]::Expr

Source: `infra/tests/test_process_security.py:86`; AST `4a62426d9c472b947222711f525fc999cded45005eb141c7e1c71f5b9178d75d`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.pop.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[5].body[2].finalbody[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].finalbody[0].body[0].value::Call

Source: `infra/tests/test_process_security.py:86`; AST `4bf0f5bca472ddc0b4e3c6bfa907f5aacb1e86f819dbe4f19bb2b7ea3a100151`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.pop.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[5].body[2].finalbody[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_module_action_receives_minimal_environment_allowlist_by_default::root.body[10].body[5].body[2].finalbody[0].orelse[0]::Assign

Source: `infra/tests/test_process_security.py:88`; AST `3f7fc81bb6a529e9fbabfc383ebddbf4e90ed8b05867de01d700f6f1ee2af00d`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: old, os. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[5].body[2].finalbody[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6]::FunctionDef

Source: `infra/tests/test_process_security.py:90`; AST `d5dfd353fc5aa21eed44e0bb83d11fbfdfd4dbb713facc5e5e6a26e7a7226944`.

Rust module: `infra::tests::test_process_security`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, child_home, code, json, payload, result, root, run_process, self, sys, td, tempfile. Outputs/bindings: child_home, code, payload, result, root, td.
Calls/effect boundaries: (root / '~').exists, Path, child_home.exists, json.loads, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0]::With

Source: `infra/tests/test_process_security.py:91`; AST `d39bc1cec3edd7dd6d439370fc1a0c9fdd8494ab7ddcad57aee5410ccf968aa9`.

Rust module: `infra::tests::test_process_security`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, child_home, code, json, payload, result, root, run_process, self, sys, td, tempfile. Outputs/bindings: child_home, code, payload, result, root, td.
Calls/effect boundaries: (root / '~').exists, Path, child_home.exists, json.loads, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[10].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_process_security.py:91`; AST `0f113ab38375d1d23c4a160c5a66059e839881542ebb83e603948e25210539f8`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[0]::Assign

Source: `infra/tests/test_process_security.py:92`; AST `51b339ad191afc36a52c2f830a5bcb3421351fee536642fc319d3901b5260160`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_process_security.py:92`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[1]::Assign

Source: `infra/tests/test_process_security.py:93`; AST `37869cf293a12e52a2cdfdc12d83387fb37d3b222c0589d8a59029d930a06901`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: code.
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[2]::Assign

Source: `infra/tests/test_process_security.py:100`; AST `3c7c6ba2422dd6a3cd798903d7c3434b57e1c006ce74a707334fa806e9695dd0`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: code, root, run_process, sys. Outputs/bindings: result.
Calls/effect boundaries: run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[2].value::Call

Source: `infra/tests/test_process_security.py:100`; AST `272a3fee608ac5f2afbfe7e0aef379a67101f706c816b3fa40a49dc024b5eb5a`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: code, root, run_process, sys. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[3]::Expr

Source: `infra/tests/test_process_security.py:101`; AST `59aae7089c22d105c70dff53ce788d3fa4fed34efa000f6d4f28d500dfbb94af`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[3].value::Call

Source: `infra/tests/test_process_security.py:101`; AST `35f0fb4b182fab5acba42128bb38dfdb1c03f7993c872856fba2dc8c91adaa89`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[4]::Import

Source: `infra/tests/test_process_security.py:102`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[10].body[6].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[5]::Assign

Source: `infra/tests/test_process_security.py:104`; AST `525ad00123968a35002702f38c09cf5cc2af7b664c23dca3a155dfccf863fb16`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, result. Outputs/bindings: payload.
Calls/effect boundaries: json.loads.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[5].value::Call

Source: `infra/tests/test_process_security.py:104`; AST `43380d64825738a41395f7ecc09149833b4f8026530d29a3c377de1e3a236eb8`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[6]::Assign

Source: `infra/tests/test_process_security.py:105`; AST `b6ac8ee42119d35c929b710d35c1e86f57c7c9db38bac4d2a9b31f1d50a9d258`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, payload. Outputs/bindings: child_home.
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[6].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[6].value::Call

Source: `infra/tests/test_process_security.py:105`; AST `bfa11e699f0d0d9c64a83221ac7448857e1fafa5ac8f4a66d021fbd9638e976a`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, payload. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[7]::Expr

Source: `infra/tests/test_process_security.py:106`; AST `34c75460295bd05de0d2837ad1841220338791d309116305a957e55becdc924b`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child_home, root, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[7].value::Call

Source: `infra/tests/test_process_security.py:106`; AST `232958ee1c5d773ebcfa231d7c243adcc8985ca17ddd1b1aaf3bb004406cb2fe`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child_home, root, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[8]::Expr

Source: `infra/tests/test_process_security.py:107`; AST `560f1a3146b4d0b40a08e35e6fdd547b4332887c5a3868d70a7f131c38a80370`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[8].value::Call

Source: `infra/tests/test_process_security.py:107`; AST `a0cb9b7826b2dcb7a15c29a3e2cf2020c4c9c58ddc0eda23c40b20667d56efc4`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[9]::Expr

Source: `infra/tests/test_process_security.py:108`; AST `30ec7fb4b059a406b46afd6c47cd40f2b094cd3896dccbd28a0ef80b3911468b`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: child_home, self. Outputs/bindings: (none).
Calls/effect boundaries: child_home.exists, self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[9].value::Call

Source: `infra/tests/test_process_security.py:108`; AST `ff13034a3cedfcbce3920b2e3fb36346fdd3120be2f63c94558096e64eb7872e`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child_home, self. Outputs/bindings: (none).
Calls/effect boundaries: child_home.exists, self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[9].value.args[0]::Call

Source: `infra/tests/test_process_security.py:108`; AST `39e63eadfc384a81b22bc75c163b877068f5cc1de29723e410db145fd8fc71f3`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: child_home. Outputs/bindings: (none).
Calls/effect boundaries: child_home.exists.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[10]::Expr

Source: `infra/tests/test_process_security.py:109`; AST `20321a3d6db610d9918a5a46ea1983d8e2c14e9d06ca1ea43503e6aaab8adb45`.

Rust module: `infra::tests::test_process_security`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / '~').exists, self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[6].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[10].value::Call

Source: `infra/tests/test_process_security.py:109`; AST `c6ef2f89e8016aa853f42d7d3c5c826ba901d105a89ef56a9fdd20fc9b871bbd`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / '~').exists, self.assertFalse.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_process_security.py::module::TestProcessSecurity::test_subprocess_home_and_cache_are_isolated_outside_workspace_and_removed::root.body[10].body[6].body[0].body[10].value.args[0]::Call

Source: `infra/tests/test_process_security.py:109`; AST `00d430d3a58cab84cce7dab1c788f297eca0c34758dec52a7b95a577c0180721`.

Rust module: `infra::tests::test_process_security`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / '~').exists.
Dependencies: agentinfra.process, agentinfra.security, json, os, pathlib, stat, sys, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[10].body[6].body[0].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
