# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 85. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_destiny_recovery.py::module::root::Module

Source: `infra/tests/test_destiny_recovery.py:1`; AST `d7b911e2ec8d55ab6386db0c2bd2f104e6f74ccac7a5d10eca2f1e6ebccd693f`.

Rust module: `infra::tests::test_destiny_recovery`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContextLedger, DestinyFixture, Path, RuntimeError, SimpleNamespace, __file__, __name__, args, attempts, changed, conclusion, context, denied, dependencies, json, ledger, len, library, load_profile, next, original, patch, path, race, result, self, str, subprocess, sys, unittest. Outputs/bindings: args, attempts, changed, denied, library, original, result.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, (self.root / '.aegis/destiny/cache' / (result['key'] + '.json')).unlink, Path, Path(__file__).resolve, SimpleNamespace, context, json.loads, len, library.write_bytes, load_profile, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text, original, patch.object, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaisesRegex, self.call, self.write, str, subprocess.run, sys.path.insert, unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[0]::Expr

Source: `infra/tests/test_destiny_recovery.py:1`; AST `f4f5c6ec5a92e6e53defcea580dc45deaa195708a747151d598cbefda8b05b8f`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[1]::Import

Source: `infra/tests/test_destiny_recovery.py:2`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:3`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[3]::Import

Source: `infra/tests/test_destiny_recovery.py:4`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[4]::Import

Source: `infra/tests/test_destiny_recovery.py:5`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[5]::Import

Source: `infra/tests/test_destiny_recovery.py:6`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:7`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:9`; AST `e6e65f5530a52602546758453e338fdf915fa82858a214cf46e5add3f8354038`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[8]::Expr

Source: `infra/tests/test_destiny_recovery.py:11`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[8].value::Call

Source: `infra/tests/test_destiny_recovery.py:11`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[8].value.args[1]::Call

Source: `infra/tests/test_destiny_recovery.py:11`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[8].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_destiny_recovery.py:11`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[8].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_destiny_recovery.py:11`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:12`; AST `0b35bf7d9067c30646f468497070d16798aef93e6cd52b40466dd13edad29f82`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:13`; AST `ffdd0fcfc57029f1fddaa38e14c9e7b93b3ab142d550710429ca8b585bac7a52`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_destiny_recovery.py:14`; AST `271cd8a5819453f6952690fd43e9ce152386df249c8de9a1999907454b0006b7`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::root.body[12]::ClassDef

Source: `infra/tests/test_destiny_recovery.py:17`; AST `e23cbd496594984b3ef5ca1aaa5a054782e373b56e8eb4841dcc6145edbc1025`.

Rust module: `infra::tests::test_destiny_recovery`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContextLedger, DestinyFixture, Path, RuntimeError, SimpleNamespace, args, attempts, changed, conclusion, context, denied, dependencies, json, ledger, len, library, load_profile, next, original, patch, path, race, result, self, str, subprocess. Outputs/bindings: args, attempts, changed, denied, library, original, result.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, (self.root / '.aegis/destiny/cache' / (result['key'] + '.json')).unlink, Path, SimpleNamespace, context, json.loads, len, library.write_bytes, load_profile, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text, original, patch.object, path.write_text, self.assertEqual, self.assertFalse, self.assertIn, self.assertRaisesRegex, self.call, self.write, str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_destiny_recovery.py:18`; AST `f903db16da144fbeef319455a45734800fcf83228d50804b4e0cfb7259b14eaa`.

Rust module: `infra::tests::test_destiny_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, library, result, self, str, subprocess. Outputs/bindings: library, result.
Calls/effect boundaries: Path, library.write_bytes, self.assertEqual, self.assertFalse, self.assertIn, self.call, self.write, str, subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[0]::Expr

Source: `infra/tests/test_destiny_recovery.py:19`; AST `c3bca481f85a00018b1ea52953cfaa1889981c15f28e46eb55d656782d14c8c0`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:19`; AST `bede26ed891be2e3bb0fbb98dcc3bc767f4ee3eddfe466a3a5e54f5e6adcd71f`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.write.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[1]::Expr

Source: `infra/tests/test_destiny_recovery.py:20`; AST `e6d1d5b0c6d02dc34b40f559d525e98dceb3ebb277d7af0eb236371f86de474a`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_destiny_recovery.py:20`; AST `5887130b55246dca196b59f80e6effbf723b00c3d62a6dd76e8eebbf8093bffc`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[2]::Expr

Source: `infra/tests/test_destiny_recovery.py:21`; AST `7f2e92f343e84dbdfac2d740aa9ec168dfbc3df7c6c9854edd0ea75242139662`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[2].value::Call

Source: `infra/tests/test_destiny_recovery.py:21`; AST `22f7525b98a8ad366dd921cbf5724c194027863d51cb01531a27ad638f7395c3`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[3]::Assign

Source: `infra/tests/test_destiny_recovery.py:23`; AST `5bad481d41748bf47dceca41bdf62bdee8b32db8af0c511a0a8836d8027ef214`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: library.
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[3].value.left::Call

Source: `infra/tests/test_destiny_recovery.py:23`; AST `350af0ef58dfeabf82fa371e4d1a0525efa6d4376cbcb9b8ead747bbdeb7de21`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[3].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[4]::Expr

Source: `infra/tests/test_destiny_recovery.py:24`; AST `0e6155ad340296be19f5adf9e59e2016e756e104c6b40b2baf66a14b6efe72a2`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: library. Outputs/bindings: (none).
Calls/effect boundaries: library.write_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[4].value::Call

Source: `infra/tests/test_destiny_recovery.py:24`; AST `f770f691fa55d13188fb048ee363dc4f46b9f7acc47a20c4aee449a8f3e301ef`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: library. Outputs/bindings: (none).
Calls/effect boundaries: library.write_bytes.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[5]::Assign

Source: `infra/tests/test_destiny_recovery.py:25`; AST `8c5c04699b0d95166363b89329c63837437ae47e4956d88841d06cec336d690a`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: library, self, str. Outputs/bindings: result.
Calls/effect boundaries: self.call, str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[5].value::Call

Source: `infra/tests/test_destiny_recovery.py:25`; AST `d6a47ec9bc979171308de7a6c176425b912c6a4befde32595c07623a32a23a9a`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: library, self, str. Outputs/bindings: (none).
Calls/effect boundaries: self.call, str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[5].value.args[3]::Call

Source: `infra/tests/test_destiny_recovery.py:25`; AST `531d374d6b75ec14086e1aea690b44e54b7402137cf93951c8a96955114178a7`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value.args[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[5].value.args[5]::Call

Source: `infra/tests/test_destiny_recovery.py:25`; AST `60838d80150d14312902c8985736ce454a5ccd824fb5c676544a81b2dde47a61`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: library, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[5].value.args[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[6]::Expr

Source: `infra/tests/test_destiny_recovery.py:26`; AST `d09c19178af27b78e8a4a08cdd5f77444d62d91374e275b207b372f4e66dc5eb`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[6].value::Call

Source: `infra/tests/test_destiny_recovery.py:26`; AST `a9167befe89e841ffd0e77fa70a8cc05b246829adfd1ac9c327e4481fc84a418`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[7]::Expr

Source: `infra/tests/test_destiny_recovery.py:27`; AST `98c59422e91a2bb55a44c561df5cb95a678c770d60edada80936939b64a2bf0a`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[7].value::Call

Source: `infra/tests/test_destiny_recovery.py:27`; AST `b7e0ad100fcac5e168e01e799e975e0a2371996165172e62b365548933e3ae83`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[8]::Expr

Source: `infra/tests/test_destiny_recovery.py:28`; AST `94883c97394fc405810dc9abcd48e0afc77ce7ae4ebd47478332cfd2ec543731`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_original_reference_is_pinned_before_execution::root.body[12].body[0].body[8].value::Call

Source: `infra/tests/test_destiny_recovery.py:28`; AST `87197201bacf2977f2d741fcc4ab91b34df7482910e647b9b6c2df57d1c2ba04`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_destiny_recovery.py:30`; AST `b863b757b39cbe5b5cf5cebe9ece49d42051dbc5e61fc33f92fccead581f282c`.

Rust module: `infra::tests::test_destiny_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: attempts, denied, json, len, next, result, self. Outputs/bindings: attempts, denied, result.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, (self.root / '.aegis/destiny/cache' / (result['key'] + '.json')).unlink, json.loads, len, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text, self.assertEqual, self.assertIn, self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[0]::Assign

Source: `infra/tests/test_destiny_recovery.py:31`; AST `6095e5e6f3a12b2180157bd3e95d20a1ce808ad0a31224430858d163bcc246db`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: result.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:31`; AST `dd013abe0d0c9a4573cc5c6831953e329ec694f12b14cd339d62250606288a65`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[1]::Expr

Source: `infra/tests/test_destiny_recovery.py:32`; AST `5a2121a76f03de3d6903bdba2a0e974dddbed10292f53a22958ddbab06d97688`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/cache' / (result['key'] + '.json')).unlink.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[1].value::Call

Source: `infra/tests/test_destiny_recovery.py:32`; AST `e72dcecb4ed1fe1ffee03e40940991333d3cf9bb28f1d41bce8cc81fef8333f5`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/cache' / (result['key'] + '.json')).unlink.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[2]::Assign

Source: `infra/tests/test_destiny_recovery.py:33`; AST `f9687136b34be29483dfdacc3edcb633ef12bbcc51e840aa821b9b335a13b218`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: denied.
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[2].value::Call

Source: `infra/tests/test_destiny_recovery.py:33`; AST `c5f2713d7b7fa3cb1effa468e9bdfb1d2d135455e45c21093613ae0de6fef8e7`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.call.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[3]::Expr

Source: `infra/tests/test_destiny_recovery.py:34`; AST `be958d31b92f47ec1409e7a9e8894fc74d955da3d983a205cbdabd7bf54d97e0`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[3].value::Call

Source: `infra/tests/test_destiny_recovery.py:34`; AST `b7085b51c6b7e167f6e929399faa1f32ebb6b9e4aadb016253d141ab3d2b9242`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[4]::Expr

Source: `infra/tests/test_destiny_recovery.py:35`; AST `40613ea76a677b078fa7db369349ed727f9150364f6fe70134f04b90a0499d5a`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[4].value::Call

Source: `infra/tests/test_destiny_recovery.py:35`; AST `ff4dad0273dd99582f944e8efa3eace63454af44b66ff09c5299f45a803a32e0`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: denied, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIn.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[5]::Assign

Source: `infra/tests/test_destiny_recovery.py:36`; AST `1192029d82c96ca893a08381451dccaea6a06fa9ffaeda0a0d6571dcd86f8e50`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, next, self. Outputs/bindings: attempts.
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, json.loads, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[5].value::Call

Source: `infra/tests/test_destiny_recovery.py:36`; AST `bfd4d675b0cadec176c1ff257a214832813bf7480c9fdbdd051798706f76f2f4`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, next, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, json.loads, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[5].value.args[0]::Call

Source: `infra/tests/test_destiny_recovery.py:36`; AST `7e6fd76c928aed3696f464a6bfd05183599a876108321a0ad0494730939e7e1f`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: next, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, next, next((self.root / '.aegis/destiny/attempts').glob('*.json')).read_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[5].value.args[0].func.value::Call

Source: `infra/tests/test_destiny_recovery.py:36`; AST `636922745b7b4fc4c4b4316a89e141e89f3d554ebb31d54cb6227bfc23af6e27`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: next, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob, next.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[5].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[5].value.args[0].func.value.args[0]::Call

Source: `infra/tests/test_destiny_recovery.py:36`; AST `3fcd698eb5974a0c93b8a0aba35f49a1fe7c3572364ca96f7ba5239d73ac8a6d`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.root / '.aegis/destiny/attempts').glob.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[5].value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[6]::Expr

Source: `infra/tests/test_destiny_recovery.py:37`; AST `61f08408f3cf070fa9c6920ebdfe21abfded04e1dc36dc359bc24527f3778525`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: attempts, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[6].value::Call

Source: `infra/tests/test_destiny_recovery.py:37`; AST `cd6a524086025151bb5822a0b3a1a8a04a99f60ec77e18a3bbdcef9650724306`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, len, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_interrupted_attempt_needs_diagnosis_before_retry::root.body[12].body[1].body[6].value.args[0]::Call

Source: `infra/tests/test_destiny_recovery.py:37`; AST `539c885121ef8792d840ffb744d17d6cdd469292090c0d02f91bb0e6f76fa088`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: attempts, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_destiny_recovery.py:39`; AST `75b589e04999a436a49a41c14e897124936da478a7ad88d0d15d872233938ecb`.

Rust module: `infra::tests::test_destiny_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContextLedger, RuntimeError, SimpleNamespace, args, changed, conclusion, context, dependencies, ledger, load_profile, original, patch, path, race, self. Outputs/bindings: args, changed, original.
Calls/effect boundaries: SimpleNamespace, context, load_profile, original, patch.object, path.write_text, self.assertEqual, self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[0]::Assign

Source: `infra/tests/test_destiny_recovery.py:40`; AST `6be36ce434e7745bcdafddc31b329fd69fe76dd656eb16a70a543a4291b58160`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextLedger. Outputs/bindings: original.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[1]::Assign

Source: `infra/tests/test_destiny_recovery.py:41`; AST `2238a8e92b6722eb37d714ced7ec4b2d973af07819155bdb9c435237f9e28aa2`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: changed.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2]::FunctionDef

Source: `infra/tests/test_destiny_recovery.py:43`; AST `5d80a34f2ec6e52060f37e36ad5b3c8ca97dc73c008525aa7b6b7aa66d3cde88`.

Rust module: `infra::tests::test_destiny_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: changed, conclusion, dependencies, ledger, original, path. Outputs/bindings: changed.
Calls/effect boundaries: original, path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[0]::Nonlocal

Source: `infra/tests/test_destiny_recovery.py:44`; AST `7d4f89365e769b0bddadeda4c8f7812646b32ec81a3e21082e65fad4ba866d27`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Nonlocal evaluation at root.body[12].body[2].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[1]::If

Source: `infra/tests/test_destiny_recovery.py:45`; AST `61a8a3d3203ead8bca454d7c4b683d905c9c6ab5ee80ef66501434047e71b8ae`.

Rust module: `infra::tests::test_destiny_recovery`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: changed, path. Outputs/bindings: changed.
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[12].body[2].body[2].body[1]; no call, error or mutation may be omitted. Condition: not changed
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[1].body[0]::Expr

Source: `infra/tests/test_destiny_recovery.py:46`; AST `44492395a70ec943ba62cbeabd7b9499eda9f94ee025f56841d2144884cdd743`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[1].body[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:46`; AST `60994c4f0287673782d785218262d99dfc49d082e5881f0166d83d76d75943f8`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.write_text.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[2].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[1].body[1]::Assign

Source: `infra/tests/test_destiny_recovery.py:47`; AST `055a1df3127077596db619aa0dc68b2016596d6a002355e3b181b0a0e09e23d5`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: changed.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[2].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[2]::Return

Source: `infra/tests/test_destiny_recovery.py:48`; AST `5f0e7cf654c605b9a956c53b166a617af6d35db0fc6ce66d479c39f799d76a6c`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: conclusion, dependencies, ledger, original, path. Outputs/bindings: (none).
Calls/effect boundaries: original.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[2].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::race::root.body[12].body[2].body[2].body[2].value::Call

Source: `infra/tests/test_destiny_recovery.py:48`; AST `67876dd717db8d1d75bcba5b7e0ba72dfd584bdea9b552550783fb959369e157`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: conclusion, dependencies, ledger, original, path. Outputs/bindings: (none).
Calls/effect boundaries: original.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[3]::Assign

Source: `infra/tests/test_destiny_recovery.py:50`; AST `66dc29c5c2723845191deadd367dfc18a95e97146126fc31fcde2a1e61f997e9`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SimpleNamespace. Outputs/bindings: args.
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[3].value::Call

Source: `infra/tests/test_destiny_recovery.py:50`; AST `347a089aaf79ec600f48e2155e257566c5a4b6a30926f00eb6dba633bf4e4d42`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SimpleNamespace. Outputs/bindings: (none).
Calls/effect boundaries: SimpleNamespace.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4]::With

Source: `infra/tests/test_destiny_recovery.py:51`; AST `62c9db336bf54b43af10c3d6f4cc6536dd78b0c3817f4b9688152bd0a53428c3`.

Rust module: `infra::tests::test_destiny_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContextLedger, RuntimeError, args, context, load_profile, patch, race, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile, patch.object, self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].items[0].context_expr::Call

Source: `infra/tests/test_destiny_recovery.py:51`; AST `c32c99ba8ef717ba0ee4cbc71115afc691c2614b4cec0312dd6b8ae7b86ba851`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextLedger, patch, race. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].body[0]::With

Source: `infra/tests/test_destiny_recovery.py:52`; AST `b98e9330c3a34b0b6175e10a6140544bd8714774745ec449d7b495c16c8f4d28`.

Rust module: `infra::tests::test_destiny_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: RuntimeError, args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile, self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].body[0].items[0].context_expr::Call

Source: `infra/tests/test_destiny_recovery.py:52`; AST `c0767606b16c4b3f044976bdc3b943f5a9a180108e07f10b0c3a1a6b8a6bb95f`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[4].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].body[0].body[0]::Expr

Source: `infra/tests/test_destiny_recovery.py:53`; AST `6e4d2e9d22d7bc49db5933a484bad2edbd845acc0f2b6ac62b010407c318e1fb`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].body[0].body[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:53`; AST `594c30f0ef8381580aa396a546b0104e9e10d2cdae488dca76d4ba7adbcd17f5`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[4].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[4].body[0].body[0].value.args[1]::Call

Source: `infra/tests/test_destiny_recovery.py:53`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[4].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[5]::Expr

Source: `infra/tests/test_destiny_recovery.py:54`; AST `90500ffa5a2232eb59b00a0b809d5d4bd6a8730620aa6922b44c3eed8ca15570`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[5].value::Call

Source: `infra/tests/test_destiny_recovery.py:54`; AST `e003605693ad7866df31c5108058fd0ce544de2833a3beeba8d503037f890500`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile, self.assertEqual.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[5].value.args[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:54`; AST `594c30f0ef8381580aa396a546b0104e9e10d2cdae488dca76d4ba7adbcd17f5`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, context, load_profile, self. Outputs/bindings: (none).
Calls/effect boundaries: context, load_profile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::TestDestinyRecovery::test_no_unchanged_claim_after_a_context_read_race::root.body[12].body[2].body[5].value.args[0].value.args[1]::Call

Source: `infra/tests/test_destiny_recovery.py:54`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[5].value.args[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[13]::If

Source: `infra/tests/test_destiny_recovery.py:57`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_destiny_recovery`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_destiny_recovery.py:58`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_destiny_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_destiny_recovery.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_destiny_recovery.py:58`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_destiny_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.context_cache, agentinfra.destiny, json, pathlib, subprocess, sys, test_destiny, types, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
