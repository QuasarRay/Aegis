# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 111. Inventory digest: `7d3dd696acbae6c553ff4906d6c68fef1bbb7240e52ca0e0e9e52c95acabc54f`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_native_read_recovery.py::module::root::Module

Source: `infra/tests/test_roadmap_native_read_recovery.py:1`; AST `e9525f4d73ececd65546ca2ce9f9f7dfbedfb0b3c59f75a99694eddacd9edc72`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, RetainedNativeExecutableTests, _read_transport_binding, before, binding, cases, copy, dict, digest, k, native, patch, pin, result, route, self, unittest, v. Outputs/bindings: before, binding, cases, k, native, pin, result, route, v.
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes, RetainedNativeExecutableTests, _read_transport_binding, cases.append, copy.deepcopy, dict, digest, native.items, native.pop, patch, pin.assert_called_once_with, self.addCleanup, self.assertEqual, self.assertIsNone, self.assertNotEqual, self.assertRaisesRegex, self.bind, self.fixture.retained, self.fixture.schema.write_text, self.fixture.setUp, self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:1`; AST `6c1600ee7a38d612b5dd639a76968568adf806c3852319179fd4006d38e89090`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_native_read_recovery.py:5`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_native_read_recovery.py:7`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_native_read_recovery.py:8`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_roadmap_native_read_recovery.py:9`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_roadmap_native_read_recovery.py:11`; AST `3c01f566fbf689933c74d9857892f944616fc795472c042b71960b3f843dff33`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_native_read_recovery.py:12`; AST `5b90894d096758c9f19f8600da372bc7cd3d8c63d0642e575f9761c8cc9880e1`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::root.body[7]::ClassDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:15`; AST `90ea3572a21a23b5f39df3040db0521b1df71d172c8a2b304048ff6e435c8645`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, RetainedNativeExecutableTests, _read_transport_binding, before, binding, cases, copy, dict, digest, k, native, patch, pin, result, route, self, unittest, v. Outputs/bindings: before, binding, cases, k, native, pin, result, route, v.
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes, RetainedNativeExecutableTests, _read_transport_binding, cases.append, copy.deepcopy, dict, digest, native.items, native.pop, patch, pin.assert_called_once_with, self.addCleanup, self.assertEqual, self.assertIsNone, self.assertNotEqual, self.assertRaisesRegex, self.bind, self.fixture.retained, self.fixture.schema.write_text, self.fixture.setUp, self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:16`; AST `53a3efd3384842845b26ca0561259946b66f8574508e26b159cc745902c8eac6`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: RetainedNativeExecutableTests, route, self. Outputs/bindings: route.
Calls/effect boundaries: RetainedNativeExecutableTests, self.addCleanup, self.fixture.retained, self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[0]::ImportFrom

Source: `infra/tests/test_roadmap_native_read_recovery.py:17`; AST `837d2f086a0cc4643afc30e4664ef2c4d8770327ff82e0fea015e48923193a48`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:18`; AST `2fbb1e88f125e8c429062e79ad5d7a4d2e293433f20681459810d4fd24d3be1b`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RetainedNativeExecutableTests, self. Outputs/bindings: (none).
Calls/effect boundaries: RetainedNativeExecutableTests.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:18`; AST `1e4f96210c9b596bd2b00d56cf42cf4372cd64473553ff087f6f1e102122710a`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RetainedNativeExecutableTests. Outputs/bindings: (none).
Calls/effect boundaries: RetainedNativeExecutableTests.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:19`; AST `b4195e7a806d59e33ddad497d89ed91aad1ad58098dbab110d42413c50b08654`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:19`; AST `50cff38fab903a202c80c0638fc0d6a67d5df57c13482f23bcdfcc3ebd759abf`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:20`; AST `019742c921d075c854a0df8fcd287403e57b287b08e19edaf6c9c0d356237f76`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:20`; AST `4fe535711da5742f8af1931193de050679474b7c3c7751171ee62bff00f7067c`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:21`; AST `5127d8056d640914446fa334ff4a70d9f92f81e009fef00f785c5154085e7fa4`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:22`; AST `67215cbf1bd92a20d6a9c4fae03f575c7e9aae0a824a9e72d4b569fe02598656`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: route.
Calls/effect boundaries: self.fixture.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:22`; AST `4f4a9986d8518c51ae4e119c0528f3f0a06c9ef903aff591d9a122bb117f6c91`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.retained.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::setUp::root.body[7].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:23`; AST `9fc4687b669c5cf24e5adbac137faccf4f8a0899ed937e828c8e16245b5a21a3`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: route, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:29`; AST `0b6224b36c284616eb66277bfe9e6e45698a02c9d528d4b304bc0f8f8e6764b8`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _read_transport_binding, copy, digest, k, native, patch, pin, result, self, v. Outputs/bindings: k, native, pin, result, v.
Calls/effect boundaries: _read_transport_binding, copy.deepcopy, digest, native.items, patch, pin.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:30`; AST `51a3bc10498468757f59a54a1b994a0c76419c823321ea1bf79ad42c859ef31b`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, native, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:30`; AST `8718e8c3729c3b0ae7f6101e003926ee7604c6565b25e4d4568a39ea778cb5a4`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, native, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:31`; AST `9d2f9916952ef6febad127045f9ef68597de2d0f5d4bc856056d306ba94c0b65`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, k, native, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, native.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:31`; AST `746477270432ea69e88d8bc0398d284527a42415543e2c9a4b77b6bb2b0c47c1`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, k, native, v. Outputs/bindings: k, v.
Calls/effect boundaries: digest, native.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[1].value.args[0]::DictComp

Source: `infra/tests/test_roadmap_native_read_recovery.py:31`; AST `c4ab865b698189f955129ef5d368e4b192e7631a22c8cf0b354eb990c575ce3f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, native, v. Outputs/bindings: k, v.
Calls/effect boundaries: native.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[7].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[1].value.args[0].generators[0].iter::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:31`; AST `a9ffbecf33d857257393650e6ed0349b2d9bfb11cd5512fc06ee10593803d9fd`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: native.items.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[1].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[2]::With

Source: `infra/tests/test_roadmap_native_read_recovery.py:32`; AST `efc5fc769cf331a0ce0ea7f1c5fd125bd2525920d692b639c3df2cc899851b3c`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: _read_transport_binding, native, patch, self. Outputs/bindings: pin, result.
Calls/effect boundaries: _read_transport_binding, patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:32`; AST `dc58eb901a49c924f2134de7fa1cd71d355b06363cb8cd3d355f07d78de31924`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:33`; AST `5009541a42600f8bb385aabd2b5bdebc406181f75ef17a76b377c31bbf565216`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _read_transport_binding, native, self. Outputs/bindings: result.
Calls/effect boundaries: _read_transport_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:33`; AST `a51c9ea7e640ee9c850e0c7effa0ecbeba44a6de9fdaa7d7eb3f8c2cd879c4e0`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read_transport_binding, native, self. Outputs/bindings: (none).
Calls/effect boundaries: _read_transport_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:34`; AST `2c267d92c4aff9ad67a78c2bce6b9793c904bc8d9d6c2602b4f27ec70cd7851e`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pin, self. Outputs/bindings: (none).
Calls/effect boundaries: pin.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:34`; AST `766eb5ce9952d101682e9b0c17b5bf535afba16f8c94fa1561fb2aba10f257fc`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pin, self. Outputs/bindings: (none).
Calls/effect boundaries: pin.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::bind::root.body[7].body[1].body[4]::Return

Source: `infra/tests/test_roadmap_native_read_recovery.py:35`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[7].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:37`; AST `c8ad1c774ff8ba3010ffc1429f314892b4623273711589b9bee20e46bff325d6`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: before, binding, self. Outputs/bindings: before, binding.
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes, self.assertEqual, self.assertNotEqual, self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:38`; AST `ee5fade873c3e280b3edc33d6c0729ad7e212bf474f5331ff6cd4e24dde18f5f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: before.
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:38`; AST `ee9bd83bd2457165072088af4db98e55530daec5cb406de2ce8bf05dbfc518d7`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[1]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:39`; AST `5347d49caa2060c4476177589750a63e615fe9a84f634832d7f28f88f4345fd3`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: binding.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:39`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:40`; AST `0a1ee1a804f0f8a836b1194d2c19053bb7a1ef047e797e45b48e0395af280267`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:40`; AST `a75b5b05de8115bd3321d928f8bace7a55bfe960a0e7ee55a5b7bf81e7ace32c`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:41`; AST `e060a10e2a2b1654600b506e6e6519faedbe82303e84c783f4429cb14b2f336d`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:41`; AST `2284182cf377664ac5890ff13580ef4cc19a546d1b62bdfd850d94622d4c0fd7`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[4]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:42`; AST `16652044195cc38e24a646544a51075b6037dfe49813e0f7eff38844f2308bff`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:42`; AST `25ee16c2082a838c2171df3c3b9137c419e3341643a169f7a4574a54aec7c0b1`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[5]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:43`; AST `fa350b547bc0d1f5b6a9f750438a06f0baaf37a3945e4188a776ca4c7d0c92d3`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[5].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:43`; AST `ec857d258c0b8a0b63f3d124e4e25d062b1ee755d034431cf3f4d3d16e2449d5`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[6]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:44`; AST `dc5f31cab4aa9d521218335deaee8b76021be4898f44202eaef779aa60ed0f5b`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[2].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[6].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:44`; AST `b8c2608f3c33f2328a5af53abcae58623d9429151187c52bc7a3a32a990cdf51`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, self. Outputs/bindings: (none).
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_installed_reader_and_retained_host_keep_both_exact_pins_and_canonical_bytes::root.body[7].body[2].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:44`; AST `ee9bd83bd2457165072088af4db98e55530daec5cb406de2ce8bf05dbfc518d7`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.fixture.root / '.aegis/project.json').read_bytes.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[2].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:46`; AST `6068988409d7b8ccf5d6ef0ff9e13f8b93cc2987864a0f634dc806a411464c3f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: binding, dict, native, self. Outputs/bindings: binding, native.
Calls/effect boundaries: dict, native.pop, self.assertEqual, self.assertIsNone, self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:47`; AST `8af8e96890874e3145b58ae3704bef6da48e601da934aa64d96af06036388a94`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: native.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:47`; AST `b53106a2a907271d5718153a8134c459f6cd024cf7dc901a0f6611b8161cc8d6`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:48`; AST `e507bc5e0576bcbd08a79d4cecedb7c60e9398329c133c59e708aca6c14ffff5`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: native.pop.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:48`; AST `702e5c37d86aa16201b035b67a2540c2d96a85e1ee5a9b1647711f58b955ac71`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: native.pop.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[2]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:49`; AST `f2e54ff7acadd2fac4278a840d6a7b926b09c24473b670ab0897bc6af9aa4d35`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native, self. Outputs/bindings: binding.
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[2].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:49`; AST `af2cf72070281beb33834f498babda05e4a0d6d2aad35def3ba82626913d4ec7`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:50`; AST `60d6fe3c3541840730020ba95e500091637feb3f0f3a322dbb58a1501228a3ab`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:50`; AST `b0259892663e8ff84f774421352fbb0b67552180c2c40feddb2aca8bcd0fae2f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:51`; AST `b6effbe6db1cf8919d880626077eaa4eb32a7b15432b12103eb05bd3968c1058`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_same_installed_host_uses_its_exact_identity_without_a_retained_route::root.body[7].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:51`; AST `0d239b600052563bdf73ca2a588af6343e74e32cdbb33948f448a5e93dd51ab4`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertIsNone.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:53`; AST `8d0ed8d65ab8adcb461e23618e7684d19654e9aaa8c46edee4e84064d9db8889`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, cases, copy, native, self. Outputs/bindings: cases, native.
Calls/effect boundaries: cases.append, copy.deepcopy, native.pop, self.assertRaisesRegex, self.bind, self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:54`; AST `94b78388342bce9ce07ab9a0596bccbbeba71dfca30933684a6682ceab121dc3`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: cases.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[1]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `e507bc5e0576bcbd08a79d4cecedb7c60e9398329c133c59e708aca6c14ffff5`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: native.pop.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `702e5c37d86aa16201b035b67a2540c2d96a85e1ee5a9b1647711f58b955ac71`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: native.pop.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `c39f4a318f008ab71c49612a970989fac9b553110658f77b41f518e948035a78`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:55`; AST `1e9d0a63e6eda5ac83765268f9039290651c3f44b76b1755d0d2e94025f115ed`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[4]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:56`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:56`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[5]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:56`; AST `56c9fd72462d2df2545491e5f165885c6c04a9365528b270e5c9e3d21f6a5b10`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:56`; AST `c39f4a318f008ab71c49612a970989fac9b553110658f77b41f518e948035a78`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:56`; AST `1e9d0a63e6eda5ac83765268f9039290651c3f44b76b1755d0d2e94025f115ed`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[7]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:57`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[7].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:57`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[8]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:57`; AST `09c043a24d40c5dc9094af4562d0daa557645666f24680b255ae627ebc2fc161`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[8]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[9]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:57`; AST `c39f4a318f008ab71c49612a970989fac9b553110658f77b41f518e948035a78`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[9]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[9].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:57`; AST `1e9d0a63e6eda5ac83765268f9039290651c3f44b76b1755d0d2e94025f115ed`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[10]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:58`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[10]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[10].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:58`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[11]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:58`; AST `0edffec460a4675c075d81872f1f016df0b4c86d9d6918727cc32d0e4d100da4`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[11]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[12]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:58`; AST `c39f4a318f008ab71c49612a970989fac9b553110658f77b41f518e948035a78`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[12]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[12].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:58`; AST `1e9d0a63e6eda5ac83765268f9039290651c3f44b76b1755d0d2e94025f115ed`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[13]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:59`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[13]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[13].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:59`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[14]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:59`; AST `6cbca4de9690d2847b1cb67685507c371af3508b878268c16ac9696c6695bf24`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[4].body[14]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[15]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:59`; AST `c39f4a318f008ab71c49612a970989fac9b553110658f77b41f518e948035a78`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[15]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[15].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:59`; AST `1e9d0a63e6eda5ac83765268f9039290651c3f44b76b1755d0d2e94025f115ed`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cases, native. Outputs/bindings: (none).
Calls/effect boundaries: cases.append.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16]::For

Source: `infra/tests/test_roadmap_native_read_recovery.py:60`; AST `44970759f68f97c57a972ca497c4d37ede3c4b5f32e12c68ff6aad91b9410f50`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, cases, native, self. Outputs/bindings: native.
Calls/effect boundaries: self.assertRaisesRegex, self.bind, self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[7].body[4].body[16]; no call, error or mutation may be omitted. Iteration: native in cases
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16].body[0]::With

Source: `infra/tests/test_roadmap_native_read_recovery.py:61`; AST `c9a23e49d5d6d1136fcb29022a51cf5a66a70d875247df40eab853b2d7e17a6a`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, native, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.bind, self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[4].body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:61`; AST `99811ae389cdb93ec01cb5634c208b131391b57c0737556e23f5a3833a0eb385`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[16].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:61`; AST `3f2f171017bf69268a6fb0f1978ad9fadd22475503868952944bf2fea12cfcd6`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[16].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:62`; AST `1882d6591a0d91f9e5fdcbf34de2eb53394159efdc211d6f5f6558c2f5c4330c`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[4].body[16].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_unqualified_different_host_or_unrelated_path_cannot_supply_read_acceptance::root.body[7].body[4].body[16].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:62`; AST `af2cf72070281beb33834f498babda05e4a0d6d2aad35def3ba82626913d4ec7`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: native, self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[4].body[16].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_native_read_recovery.py:64`; AST `887afbb1f92ea25e8296777495348b8e2ffa7d8de9f8596f7c8adec42bc43b31`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, _read_transport_binding, copy, native, patch, self. Outputs/bindings: native.
Calls/effect boundaries: _read_transport_binding, copy.deepcopy, patch, self.assertRaisesRegex, self.bind, self.fixture.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:65`; AST `7007fafd264c414bfe8b4b2d51b88d4744d2336434830d04bacc4dbf354bfc6f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: native.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:65`; AST `7658ef012882d33a61dc2b0f4047e9ec03c933de11bcabc963b40fd9c985713f`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[1]::Assign

Source: `infra/tests/test_roadmap_native_read_recovery.py:65`; AST `3fe903cbd41edc88084cab4fe4a5d9625ec25a654eca032671e2a5b2589d8615`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: native. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[2]::With

Source: `infra/tests/test_roadmap_native_read_recovery.py:66`; AST `a72f570ec39a689398f2eb90571662852fc00fa442c27a0b7321985b0fc5cc61`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, _read_transport_binding, native, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: _read_transport_binding, patch, self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:66`; AST `dc58eb901a49c924f2134de7fa1cd71d355b06363cb8cd3d355f07d78de31924`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[2].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:66`; AST `f0be43b7298b69ff97116a9fcdf64ba1f2e9f677fbfa7af98380d58c02ee4160`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[2].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:67`; AST `b3afee75841bc29c9788191220e4ed2608f2bee41906a1ade7bd2f123f83b588`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _read_transport_binding, native, self. Outputs/bindings: (none).
Calls/effect boundaries: _read_transport_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:67`; AST `a51c9ea7e640ee9c850e0c7effa0ecbeba44a6de9fdaa7d7eb3f8c2cd879c4e0`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _read_transport_binding, native, self. Outputs/bindings: (none).
Calls/effect boundaries: _read_transport_binding.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[3]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:68`; AST `b1a75852db90196632b57baaac4023ee409124cc509ce0f739b811715ee62e66`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[3].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:68`; AST `7bdfa81b8ebeb6c1eb92531d8765081a9f703c9f821ff355e77e54933d550793`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.schema.write_text.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[4]::With

Source: `infra/tests/test_roadmap_native_read_recovery.py:69`; AST `c74769c031bae197cf34ab199132025a9e075e06de09e4b6945524f281f837af`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex, self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[4].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:69`; AST `7adbea6e4d6b3d227e1bb77ba266bd40040c472325614f4d7d849e3b75d73f2a`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[4].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[4].body[0]::Expr

Source: `infra/tests/test_roadmap_native_read_recovery.py:70`; AST `3c9693e6e99acaacd00c509d8b14a0a84cd6075e941268a3fb3d7695dd1cbe1b`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[5].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_native_read_recovery.py::module::NativeReadRecoveryTests::test_prior_pin_schema_tampering_and_changed_owned_observation_are_rejected::root.body[7].body[5].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_native_read_recovery.py:70`; AST `735b7360d145ba366767ccce397de4a2d2bcc81706701ddd788376f784a4a78d`.

Rust module: `infra::tests::test_roadmap_native_read_recovery`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.bind.
Dependencies: __future__, agentinfra.roadmap_native, agentinfra.roadmap_records, copy, test_roadmap_retained_native, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[5].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: standard Rust constructs; qualify external boundaries
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
