# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 53. Inventory digest: `eee518c577e8a0077be15729b8d3412b2c9be40088c06bee79194e5c355ac894`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_context_cache.py::module::root::Module

Source: `infra/tests/test_context_cache.py:1`; AST `f293d7c9569f258fa93a3ab5ffb335d625dbe438f28f08f177086459fe51d540`.

Rust module: `infra::tests::test_context_cache`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContextLedger, Path, __file__, c, p, r, self, str, sys, td, tempfile, unittest. Outputs/bindings: c, p, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, Path(__file__).resolve, c.check_external, c.check_file, c.record_external, c.record_file, p.write_text, self.assertFalse, self.assertTrue, str, sys.path.insert, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[0]::Import

Source: `infra/tests/test_context_cache.py:1`; AST `b400fb0a9b6adb96c85f34ec7956316b19d8ee3a6839165cd5ae308b9fcc1d1e`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_context_cache.py:2`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[2]::Import

Source: `infra/tests/test_context_cache.py:3`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[3]::Expr

Source: `infra/tests/test_context_cache.py:4`; AST `61fad4888db62e44ef99d9882a36cf9031e788cf0d285b1b1a6f58e0f3f453be`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[3].value::Call

Source: `infra/tests/test_context_cache.py:4`; AST `7c0537fe3f970c5fb1e332974a152c840c375cb8068e9725b91862d6134539d8`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str, sys.path.insert.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[3].value.args[1]::Call

Source: `infra/tests/test_context_cache.py:4`; AST `ab2eca00c1f4645269130fc06c0895e2863927ebec1c6947bafa9c81f17c0516`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve, str.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[3].value.args[1].args[0].value.value::Call

Source: `infra/tests/test_context_cache.py:4`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1].args[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[3].value.args[1].args[0].value.value.func.value::Call

Source: `infra/tests/test_context_cache.py:4`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[3].value.args[1].args[0].value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_context_cache.py:5`; AST `0b35bf7d9067c30646f468497070d16798aef93e6cd52b40466dd13edad29f82`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::root.body[5]::ClassDef

Source: `infra/tests/test_context_cache.py:6`; AST `5a433ac2c4fb02df17f5cab886195baf0c5d3d7384942edc7c55390393101a4d`.

Rust module: `infra::tests::test_context_cache`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContextLedger, Path, c, p, r, self, td, tempfile, unittest. Outputs/bindings: c, p, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, c.check_external, c.check_file, c.record_external, c.record_file, p.write_text, self.assertFalse, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0]::FunctionDef

Source: `infra/tests/test_context_cache.py:7`; AST `3f0b3adf8e80bc5b8484408b821542f67ad072c645c5ab5b2b151ac32be572d4`.

Rust module: `infra::tests::test_context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContextLedger, Path, c, p, r, self, td, tempfile. Outputs/bindings: c, p, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, c.check_file, c.record_file, p.write_text, self.assertFalse, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0]::With

Source: `infra/tests/test_context_cache.py:8`; AST `0c3697baa226d7a562ab1be0b0e4d00acd73b9d97cfbe0bd054cc16300a3e685`.

Rust module: `infra::tests::test_context_cache`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContextLedger, Path, c, p, r, self, td, tempfile. Outputs/bindings: c, p, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, c.check_file, c.record_file, p.write_text, self.assertFalse, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_context_cache.py:8`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_context_cache.py:9`; AST `078760d9bdca95fe75cfe621dc62f15c757edcd68a31dee43d1c2d9fa9c3b358`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: r.
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[1]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `e0727b5322fc957eb8c69b44d368de016f42a7f5504181be6205fd0a80e14401`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[1].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `3f0983fbee1ea97b2067d3d67a1436cf3a95ad16f2d68ede9fad52fd829a5543`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[2]::Assign

Source: `infra/tests/test_context_cache.py:9`; AST `4ac606d6324358cb1499de12129c0a1635bb70c8c04118e301b9e34cf9fdb054`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: p.
Calls/effect boundaries: (none).
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[3]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `98a00a75a0ff24be3337f4d1ce4b6b04c3ddd8dc88c1c00e2bc8ce6d370c098e`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.write_text.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[3].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `aa147fdc8b8f02cb4c103b9a74b0d80c577f2a8da0dc6d1a91ff9b4d7f366dad`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.write_text.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[4]::Assign

Source: `infra/tests/test_context_cache.py:9`; AST `254f8487ca759001994902c163f953f275a984e81a3a620d1fa20fafc050cebe`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextLedger, r. Outputs/bindings: c.
Calls/effect boundaries: ContextLedger.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[0].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[4].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `06b52f2116e6de57e4e6f3a30d5b92d66faa7c4e14976936847b289a20360243`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextLedger, r. Outputs/bindings: (none).
Calls/effect boundaries: ContextLedger.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[5]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `f50bee5dc3a0b15872f45a2b0d76caf9c772789dd65e848fd3acda0f9f59ae24`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, p. Outputs/bindings: (none).
Calls/effect boundaries: c.record_file.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[5].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `d564df13e3a016c7f33747a566d2a8a20213bbaf4f44d56426193deb32557959`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, p. Outputs/bindings: (none).
Calls/effect boundaries: c.record_file.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[6]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `0c5d10dd578d335f0afcc39e4c131b4b8659e6243068e2f33d0ec873ff593af4`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, p, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[6].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `662c901c0e9cd6a0e46c4c7676644dc9493063330181d04fd84f0424a0575e0e`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, p, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[6].value.args[0].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `481df168ceb0a072f10e0a379f8089ea2ac9176a5032b7f09743a701925c344d`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, p. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[7]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `de92bef50679a7f6f5a770f76cfca57e646901c550d53185d66f45d0315090d1`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.write_text.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[7].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `3edfc4e92a4dae45e489e9fb682f9bc6ee7c0a47cd9291f36e4315c3506808b8`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.write_text.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[8]::Expr

Source: `infra/tests/test_context_cache.py:9`; AST `4383ee5bbaf378e75d38627af35914a1da7ceb1bb630719f68e770136c606063`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, p, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file, self.assertFalse.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[0].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[8].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `ce0271ddeb4e2538522c7bb3967bb84c346ee277741844461c4686e53ba6328c`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, p, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file, self.assertFalse.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_freshness::root.body[5].body[0].body[0].body[8].value.args[0].value::Call

Source: `infra/tests/test_context_cache.py:9`; AST `481df168ceb0a072f10e0a379f8089ea2ac9176a5032b7f09743a701925c344d`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, p. Outputs/bindings: (none).
Calls/effect boundaries: c.check_file.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[0].body[0].body[8].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1]::FunctionDef

Source: `infra/tests/test_context_cache.py:10`; AST `d118a09347032443f8b0e0bddb2f5e07b5367e6375c4f562bec31ef5a213c0eb`.

Rust module: `infra::tests::test_context_cache`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContextLedger, Path, c, r, self, td, tempfile. Outputs/bindings: c, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, c.check_external, c.record_external, self.assertFalse, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0]::With

Source: `infra/tests/test_context_cache.py:11`; AST `475b82c335e3a26b26441409b3cb8b51c2631429b8134c6d79a46f505340aebe`.

Rust module: `infra::tests::test_context_cache`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContextLedger, Path, c, r, self, td, tempfile. Outputs/bindings: c, r, td.
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir, ContextLedger, Path, c.check_external, c.record_external, self.assertFalse, self.assertTrue, tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_context_cache.py:11`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[0]::Assign

Source: `infra/tests/test_context_cache.py:12`; AST `078760d9bdca95fe75cfe621dc62f15c757edcd68a31dee43d1c2d9fa9c3b358`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, td. Outputs/bindings: r.
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[0].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `40bd10ef988a11cfcc1811702f293fafab0ee58341a21ebd24d826d93d2e1bc5`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, td. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[1]::Expr

Source: `infra/tests/test_context_cache.py:12`; AST `e0727b5322fc957eb8c69b44d368de016f42a7f5504181be6205fd0a80e14401`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[1].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `3f0983fbee1ea97b2067d3d67a1436cf3a95ad16f2d68ede9fad52fd829a5543`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: r. Outputs/bindings: (none).
Calls/effect boundaries: (r / '.aegis' / 'runtime').mkdir.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[2]::Assign

Source: `infra/tests/test_context_cache.py:12`; AST `254f8487ca759001994902c163f953f275a984e81a3a620d1fa20fafc050cebe`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContextLedger, r. Outputs/bindings: c.
Calls/effect boundaries: ContextLedger.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[5].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[2].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `06b52f2116e6de57e4e6f3a30d5b92d66faa7c4e14976936847b289a20360243`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContextLedger, r. Outputs/bindings: (none).
Calls/effect boundaries: ContextLedger.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[3]::Expr

Source: `infra/tests/test_context_cache.py:12`; AST `e8644fd3d2e92a68c07fab695019bc63dfca590ad86784d7213ab33a22179cf5`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.record_external.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[3].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `4665ac45f147e6ed0ef6da01da9a8bd8e53c6f4045075554b9694e80b4a97747`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.record_external.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[4]::Expr

Source: `infra/tests/test_context_cache.py:12`; AST `47913a5c8a707487f25205e4eb82bfbf08a94104c2d62f8af964922e61371ccb`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[4].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `3c317de5285d44cdf1b8f737c996b68f19722d0bcc5a848e4d2cb9a8bca62551`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[4].value.args[0].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `8e1a679eb26e6aa966a0becd734bba2a9f17b8c033bd09fe9beb4b0f1babe969`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[5]::Expr

Source: `infra/tests/test_context_cache.py:12`; AST `3e2268da20d28b0770760ed473e41467218ff49794aaa117dd8e74eefc198f43`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[5].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `4f2674beb7cc05f884b71f4ffaa0942591bd58f66d34c8fe64b821d0415ae971`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertTrue.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[5].value.args[0].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `c9ad26c96e65d85303cf6c8290bcd06c302bee0f2c92e03bf5234bab4a65f4a8`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[5].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[6]::Expr

Source: `infra/tests/test_context_cache.py:12`; AST `8820664322768742b1675107e31eb942d8732a0d3300ff91f1e0d975a25ad57a`.

Rust module: `infra::tests::test_context_cache`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertFalse.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[5].body[1].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[6].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `1fc26ee669841728d846c20f8a3bb4225868a248ce93ca758f3300157d379c10`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c, self. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external, self.assertFalse.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_context_cache.py::module::TestContext::test_external_fingerprint_and_ttl::root.body[5].body[1].body[0].body[6].value.args[0].value::Call

Source: `infra/tests/test_context_cache.py:12`; AST `67a67dfc65a6362a060959ea4706647f75b74b9a14102e61150d17588c47cb96`.

Rust module: `infra::tests::test_context_cache`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: c. Outputs/bindings: (none).
Calls/effect boundaries: c.check_external.
Dependencies: agentinfra.context_cache, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[5].body[1].body[0].body[6].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
