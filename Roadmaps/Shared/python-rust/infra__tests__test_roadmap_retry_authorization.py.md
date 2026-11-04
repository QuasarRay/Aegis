# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 166. Inventory digest: `832d25e61e159f94002a9d5308faf9b4d528dd8fde7cc263f9e3fd59e55ce94f`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_retry_authorization.py::module::root::Module

Source: `infra/tests/test_roadmap_retry_authorization.py:1`; AST `844e19829066a408fa4b0e8c881450e9eb0a8d00e1caf372ed83e35e07cd4281`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, FIELDS, WorkspaceLease, __name__, a, amendment, authorize_single_retry, changes, consumed, contextmanager, copy, dict, digest, expected_digest, f, file_binding, history, json, k, kwargs, later, later_spec, limits, mirror_support, patch, path, retry_limits, scenarios, self, source, spec, str, unchanged, unittest, user_authorized. Outputs/bindings: FIELDS, a, amendment, consumed, f, history, k, kwargs, later, later_spec, limits, path, scenarios, spec, unchanged.
Calls/effect boundaries: (f.root / 'later-spec.json').write_text, (f.root / 'pin.json').write_text, (f.root / 'spec.json').write_text, authorize_single_retry, copy.deepcopy, dict, digest, f.record.update, f.state, file_binding, json.dumps, mirror_support.RetryScopeTests, patch, patch.object, path.read_bytes, path.write_text, retry_limits, self.addCleanup, self.assertEqual, self.assertRaises, self.assertRaisesRegex, self.authorize, self.fixture.setUp, self.state, self.subTest, str, unittest.main.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:1`; AST `08346095342729515e3feefcc591e80194184e0ca7ab280fcc7bd4b23a1ffa30`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[2]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:4`; AST `a510406c1fa6f159ec004f4ead0d836747696bf4154e0a5daee8abdfbd9829f0`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_retry_authorization.py:5`; AST `33e554a09588607f47c37f53babe8c268271234110ee05725315e1f269aea608`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_retry_authorization.py:6`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_retry_authorization.py:7`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:8`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[7]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:10`; AST `7e9c3f5290a99e55259b83ed615988e11578a991178ada162c503777b0b68347`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:11`; AST `7903500660d6419532fb05d53920d5290554e3194c5894134211635fe8ad7cbf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_retry_authorization.py:12`; AST `dd38b0e37a4623507f82f9c55f2af1f45f0b51dbfe7252112a74b01b60dd59fa`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[10]::Import

Source: `infra/tests/test_roadmap_retry_authorization.py:13`; AST `36e094ecb2ba48db55b3ecc5a98be436670268bd7b8ab9111b5a1f8f0d9f8304`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[11]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:16`; AST `9a28acc4e4114d8b46a2fab72b65d7663799ccc06501c411dbb225e775cae991`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: FIELDS.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_retry_authorization.py:19`; AST `0c2972f22087710869c9877207183c09b87feca5c3a9be3585b3e464debb5198`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, FIELDS, WorkspaceLease, a, amendment, authorize_single_retry, changes, consumed, contextmanager, copy, dict, digest, expected_digest, f, file_binding, history, json, k, kwargs, later, later_spec, limits, mirror_support, patch, path, retry_limits, scenarios, self, source, spec, str, unchanged, unittest, user_authorized. Outputs/bindings: a, amendment, consumed, f, history, k, kwargs, later, later_spec, limits, path, scenarios, spec, unchanged.
Calls/effect boundaries: (f.root / 'later-spec.json').write_text, (f.root / 'pin.json').write_text, (f.root / 'spec.json').write_text, authorize_single_retry, copy.deepcopy, dict, digest, f.record.update, f.state, file_binding, json.dumps, mirror_support.RetryScopeTests, patch, patch.object, path.read_bytes, path.write_text, retry_limits, self.addCleanup, self.assertEqual, self.assertRaises, self.assertRaisesRegex, self.authorize, self.fixture.setUp, self.state, self.subTest, str.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:20`; AST `01bbb268b02ee34ce06813dcfb959e5c4dbe0b266296f07e43a75cdddb00d58b`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: a, copy, dict, digest, f, mirror_support, self, str. Outputs/bindings: a, f.
Calls/effect boundaries: copy.deepcopy, dict, digest, mirror_support.RetryScopeTests, self.addCleanup, self.fixture.setUp, str.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:21`; AST `39d6b89a97c1629bdaad9f65e414d85045515284fbcff90e55266a42d9d5815e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mirror_support, self. Outputs/bindings: (none).
Calls/effect boundaries: mirror_support.RetryScopeTests.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:21`; AST `bda9b07c51bc032fc8f34e063fa32c9a6744104bfcf98a296cf5d4bbcf838c8c`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mirror_support. Outputs/bindings: (none).
Calls/effect boundaries: mirror_support.RetryScopeTests.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:22`; AST `b4195e7a806d59e33ddad497d89ed91aad1ad58098dbab110d42413c50b08654`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:22`; AST `50cff38fab903a202c80c0638fc0d6a67d5df57c13482f23bcdfcc3ebd759abf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.fixture.setUp.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:23`; AST `019742c921d075c854a0df8fcd287403e57b287b08e19edaf6c9c0d356237f76`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:23`; AST `4fe535711da5742f8af1931193de050679474b7c3c7751171ee62bff00f7067c`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:24`; AST `3c30f78126eccd2f1016bf9f30cca06f629d6ac874dacdc1c8944b0ff48c1597`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:25`; AST `e0c2780f26aa20f0a9118a0b6bc37388c2d3d30b3321e1e8d5edee0837b8b7cf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, f, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:25`; AST `1006cc1894d0ce6001df8edba493e342af9b689499b10a63bbb63ea51ff105db`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, f, str. Outputs/bindings: (none).
Calls/effect boundaries: digest, str.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[4].value.args[0].values[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:25`; AST `9202beec4664d58c985966e51b90daa94b7b345831f69be192bfb1847d9b5d11`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[4].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:27`; AST `31e91a84a8ca78ec1bfccf5f366d4ad070d38392a3bec3c9811debe10ecdcd14`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:28`; AST `1f9d2d9a846fd0a68d276d6f754cec0e67bd6993fc3df7fd1326242e51a92593`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: a, dict, f, self. Outputs/bindings: a.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[6].value::ListComp

Source: `infra/tests/test_roadmap_retry_authorization.py:28`; AST `bcb70f75e709a427bf08d7207a392f47cac177dab9836906baa0d825c532b3bf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: a, dict, f. Outputs/bindings: a.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[6].value.elt::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:28`; AST `cf48dd11e222e75db06f72e1fbba5b6f752f09356445c038eb1a7fdd8ccd73f9`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: a, dict, f. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[7]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:29`; AST `42bc0783554fc0098abfe2ea3dcd9b7263480d6de3fc9cf3a4a466152d212931`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[7].value.elts[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:29`; AST `e18390867c05e6cda1cc4991ee6fa6d9fd60ea710630afed3120b34645c515b3`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[7].value.elts[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:30`; AST `3efba61973398150e09d6682eb4b1284f2d13826b7428d473339f44374564510`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[7].value.elts[2]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:31`; AST `2dbd05d3cc7cf56d62dd1d2137d7059218b949ae134cbaff4cd9fbe05f3b8113`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[7].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:33`; AST `64f9203f8e11bbf07ec637436c8f3539c2dc6bf9a6f0637c3b237171d6138479`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, f, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:33`; AST `002993f8b1a6928b3cc7a0f2bd417b9a9d41ec1b1143b186be98d2a578183fb6`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, f. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[9]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:34`; AST `0312989009ebcf0e8e9888048431e153a72bf912ad7e04447a1658ea4163a8c8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[10]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:35`; AST `d10d3d1507d42db7f58f48f55f84afaf899bd359ba5488aece68f04555972bfa`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::setUp::root.body[12].body[0].body[11]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:36`; AST `b1a9624f574563d18161fa0614d5013bb8627f962a4b4fd92cacb1dd47fb862d`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:40`; AST `19dd8860c09709b86d415afde2e4c35990e2b370a3ce7b170a016c0c46a33668`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: changes, digest, expected_digest, f, json, path, self. Outputs/bindings: f, path.
Calls/effect boundaries: digest, f.record.update, json.dumps, path.read_bytes, path.write_text, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:41`; AST `3c30f78126eccd2f1016bf9f30cca06f629d6ac874dacdc1c8944b0ff48c1597`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:42`; AST `425bf8c01255c117f66733a1abfc4d473be45a9b8fdd8c568cc0b19c4244a77f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:43`; AST `54072a178c6d70031ceec41d657148e346ac161adaefe305c4c6b3a4dee5b2f9`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, expected_digest, path, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:43`; AST `67295d28b29c352a574db6a0e81113158d96499044cec26674444bcc91408033`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, expected_digest, path, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[2].value.args[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:43`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[2].value.args[1].args[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:43`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[2].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[3]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:44`; AST `e3c5331e1ed87b603a11d33c0abd1205421e008f3de100ced813ef797612f73f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: changes, f. Outputs/bindings: (none).
Calls/effect boundaries: f.record.update.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:44`; AST `5d56ef53a645f841d707d62e449db68523ce77d1ad2f84b656006316d4e110f8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: changes, f. Outputs/bindings: (none).
Calls/effect boundaries: f.record.update.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[4]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:45`; AST `e90f160c7fccb003e8edb32bf3401850bdbd0a823594123437d4118c0227210a`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[4].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:45`; AST `8b00e905f0e746d23de30fa232c92b993f8dc4dd54ddc93c69615a83c293c503`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, json, path. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::save_record::root.body[12].body[1].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:45`; AST `e681dca2d22904e845d5479363acd46e65604b2bca63140f0c86ef7e137a84b5`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:48`; AST `86268bed256585a007643baaa76091ad5a38f4637dfd190512a93ea909f523f4`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: WorkspaceLease, contextmanager, f, history, patch, self. Outputs/bindings: f.
Calls/effect boundaries: f.state, patch, patch.object.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:49`; AST `3c30f78126eccd2f1016bf9f30cca06f629d6ac874dacdc1c8944b0ff48c1597`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:50`; AST `f953bfca0525441225d4468537a29e5b59bd28fca8883246331d9c27346c2514`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: WorkspaceLease, f, history, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: f.state, patch, patch.object.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:50`; AST `7e957f02bd54bedd66e4c81dab206cdb00f63f5e3633e584ffaa2991cc192b02`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, history. Outputs/bindings: (none).
Calls/effect boundaries: f.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:51`; AST `037b4cddac3035cc7fc93b435ca6a9f2d98e0f283d57896f90e8d17c86654f8f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: WorkspaceLease, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.object.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:52`; AST `858e340cfa4e5082dd2b9a03ba1811e1dd4f31d943aa818b40ab0a1dcaf36bbd`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1].items[3].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:53`; AST `cc9f5b7f5a5f5b8be925fcffdf68576e368df60a657c241b75eee18f268dcbc8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, self. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].items[3].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::state::root.body[12].body[2].body[1].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:54`; AST `4ef85b91bd2f837cbb619428370c77b4e8f23faa1461fa93120d8bde06a4c480`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::authorize::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:56`; AST `17c7ca51f3bdb269552eb12297eefa1fe99a00e3b9fd9618dd6c2e71c22d628d`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: authorize_single_retry, f, file_binding, self, source, user_authorized. Outputs/bindings: f.
Calls/effect boundaries: authorize_single_retry, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::authorize::root.body[12].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:57`; AST `3c30f78126eccd2f1016bf9f30cca06f629d6ac874dacdc1c8944b0ff48c1597`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::authorize::root.body[12].body[3].body[1]::Return

Source: `infra/tests/test_roadmap_retry_authorization.py:58`; AST `e6ccbd746578ac6cf86c56b98e498310cdf37359c0ba485e0c77d3a78ade0173`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: authorize_single_retry, f, file_binding, self, source, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: authorize_single_retry, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::authorize::root.body[12].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:58`; AST `7107a9513a060d4835f32aa918261bf40602c43f7e31e7b232377f62c47198e8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: authorize_single_retry, f, file_binding, self, source, user_authorized. Outputs/bindings: (none).
Calls/effect boundaries: authorize_single_retry, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::authorize::root.body[12].body[3].body[1].value.keywords[2].value.elts[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:60`; AST `6c7e8d1704b21462aafe231951d9823e04e07e38191f2e72830c01f2e74a73bb`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, file_binding. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].value.keywords[2].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:62`; AST `2daabbe165a9f1926909b9e17afdaec42e999a321d86a16ad3197786c2af2022`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FIELDS, a, amendment, copy, k, limits, retry_limits, self, unchanged. Outputs/bindings: a, amendment, k, limits, unchanged.
Calls/effect boundaries: copy.deepcopy, retry_limits, self.assertEqual, self.authorize, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:63`; AST `a676bb33f4211862f9b10b8664f852e0685d4d4870bae17bfd61d5ff0a84f8a1`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: copy, self. Outputs/bindings: unchanged.
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:63`; AST `143c06aae24e4de242d0a1267b3119a2c0b16def9f052f841644af13a0bf0192`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: copy, self. Outputs/bindings: (none).
Calls/effect boundaries: copy.deepcopy.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:64`; AST `72e6892c64dbc5ef1d4a9b9c8bdd558501badfee3d2ee18c041a7e7d86f0572c`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: retry_limits, self. Outputs/bindings: amendment, limits.
Calls/effect boundaries: retry_limits, self.authorize, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:64`; AST `2cf62bca7e075f534e0e724bf4c89924da2a5d69067d7ccebaa88fff8814cf81`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:65`; AST `16d429175fa000a8b6ad6252c85919154b66b44adb5259c7ff29b43ce49deebb`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: amendment.
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:65`; AST `a89915d807bbcda64eaf2188f7e2d489a018ddbb7c0b2fc2ccc64e532dc42c64`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:66`; AST `b3db63b45258948e1c7987cf7b33867875bd9cddeca190830846fd701e72277d`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: limits.
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:66`; AST `31197e31c4111bf63e642fea438d45ec3a70fb40cebecf54ff34ca1ffc2dd61e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:67`; AST `a9ff9a4b1e2bf9d0ea841017b6887c321a2be258195db0d49909d701871e4662`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:67`; AST `1cb1d5c00cc3254fa389ec8fdb0dd0acd78adc7ac560570b7df242f9d3e2a8d4`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[2].value.args[1]::ListComp

Source: `infra/tests/test_roadmap_retry_authorization.py:67`; AST `b52db4556fcab44cc94b21d0d0fb1eb29de695d2effefb65992ad5f732369e64`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: FIELDS, a, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[2].value.args[1].elt::DictComp

Source: `infra/tests/test_roadmap_retry_authorization.py:67`; AST `3a17bfd0974a2805104623d598ecc82534533f7e7cb0d8e70fc5c905654fa084`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: FIELDS, a, k. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[4].body[2].value.args[1].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[3]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:68`; AST `d21b5776e2f884338ffb276d464c1f831c886c81d3f6ea4b428059436917b6fa`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[3].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:68`; AST `7cf23d2e665530aa0c31a53de33e9f7d5ff6053c44617d78ba4ccdcd097c59f5`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[3].value.args[1]::ListComp

Source: `infra/tests/test_roadmap_retry_authorization.py:68`; AST `d70dc340df2c8d9e8019472f5cfccf0998e0892bdde3cc830db7755caca5c9bd`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: FIELDS, a, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[4].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[3].value.args[1].elt::DictComp

Source: `infra/tests/test_roadmap_retry_authorization.py:68`; AST `3a17bfd0974a2805104623d598ecc82534533f7e7cb0d8e70fc5c905654fa084`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: FIELDS, a, k. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[4].body[3].value.args[1].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[4]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:69`; AST `12b5a01d663c7d2694e8e1b5644c9ddb6de071ad6ef320ab33fab9ddfc627a0f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: limits, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[4].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:69`; AST `3cfc3182994a0059fd8d934450eb671d5536a0f4a7ffdc79790667f9bb180756`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: limits, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[5]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:70`; AST `d7a1be87ec242f415043d4b9f352f3ac81a598446473c8e20e9d4beb28a7f825`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, unchanged. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[5].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:70`; AST `7402a9224b60b6cd13edb691280f54d732f0bf26afa83bfec051b1f97c5df194`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, unchanged. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[6]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:71`; AST `fb3a8da42afd3f208ba8dcadaeed9cef3f393638aacb51968e3119a2d37c2806`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[6].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:71`; AST `a6479f26ad94960b83360109a9bee0d925ab8525a35557da383809ccd4f8efb0`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[7]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:72`; AST `78901c0448c17324cd6825bf96200be9573b55dbb2e3381ed748e54afa76f4c0`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_latest_exhausted_generation_keeps_all_older_attempts::root.body[12].body[4].body[7].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:72`; AST `2cf0e42b577c31fabb8874492a05a6332b6a0c39d4d7e507d76f8c082b017867`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:74`; AST `11c673f8866648ccc84669fcfaf3a1c54fe5436e461b09d8508147343db2d28e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, dict, kwargs, self. Outputs/bindings: kwargs.
Calls/effect boundaries: dict, self.assertEqual, self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0]::For

Source: `infra/tests/test_roadmap_retry_authorization.py:75`; AST `4b1fd4d9e866a4db14025e94dbec48447a1c32b44f2e76980ad4f3cacac01710`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, dict, kwargs, self. Outputs/bindings: kwargs.
Calls/effect boundaries: dict, self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted. Iteration: kwargs in ({'user_authorized': False}, {'source': dict(self.source, role='assistant')}, {'source': dict(self.source, observed_native_turn='different-turn')})
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].iter.elts[1].values[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:76`; AST `4f9c502ee4158738fc8033a07dc34782a12b2d1029ec8ddb445c4bc6e8041b16`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].iter.elts[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].iter.elts[2].values[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:77`; AST `ef1ff9ede1a1c0ecd0bb6de611b6c4807acaac2ce4379b345783acc79124ac35`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].iter.elts[2].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:78`; AST `0e4d1b532dc31411653b51b1ec1ae556cf604bc0280dc420bbae8c202691ff09`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:78`; AST `b7c359e765a2530c369858b63529ca266627c2b855afb56e466938e9a5113d2b`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:78`; AST `2cf62bca7e075f534e0e724bf4c89924da2a5d69067d7ccebaa88fff8814cf81`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:78`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[0].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:79`; AST `b5b19c6c9a48016c5a968d6940032fd2fe786e1b86fa38c1a7e3fb0969acf6e7`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:79`; AST `19f79e7702d1da1bf7fba357fabd806459839e1519cf3713d76a2864979ed84f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:80`; AST `4a5116d88ee9087dd7f4cbf83bdb9d00bd02cce952affcabb9b8c906014f39ce`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_explicit_user_authority_and_current_native_turn_remain_required::root.body[12].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:80`; AST `a455c4ca47744d63bb6eccd8a5cdc7feb1f11a789490b6dd3c2406b700a9cf48`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:82`; AST `2e4f65b589316fcb67c217d4b1202099b6967697dc7fcffd52436da7ea6c984f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, dict, history, scenarios, self. Outputs/bindings: history, scenarios.
Calls/effect boundaries: dict, self.assertEqual, self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:83`; AST `1019e1e22b3a54c20b5b68948d00e7523df0a8db12756b55369ab3b1837cc62f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: scenarios.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[0].value.elts[1].elts[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:84`; AST `bd638aeb82388aedf0063c589f8117d3f7aed2437c5ecff666a57bfd3b97bc81`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value.elts[1].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[0].value.elts[2].elts[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:85`; AST `32962519f334df5b134dd831477ea7160729b4a1e2b6e220e400d1c19ee3eaf7`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value.elts[2].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[0].value.elts[3].elts[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:86`; AST `34c9b930c5eb86ddd423a5f23f55e07213e122c8a75f2465b47cb3d47e4f30a5`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].value.elts[3].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1]::For

Source: `infra/tests/test_roadmap_retry_authorization.py:87`; AST `e8dcb1834162f9d40ff82f940ae9e36d8e2a225e4a38bc3f21d36814ed9b2608`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, history, scenarios, self. Outputs/bindings: history.
Calls/effect boundaries: self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[6].body[1]; no call, error or mutation may be omitted. Iteration: history in scenarios
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:88`; AST `283ca9c84a30e3f5743766983d50e8ec21c5cbe4cb10bb7bf853ae9ee6202dc5`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, history, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:88`; AST `c36fa9b16208e7e228130b32c6e424f3dad6c5ccaa02461b1a0c114a5493f5b8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:88`; AST `cf2b8048ba1aa5453f0137e3aeb6d040c5a7f8f28461c6c235b877a41b0bf9c4`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:88`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].body[0].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:89`; AST `d23e33eda3ea24e0a92698d9902b171b2c5de3eaae61873531688a8d8ad38ccf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:89`; AST `a89915d807bbcda64eaf2188f7e2d489a018ddbb7c0b2fc2ccc64e532dc42c64`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[2]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:90`; AST `4a5116d88ee9087dd7f4cbf83bdb9d00bd02cce952affcabb9b8c906014f39ce`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_unspent_successful_or_unresolved_generations_cannot_borrow_failures::root.body[12].body[6].body[2].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:90`; AST `a455c4ca47744d63bb6eccd8a5cdc7feb1f11a789490b6dd3c2406b700a9cf48`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:92`; AST `b6e60d96529c13db1c80a7630f6c52203e688ea80b674bab26548d0db4872458`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, dict, history, retry_limits, scenarios, self. Outputs/bindings: history, scenarios.
Calls/effect boundaries: dict, retry_limits, self.assertRaisesRegex, self.authorize, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[0]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:93`; AST `5ae8243700debcf178141f98469d99f44ecdbe572237f17b6c5f9dfbc3845883`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:93`; AST `2cf62bca7e075f534e0e724bf4c89924da2a5d69067d7ccebaa88fff8814cf81`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:94`; AST `d23e33eda3ea24e0a92698d9902b171b2c5de3eaae61873531688a8d8ad38ccf`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:94`; AST `a89915d807bbcda64eaf2188f7e2d489a018ddbb7c0b2fc2ccc64e532dc42c64`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[1]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:95`; AST `25d78765437fd2db29b21d6a72605baa64af955620541b8e66cd2f860358f7de`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, self. Outputs/bindings: scenarios.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[1].value.elts[2].elts[1]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:97`; AST `2d8375258929095cb0da2cd038acc7418d4f50eef9436bf117746cb4efee6e9f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[1].value.elts[2].elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2]::For

Source: `infra/tests/test_roadmap_retry_authorization.py:99`; AST `5a327b9b8e3c0121163ee6ac10d8d38af12a5a3b17faa59a09a4402ec47e0a93`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, history, retry_limits, scenarios, self. Outputs/bindings: history.
Calls/effect boundaries: retry_limits, self.assertRaisesRegex, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[7].body[2]; no call, error or mutation may be omitted. Iteration: history in scenarios
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:100`; AST `81136bc58c460308cb046b8aa502200dff1e7b42daff80cbbf188fcb3dd66c36`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, history, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertRaisesRegex, self.state, self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:100`; AST `c36fa9b16208e7e228130b32c6e424f3dad6c5ccaa02461b1a0c114a5493f5b8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:100`; AST `cf2b8048ba1aa5453f0137e3aeb6d040c5a7f8f28461c6c235b877a41b0bf9c4`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: history, self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:100`; AST `06644738e9a475fc5e87a6ffd01516bb1976a842caf65d49e46a06bfdf2f41f2`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaisesRegex.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].body[0].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:101`; AST `eb1e424e961b0f3ea0527fa754e60d96a3309965464211e84a26a1637d68439e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_deleting_changing_or_reordering_older_history_invalidates_amendment::root.body[12].body[7].body[2].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:101`; AST `31197e31c4111bf63e642fea438d45ec3a70fb40cebecf54ff34ca1ffc2dd61e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[2].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_retry_authorization.py:103`; AST `f29547537c89cbcba3f2d774dd61a046ec53d99249838553b80032f2db49b105`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FIELDS, a, amendment, consumed, dict, digest, f, file_binding, json, k, later, later_spec, retry_limits, self, spec. Outputs/bindings: a, amendment, consumed, f, k, later, later_spec, spec.
Calls/effect boundaries: (f.root / 'later-spec.json').write_text, (f.root / 'pin.json').write_text, (f.root / 'spec.json').write_text, dict, digest, file_binding, json.dumps, retry_limits, self.assertEqual, self.authorize, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:104`; AST `3c30f78126eccd2f1016bf9f30cca06f629d6ac874dacdc1c8944b0ff48c1597`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: f.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[1]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:105`; AST `e734e0af64c0b0c19b29eadd6ab5f6179f0c97cb7fba4c57648caf1af0d2d846`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: self. Outputs/bindings: amendment.
Calls/effect boundaries: self.authorize, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:105`; AST `2cf62bca7e075f534e0e724bf4c89924da2a5d69067d7ccebaa88fff8814cf81`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:106`; AST `16d429175fa000a8b6ad6252c85919154b66b44adb5259c7ff29b43ce49deebb`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: amendment.
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:106`; AST `a89915d807bbcda64eaf2188f7e2d489a018ddbb7c0b2fc2ccc64e532dc42c64`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.authorize.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[2]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:107`; AST `2627acda8b6ea2fd3b5c626f949ff1abf75a094da2a6c2d39cb1c4d1ad479521`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: spec.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[3]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:108`; AST `2fd38bd13293afa7a3cce5bad26275cdab9853d3dd4191ac9488761c0b53be6a`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[3].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:108`; AST `3254329772b6922735f4ec217b2980d09b0fc6afc04d7da3cfb886c9cb23f6e6`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[4]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:109`; AST `c4b9ad6cef6105859fa90d1cff2c9655106b8a8ac725513ae4971b056c486ed8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, json, spec. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[4].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:109`; AST `e09fbe5ed2afb3d4682546f21569fe414aecd5fa9fbffa5eec7b55a31bfc43db`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, json, spec. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:109`; AST `ce6786d296b3d003b2100e46234b9b78eb236599129eb107d286cbb31d047e76`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, spec. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[5]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:110`; AST `576b0c6c614faff6665c583519947f686c20cb5f84933bf2cf5350ded2e48bef`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, f, file_binding, self, spec. Outputs/bindings: consumed.
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[5].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:110`; AST `159c5e00ad66ce8480be01eef31a097da86c0ef1a5e92efb7035a929100b5ee8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, f, file_binding, self, spec. Outputs/bindings: (none).
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[5].value.keywords[3].value.values[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:111`; AST `2dad2840552a424b1f785510b6e0a20f376db41f874fc0a692d38979cfeb6bb8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, file_binding. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[5].value.keywords[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[6]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:112`; AST `ac33c2a18ce80230ede2079b09029f7cea0f6edc559cc69ab3494df5f1262e0b`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: later_spec.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[7]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:113`; AST `5994d505ba01066dcb5f9b3fd54a8e20ba43d65d70893b8b85461494cd7fd58e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[7].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:113`; AST `41e75853b21ed5f4a7b09bfe647ae4722439481669336072f2854ffb6d5d60b8`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[8]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:114`; AST `9bc1f44666b603242ad9a50d3aae0e41999f3ebcb8593f80b17f3ba466db17a3`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, json, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'later-spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[8].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:114`; AST `44c3a3bf7d2b0e46b2cbf470399bc59291ed4534641376649636e79446c40169`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, json, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'later-spec.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:114`; AST `ab6adc3d8d975cd2b9549a380ee5b918df1ad3ed81597923b3cb6ca552e19647`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[9]::Assign

Source: `infra/tests/test_roadmap_retry_authorization.py:115`; AST `8e5221b7a60a12c0ba9aa2ccce9ef70721c31fb9587b3d4c50340dc743e1492f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: consumed, dict, f, file_binding, later_spec. Outputs/bindings: later.
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[8].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[9].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:115`; AST `05e760b021dd464fcc2e8e745fac2e814cd4c04506e05a1b918de99fb2065d0a`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consumed, dict, f, file_binding, later_spec. Outputs/bindings: (none).
Calls/effect boundaries: dict, file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[9].value.keywords[3].value.values[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:116`; AST `69dda6d0701669f4d78e39496ee854f0b73cd8a27f84dc17c6ce172a03444bc7`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, file_binding. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[9].value.keywords[3].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[10]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:117`; AST `ee14dfc38c0ac30828dc8eb55f74151e6e6cd80350a0c1631e9eaf989d92c14d`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[10].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:117`; AST `2d11b6a92bdc56df3d7a22f0255ac05a1a66cbc87aefd5544ae8ce0d83e8374c`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f. Outputs/bindings: (none).
Calls/effect boundaries: (f.root / 'pin.json').write_text.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[11]::With

Source: `infra/tests/test_roadmap_retry_authorization.py:118`; AST `5728a10923bf1526fdbb6d753e39170b4be6e3f55692be1857bf00b2f375705e`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: consumed, f, later, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual, self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[11].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:118`; AST `0d7543d462124239de38325d22fe25f8a88951fd65a53d5433722deebd2e730f`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: consumed, later, self. Outputs/bindings: (none).
Calls/effect boundaries: self.state.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[11].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[11].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:119`; AST `5a09c33c63831fe271f0e8234cccf6228c9a00bd6b8112c4984ba0194a189c7c`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: f, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[11].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[11].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:119`; AST `af5edab79d76ea4e0354d048ca5f673523461683716d865403c50cc61a391dc9`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, retry_limits, self. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[11].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[11].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:119`; AST `557c654767f5346e3226d770154325d26c7dce82fc2786f18727dcdefab92e04`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: f, retry_limits. Outputs/bindings: (none).
Calls/effect boundaries: retry_limits.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[11].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[12]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:121`; AST `d21b5776e2f884338ffb276d464c1f831c886c81d3f6ea4b428059436917b6fa`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[12].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:121`; AST `7cf23d2e665530aa0c31a53de33e9f7d5ff6053c44617d78ba4ccdcd097c59f5`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FIELDS, a, amendment, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[12].value.args[1]::ListComp

Source: `infra/tests/test_roadmap_retry_authorization.py:121`; AST `d70dc340df2c8d9e8019472f5cfccf0998e0892bdde3cc830db7755caca5c9bd`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: FIELDS, a, k, self. Outputs/bindings: a, k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered ListComp evaluation at root.body[12].body[8].body[12].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::RetryAuthorizationHistoryTests::test_consumed_generation_cannot_extend_later_work_or_freeze_old_pins::root.body[12].body[8].body[12].value.args[1].elt::DictComp

Source: `infra/tests/test_roadmap_retry_authorization.py:121`; AST `3a17bfd0974a2805104623d598ecc82534533f7e7cb0d8e70fc5c905654fa084`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: FIELDS, a, k. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered DictComp evaluation at root.body[12].body[8].body[12].value.args[1].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[13]::If

Source: `infra/tests/test_roadmap_retry_authorization.py:124`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_retry_authorization.py:125`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_retry_authorization.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_retry_authorization.py:125`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_retry_authorization`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_lease, agentinfra.roadmap_records, agentinfra.roadmap_runtime, contextlib, copy, json, test_roadmap_mirrors, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
