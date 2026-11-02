# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 106. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_coverage.py::module::root::Module

Source: `infra/tests/test_coverage.py:1`; AST `0d1bdb22a51b519dba0250f6419929a5022f9e26a3d33592c7bb44b4d50bb4c3`.

Rust module: `infra::tests::test_coverage`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, __file__, __name__, any, assurance, entry, helper, kind, levels, manifest, name, proof, proofs, self, status, str, sys, unittest. Outputs/bindings: helper, levels, name, proof, proofs.
Calls/effect boundaries: Path, Path(__file__).resolve, any, assurance, assurance(None, [self.proof('proofs::a')]).values, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, entry.split, proof['assertion_properties'].append, self.assertFalse, self.assertTrue, self.proof, self.record['required_obligations']['spec_proved'][1]['assertion_properties'].append, str, sys.path.insert, unittest.main.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[0]::Expr

Source: `infra/tests/test_coverage.py:1`; AST `5c991d2c6a93bfe384e1a7d21655e7dae01ccd13d3daa27e017695ba72452599`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_coverage.py:2`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[2]::Import

Source: `infra/tests/test_coverage.py:3`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[3]::Import

Source: `infra/tests/test_coverage.py:4`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[4]::Expr

Source: `infra/tests/test_coverage.py:6`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[4].value::Call

Source: `infra/tests/test_coverage.py:6`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[4].value.args[1]::Call

Source: `infra/tests/test_coverage.py:6`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[4].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_coverage.py:6`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[4].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_coverage.py:6`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[4].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_coverage.py:7`; AST `e83e530603c0e175aaa8faba4e7c4deca5aa0c1ce140792d0d5e50542b3fbb93`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::root.body[6]::ClassDef

Source: `infra/tests/test_coverage.py:10`; AST `b12d351ee26551ed44414e1b9051d862eb07a3aedeae949a584a20121b448e60`.

Rust module: `infra::tests::test_coverage`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: any, assurance, entry, helper, kind, levels, manifest, name, proof, proofs, self, status, unittest. Outputs/bindings: helper, levels, name, proof, proofs.
Calls/effect boundaries: any, assurance, assurance(None, [self.proof('proofs::a')]).values, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, entry.split, proof['assertion_properties'].append, self.assertFalse, self.assertTrue, self.proof, self.record['required_obligations']['spec_proved'][1]['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::setUp::root.body[6].body[0]::FunctionDef

Source: `infra/tests/test_coverage.py:11`; AST `57a4089a3e4abf851512cd52972ab322d22e23c0817fb59e90f0360fab6e2205`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::setUp::root.body[6].body[0].body[0]::Assign

Source: `infra/tests/test_coverage.py:12`; AST `d37dc357d3f78b2a3a958cd8d9fc701471802ef786ca6ec2964a66d7ccf76bf3`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::proof::root.body[6].body[1]::FunctionDef

Source: `infra/tests/test_coverage.py:17`; AST `87549a17d84f3920d69689fe4d68e8922ab9ec295d9842e1d2e38c608e568a29`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: entry, kind, manifest, name, status. Outputs/bindings: name.
Calls/effect boundaries: entry.split.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::proof::root.body[6].body[1].body[0]::Assign

Source: `infra/tests/test_coverage.py:18`; AST `22c2fa9f624a5bd8d13393fd8fc9ad3ecbdf4bc819204c5c89865621648074df`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: name.
Calls/effect boundaries: entry.split.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::proof::root.body[6].body[1].body[0].value.value::Call

Source: `infra/tests/test_coverage.py:18`; AST `e62de9b44997fc5c5ed15d825e1ffef0e76b9f75ef9bb80fa22d4c865d0f3439`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.split.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[1].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::proof::root.body[6].body[1].body[1]::Return

Source: `infra/tests/test_coverage.py:19`; AST `61b35e0aceed320d87955c0b64858f6edb5f1a4b18576dd757612491eae97818`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, kind, manifest, name, status. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Return evaluation at root.body[6].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2]::FunctionDef

Source: `infra/tests/test_coverage.py:22`; AST `5d353a47f632ea653ef6cf8a3d353357ffc58a2203d8dad51b52a52ed0209bc7`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: assurance, proof, self. Outputs/bindings: proof.
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[0]::Assign

Source: `infra/tests/test_coverage.py:23`; AST `ba2b353b2b48e244ad3ec19b57fc3aac25634bb38dff20089b0fd1231149e50d`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: proof.
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[0].value::Call

Source: `infra/tests/test_coverage.py:23`; AST `6bb2977f8236a6b4eee4b3c1439e37ff4e3990f442f5b7db5d7a1d3d9afef5ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[1]::Assign

Source: `infra/tests/test_coverage.py:24`; AST `1b438a2186d6435a56afc6222c3176945a119a9d44172f13e3d51c270ac29dec`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[2]::Expr

Source: `infra/tests/test_coverage.py:25`; AST `2b6a76c728273550c834712e11b0f0410423cbba6913df4a6a23cc839ed6a768`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[2].value::Call

Source: `infra/tests/test_coverage.py:25`; AST `70f23a418514424c24ff394232383929875f23fcb84d178aafb17805652011ac`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[2].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:25`; AST `7d078ce140d5027de658ced6fc4f6670810f5b728d5aeaa68ea0a077c283798b`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[2].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_partial_assertion_list_does_not_discharge_a_whole_harness_requirement::root.body[6].body[2].body[2].value.args[0].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:25`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[2].body[2].value.args[0].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_one_success_does_not_discharge_two_assertion_obligations::root.body[6].body[3]::FunctionDef

Source: `infra/tests/test_coverage.py:27`; AST `0f719eef5523b5c69bdb988767c2294e9271185d0b2230b086e010dc543a682f`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_one_success_does_not_discharge_two_assertion_obligations::root.body[6].body[3].body[0]::Expr

Source: `infra/tests/test_coverage.py:28`; AST `c4ed8c9d3afaf572a37e7133c169d70fc9860b3fbb4e23d8c4e1f82175009ca0`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_one_success_does_not_discharge_two_assertion_obligations::root.body[6].body[3].body[0].value::Call

Source: `infra/tests/test_coverage.py:28`; AST `06af229836038de747e399050d914fabef299df516f739eb41cb3fd8a4f2de01`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_one_success_does_not_discharge_two_assertion_obligations::root.body[6].body[3].body[0].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:28`; AST `4fc33038d88a93f585a05481fa4fbc3b5a2f64221456bcf7d0fcccc1de722da3`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_one_success_does_not_discharge_two_assertion_obligations::root.body[6].body[3].body[0].value.args[0].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:28`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[3].body[0].value.args[0].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4]::FunctionDef

Source: `infra/tests/test_coverage.py:30`; AST `de8d59a39a58f9b80bcb073f176c1a4b0c4efb4857a50e207f0c754273f59b64`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: assurance, levels, proof, self. Outputs/bindings: levels, proof.
Calls/effect boundaries: assurance, self.assertFalse, self.assertTrue, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[0]::Assign

Source: `infra/tests/test_coverage.py:31`; AST `feb8a16bf70688881fe07d94c55eeebdeb05611eacaee4670ed4daa000c7f4bc`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: proof.
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[0].value::Call

Source: `infra/tests/test_coverage.py:31`; AST `fe4091b5d02d316aec8a8c1bbf16ccf9ad1eb9ac03fc1f4f292d0c6d51afd88d`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[1]::Expr

Source: `infra/tests/test_coverage.py:32`; AST `caa9db74e535165dc6c7b8dc8284fa62f0bd37811cb5df58d1b137995f396788`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[1].value::Call

Source: `infra/tests/test_coverage.py:32`; AST `5c08abb9d84444e39c8c86618a62ad7d4ccb2a0f207b9e63db81caa6ba2df6d8`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[1].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:32`; AST `dd009e3fc47d7832451a993e413e8bbcf58b73d3c16d676b7b4ddb8ffa7b1c75`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[2]::Assign

Source: `infra/tests/test_coverage.py:33`; AST `181de0d6c1f0fda18d2c2b93d8b51430407a877abd8ed7827ba328e40d13ad25`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[3]::Assign

Source: `infra/tests/test_coverage.py:35`; AST `b5c9ed81a842fe31be0fb5f940c41a0c2799e9e8021d716f44577b85f41abc95`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proof, self. Outputs/bindings: levels.
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[3].value::Call

Source: `infra/tests/test_coverage.py:35`; AST `df6c4b6275e4071a38c713ca98e8e8c8bc8c43b4f8316a9fdc0306b2b607e84a`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[3].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:35`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[3].value.args[1].elts[1]::Call

Source: `infra/tests/test_coverage.py:35`; AST `6bb2977f8236a6b4eee4b3c1439e37ff4e3990f442f5b7db5d7a1d3d9afef5ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[3].value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[4]::Expr

Source: `infra/tests/test_coverage.py:36`; AST `4bef04dbc64a65c8ca1c9150ca61e9b2a808c42275012d835dfe47db729a6a2c`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: levels, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[4].value::Call

Source: `infra/tests/test_coverage.py:36`; AST `3847a739a4a3edcf32f9e4f3e695b75204ccedc2af8b9b252ef77a02c28a03c6`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: levels, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[5]::Expr

Source: `infra/tests/test_coverage.py:37`; AST `214e8b9f9e3d5c48077d890e4eb0daae9f3a82f7f8b359276237fcf66c565d2d`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: levels, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[5].value::Call

Source: `infra/tests/test_coverage.py:37`; AST `66fcefd19e0fe0ce897fa9a4b8ed2d35c29facb87904d0db64187093ca497310`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: levels, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[6]::Expr

Source: `infra/tests/test_coverage.py:38`; AST `18d48bea3f797094d73db9aa06f7c25f7ad5bb3552fdc1f041c04986cad01102`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[6].value::Call

Source: `infra/tests/test_coverage.py:38`; AST `bf2af176b5481686327f9a4fd4ad3ec90cadca5625f996d36b7786f8776e0139`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[6].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:38`; AST `c3ea39fee040f13947e7d6b98ce45b6718397e189eb0b1a20a1dd444617334ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[6].value.args[0].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:38`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[6].value.args[0].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_proved_kernel_retains_unproved_wrapper_correspondence::root.body[6].body[4].body[6].value.args[0].value.args[1].elts[1]::Call

Source: `infra/tests/test_coverage.py:38`; AST `6bb2977f8236a6b4eee4b3c1439e37ff4e3990f442f5b7db5d7a1d3d9afef5ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[4].body[6].value.args[0].value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5]::FunctionDef

Source: `infra/tests/test_coverage.py:40`; AST `8652823a0a4b6839817b2bb531d8ed15d14b19e3ae8a367ec6ee7e4f37b7f997`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: assurance, proof, self. Outputs/bindings: proof.
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0]::For

Source: `infra/tests/test_coverage.py:41`; AST `6fe5c897310821c9faa836b84f21eeb4a26f297c6eec800cadc120de97cb4f61`.

Rust module: `infra::tests::test_coverage`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: assurance, proof, self. Outputs/bindings: proof.
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered For evaluation at root.body[6].body[5].body[0]; no call, error or mutation may be omitted. Iteration: proof in (self.proof('proofs::b', status='STALE_SOURCE'), self.proof('proofs::b', manifest='other/Cargo.toml'), self.proof('proofs::b', kind='production_rust_refinement_proved'))
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].iter.elts[0]::Call

Source: `infra/tests/test_coverage.py:41`; AST `546b7e720418d4ba4c9d3e6b0622f23953e7e1a10b196371a73b64e8c1446d25`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].iter.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].iter.elts[1]::Call

Source: `infra/tests/test_coverage.py:42`; AST `b0bc7a934a68fa38a34972bd6b428467a9397ef9a54b6f6bddb94d61a16d1cfe`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].iter.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].iter.elts[2]::Call

Source: `infra/tests/test_coverage.py:43`; AST `f69fec5c6020575a9f1acec14964355c08a9453c47e6a46a852e7c731706981d`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].iter.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].body[0]::Expr

Source: `infra/tests/test_coverage.py:44`; AST `2b6a76c728273550c834712e11b0f0410423cbba6913df4a6a23cc839ed6a768`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_coverage.py:44`; AST `70f23a418514424c24ff394232383929875f23fcb84d178aafb17805652011ac`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].body[0].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:44`; AST `7d078ce140d5027de658ced6fc4f6670810f5b728d5aeaa68ea0a077c283798b`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proof, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_stale_wrong_manifest_or_wrong_lane_does_not_discharge_requirement::root.body[6].body[5].body[0].body[0].value.args[0].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:44`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[5].body[0].body[0].value.args[0].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6]::FunctionDef

Source: `infra/tests/test_coverage.py:46`; AST `abc4fad5aa20e361fa6439ba0be7880adf18753e920cb2753c6b76d042c742db`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(None, [self.proof('proofs::a')]).values, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0]::Expr

Source: `infra/tests/test_coverage.py:47`; AST `def4aeb4de435b8d68825b1f45cc3a44edf5b76dadee42fa94d6f9045a261fd0`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(None, [self.proof('proofs::a')]).values, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0].value::Call

Source: `infra/tests/test_coverage.py:47`; AST `5b4e0d95c06e60636aa0d0cdf16ef6f157159dd018eae22a5b2db35f828f8029`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(None, [self.proof('proofs::a')]).values, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0].value.args[0]::Call

Source: `infra/tests/test_coverage.py:47`; AST `5dd2c1e7e14bddfe107895bcee84484332b0ae86a90027888b27dc6ec65235aa`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(None, [self.proof('proofs::a')]).values, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0].value.args[0].args[0]::Call

Source: `infra/tests/test_coverage.py:47`; AST `da0d52d69ba24128a795531c3a123d699cee2478bcb0a93dbae087e622b3428c`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, assurance(None, [self.proof('proofs::a')]).values, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[0].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0].value.args[0].args[0].func.value::Call

Source: `infra/tests/test_coverage.py:47`; AST `7c8a3282988a35eb8c22cf60cf99d159a56302518789b7687abf8ab93d10a023`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[0].value.args[0].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[0].value.args[0].args[0].func.value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:47`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[0].value.args[0].args[0].func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[1]::Assign

Source: `infra/tests/test_coverage.py:48`; AST `280adae331c39faedd45d5e2f3525b0a637f8e3169c768683592e961ef4562c3`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2]::Expr

Source: `infra/tests/test_coverage.py:49`; AST `8469c74d72de39c66b71aeae3a26e6609c473d68406ca74c35a57fa0144f4408`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value::Call

Source: `infra/tests/test_coverage.py:49`; AST `82dc02df768ff528d33ea935e97b8812738f1fc3da0d0464ff85c722eb6dbf59`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value.args[0]::Call

Source: `infra/tests/test_coverage.py:49`; AST `d6f093de016e5ec5d532349bb3739fd36ea67a87213f73b49b28567a5c1d7555`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: any, assurance, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value.args[0].args[0]::Call

Source: `infra/tests/test_coverage.py:49`; AST `168a3fe5d5f2182c36a31ce33e597a594d5e55368f65719ef891e2aea5620722`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, assurance(self.record, [self.proof('proofs::a'), self.proof('proofs::b')]).values, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value.args[0].args[0].func.value::Call

Source: `infra/tests/test_coverage.py:49`; AST `c3ea39fee040f13947e7d6b98ce45b6718397e189eb0b1a20a1dd444617334ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value.args[0].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value.args[0].args[0].func.value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:49`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value.args[0].args[0].func.value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[2].value.args[0].args[0].func.value.args[1].elts[1]::Call

Source: `infra/tests/test_coverage.py:49`; AST `6bb2977f8236a6b4eee4b3c1439e37ff4e3990f442f5b7db5d7a1d3d9afef5ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[2].value.args[0].args[0].func.value.args[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[3]::Assign

Source: `infra/tests/test_coverage.py:50`; AST `19ebd5c2d709a468447ff588cdd7453d36b25a71d7326abe0b55cc46537c687b`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[6].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[4]::Assign

Source: `infra/tests/test_coverage.py:51`; AST `db6cc746d08d366343651c2867c7a68ab91086255b10289bdd70bafe9afa9326`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[6].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[5]::Expr

Source: `infra/tests/test_coverage.py:52`; AST `c4ed8c9d3afaf572a37e7133c169d70fc9860b3fbb4e23d8c4e1f82175009ca0`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[6].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[5].value::Call

Source: `infra/tests/test_coverage.py:52`; AST `06af229836038de747e399050d914fabef299df516f739eb41cb3fd8a4f2de01`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[5].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:52`; AST `4fc33038d88a93f585a05481fa4fbc3b5a2f64221456bcf7d0fcccc1de722da3`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_review_and_nonempty_requirements_are_required::root.body[6].body[6].body[5].value.args[0].value.args[1].elts[0]::Call

Source: `infra/tests/test_coverage.py:52`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[6].body[5].value.args[0].value.args[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7]::FunctionDef

Source: `infra/tests/test_coverage.py:54`; AST `49d6e466ae21f24f07cac9f712df090e3a37a7f4800408f323033575d29cc3dd`.

Rust module: `infra::tests::test_coverage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: assurance, helper, proof, proofs, self. Outputs/bindings: helper, proof, proofs.
Calls/effect boundaries: assurance, proof['assertion_properties'].append, self.assertFalse, self.assertTrue, self.proof, self.record['required_obligations']['spec_proved'][1]['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[6].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[0]::Assign

Source: `infra/tests/test_coverage.py:55`; AST `e772583c9a003c4510645f316f766e701a03809ac5739ceb832c59ffac7c9f2d`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: helper.
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[1]::Expr

Source: `infra/tests/test_coverage.py:56`; AST `90ce6e63d672680d2b01e80230a25eb55a7e52edf44544dc1652dc8f38b7c66c`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: helper, self. Outputs/bindings: (none).
Calls/effect boundaries: self.record['required_obligations']['spec_proved'][1]['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[1].value::Call

Source: `infra/tests/test_coverage.py:56`; AST `aeb68a1dbaf1c212a056c26a8fea244075d364397d21c7dbd481b6a77f13a18d`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: helper, self. Outputs/bindings: (none).
Calls/effect boundaries: self.record['required_obligations']['spec_proved'][1]['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[2]::Assign

Source: `infra/tests/test_coverage.py:57`; AST `81fc2b294d448cb9e1fe523ddcd7b51b6a79dde83613f7ad77b8fe716507817b`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: helper, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[3]::Assign

Source: `infra/tests/test_coverage.py:60`; AST `ba2b353b2b48e244ad3ec19b57fc3aac25634bb38dff20089b0fd1231149e50d`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: proof.
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[3].value::Call

Source: `infra/tests/test_coverage.py:60`; AST `6bb2977f8236a6b4eee4b3c1439e37ff4e3990f442f5b7db5d7a1d3d9afef5ec`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[4]::Expr

Source: `infra/tests/test_coverage.py:61`; AST `a6b1ecdb7d4930eb03446d82d32f8aa2f87b37afd15f1ffd7f95a78e9eb61bfb`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: helper, proof. Outputs/bindings: (none).
Calls/effect boundaries: proof['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[4].value::Call

Source: `infra/tests/test_coverage.py:61`; AST `c3fee3262faed6e00807afc4a1409be20ed7f08f285a436061701a16374e2ff6`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: helper, proof. Outputs/bindings: (none).
Calls/effect boundaries: proof['assertion_properties'].append.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[5]::Assign

Source: `infra/tests/test_coverage.py:62`; AST `d05d43806221b755aabeae38b755b805148c31a17f51f143e44248a8d4a33f21`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: proof, self. Outputs/bindings: proofs.
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[5].value.elts[0]::Call

Source: `infra/tests/test_coverage.py:62`; AST `f901f836e9894f607ad8f66d2fce27ef22a0bbc6c8e1951573eb850840ad9d19`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.proof.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[5].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[6]::Expr

Source: `infra/tests/test_coverage.py:63`; AST `86f1e29ba5dd6edf01ebdaeca4ecc29e699ff486472c4a36883807a00b05f52b`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[6].value::Call

Source: `infra/tests/test_coverage.py:63`; AST `a39ff749487aa89fa0059e874e514e48b6eba855ab6588cfc0b474ae949b97b9`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[6].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:63`; AST `01d344aabd39fa92377143778888017242ea8ad5cc3056e6e9ddde50b34b3426`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[7]::Assign

Source: `infra/tests/test_coverage.py:64`; AST `9625ca402ca10e8c818c0df566aaa0ed033265adbecd8a6c88945dd8a63252af`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: helper, proof. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[8]::Expr

Source: `infra/tests/test_coverage.py:65`; AST `66234f421a75ead4459c63a09c25a1a0d41068ff3821e402f7e7dfbc98469040`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[8].value::Call

Source: `infra/tests/test_coverage.py:65`; AST `a3730cc1bdf13a717a6f86c72403f8e678ec8b349c00af5db7d46de957f6b987`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertTrue.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[8].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:65`; AST `01d344aabd39fa92377143778888017242ea8ad5cc3056e6e9ddde50b34b3426`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[8].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[9]::Assign

Source: `infra/tests/test_coverage.py:66`; AST `e4066a63d38bccca6db32b147764608a41a3823196d28d5a3a8d15eebb5065bd`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: helper, proof. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6].body[7].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[10]::Expr

Source: `infra/tests/test_coverage.py:67`; AST `86f1e29ba5dd6edf01ebdaeca4ecc29e699ff486472c4a36883807a00b05f52b`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[6].body[7].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[10].value::Call

Source: `infra/tests/test_coverage.py:67`; AST `a39ff749487aa89fa0059e874e514e48b6eba855ab6588cfc0b474ae949b97b9`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance, self.assertFalse.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::TestCaseConjunction::test_shared_helper_property_needs_its_exact_observed_location::root.body[6].body[7].body[10].value.args[0].value::Call

Source: `infra/tests/test_coverage.py:67`; AST `01d344aabd39fa92377143778888017242ea8ad5cc3056e6e9ddde50b34b3426`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: assurance, proofs, self. Outputs/bindings: (none).
Calls/effect boundaries: assurance.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].body[7].body[10].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[7]::If

Source: `infra/tests/test_coverage.py:70`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_coverage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered If evaluation at root.body[7]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[7].body[0]::Expr

Source: `infra/tests/test_coverage.py:71`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_coverage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_coverage.py::module::root.body[7].body[0].value::Call

Source: `infra/tests/test_coverage.py:71`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_coverage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.coverage, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
