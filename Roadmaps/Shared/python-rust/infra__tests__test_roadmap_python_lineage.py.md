# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 50. Inventory digest: `2882e1af4f22caf3d68c072cb63fa1ef516360cbcdd49675bb229423b2f48a36`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python_lineage.py::module::root::Module

Source: `infra/tests/test_roadmap_python_lineage.py:1`; AST `5f804207876e285dfd5b45bc14f71200fe5961a65676f8ce6fee0ca10928eb63`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, __file__, __name__, adapter, after, after_lineage, before, before_lineage, compile_roadmaps, compiled, materialize, patch, qualification_lineage_digest, root, self, unittest. Outputs/bindings: adapter, after, after_lineage, before, before_lineage, compiled, root.
Calls/effect boundaries: Path, Path(__file__).resolve, compile_roadmaps, materialize, patch, qualification_lineage_digest, self.assertEqual, self.assertNotEqual, unittest.main.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:1`; AST `4e094d6f94cf27400bad6c54f8bdab53b67755286c968bd9e5e606ea4c578f2a`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python_lineage.py:2`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python_lineage.py:3`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[3]::ImportFrom

Source: `infra/tests/test_roadmap_python_lineage.py:4`; AST `4337bb2ad9c9b8e6d80fa1b5afcef1e5d4531beaa533830f57d17fa8c1fbfed0`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_roadmap_python_lineage.py:6`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_roadmap_python_lineage.py:7`; AST `f591b94bc26fa70d226222ceced27abd3b76227ea4ed3f2f55f990245323a8f6`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[6]::ImportFrom

Source: `infra/tests/test_roadmap_python_lineage.py:8`; AST `9522470acdd9432bb8a66c5f3ab64ab27f43c5e9d9cfed23e8413315fafcd375`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::root.body[7]::ClassDef

Source: `infra/tests/test_roadmap_python_lineage.py:11`; AST `f79d02103ced62e4768ef6b32b597dcd0f4cd735a2c863821bb9a76669ac8d7f`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, __file__, adapter, after, after_lineage, before, before_lineage, compile_roadmaps, compiled, materialize, patch, qualification_lineage_digest, root, self, unittest. Outputs/bindings: adapter, after, after_lineage, before, before_lineage, compiled, root.
Calls/effect boundaries: Path, Path(__file__).resolve, compile_roadmaps, materialize, patch, qualification_lineage_digest, self.assertEqual, self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python_lineage.py:12`; AST `e277aae2ead74d5217671ec2392ab4846092ff62a1eea7ce847b922366a892f0`.

Rust module: `infra::tests::test_roadmap_python_lineage`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, __file__, adapter, after, after_lineage, before, before_lineage, compile_roadmaps, compiled, materialize, patch, qualification_lineage_digest, root, self. Outputs/bindings: adapter, after, after_lineage, before, before_lineage, compiled, root.
Calls/effect boundaries: Path, Path(__file__).resolve, compile_roadmaps, materialize, patch, qualification_lineage_digest, self.assertEqual, self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:13`; AST `102a72c5f3942e83b9aacee69bcfb09ce3245f1d4d9767548da37bf9e4c027ac`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: root.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[0].value.value.value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:13`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[0].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[0].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:13`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[0].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:14`; AST `8deac8da987fee33047b87c849024fe4b35da2d8f7167922e3c744059f79a3b1`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compile_roadmaps, root. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:14`; AST `8d757ae521db00b1487ab7b49b1e2f506dd3bb8860b646bae4d025634d847d29`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compile_roadmaps, root. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[2]::With

Source: `infra/tests/test_roadmap_python_lineage.py:15`; AST `a7d05664967e90e7bcd14e010e329877697bc714cab813e837300b1e2eda4fce`.

Rust module: `infra::tests::test_roadmap_python_lineage`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: patch, qualification_lineage_digest, root. Outputs/bindings: before_lineage.
Calls/effect boundaries: patch, qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:15`; AST `4db61d8f13b2b7ca13e2b9b7a5b46a17e707789f8aae9220d804cd23a9051327`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:16`; AST `094cf0aa70cd9cf93103f122238fb28fa493e874ebae674274ab5938a401c2d5`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_lineage_digest, root. Outputs/bindings: before_lineage.
Calls/effect boundaries: qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:16`; AST `6f771478205f96f6fe57db67be5c9976b9c13a5a608aabbbb21d78181a763e87`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_lineage_digest, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[3]::With

Source: `infra/tests/test_roadmap_python_lineage.py:17`; AST `8ae882f0dabd657434c1b4ef5704d04acc4e65ac7ee0c56a3eee8c1914bdaa00`.

Rust module: `infra::tests::test_roadmap_python_lineage`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: patch, qualification_lineage_digest, root. Outputs/bindings: after_lineage.
Calls/effect boundaries: patch, qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:17`; AST `010bded60f062783c32d66f42e5daee477a3f088790d2ab4d4cace4eae8a3749`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:18`; AST `25704570b1e1f935331bb1d3ba60811298ba9d5df8e504fd621b77e3844096a5`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: qualification_lineage_digest, root. Outputs/bindings: after_lineage.
Calls/effect boundaries: qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:18`; AST `6f771478205f96f6fe57db67be5c9976b9c13a5a608aabbbb21d78181a763e87`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification_lineage_digest, root. Outputs/bindings: (none).
Calls/effect boundaries: qualification_lineage_digest.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:19`; AST `41da686a9feaca2fc7f208cc78e6ab315b1e7f6dbab7709cc915386bbc3436fa`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after_lineage, before_lineage, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:19`; AST `21962728ebfdaf6e8cdc74476b8a17a06273807e8271ca1c78cd3736b83b779c`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after_lineage, before_lineage, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5]::With

Source: `infra/tests/test_roadmap_python_lineage.py:20`; AST `b72eb3c71f5e1026c26bb57f24aa0a97b15b616e03014b79b7aac83379e1fc07`.

Rust module: `infra::tests::test_roadmap_python_lineage`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: adapter, after_lineage, before_lineage, compiled, materialize, patch, root. Outputs/bindings: adapter, after, before.
Calls/effect boundaries: materialize, patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:20`; AST `bbb1b9b6d4f336f0b21a21f67813e261928092532a3073a94ab28f6a3467eb88`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:21`; AST `8a1670d5130c1f428bd0fabd5771e6a1faf7e512b9e2e4c74cb0b729c9a7917d`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].items[2].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:22`; AST `c3a5571317df0619f5fc1b096548722ecd06ee7b1380fbe4f69b5ed2961856fe`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].items[2].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].items[3].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:23`; AST `db9b5ae47aa6af3348dab74806ca6c58e205b70face592b92208d6c153f540ba`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].items[3].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:24`; AST `b257a05bb6a518286e1e04e095de68e76139f200f6f09dbbfed908fccdb7adba`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: adapter. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[1]::With

Source: `infra/tests/test_roadmap_python_lineage.py:25`; AST `6c43e53db115955a9cbd75b3ab6c629f6180ee4000de927c5298a459f2d0e62e`.

Rust module: `infra::tests::test_roadmap_python_lineage`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: before_lineage, compiled, materialize, patch, root. Outputs/bindings: before.
Calls/effect boundaries: materialize, patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[0].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[1].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:25`; AST `e5a91090f1be6f399d900351fd9eeb39833e9f6ec3ed346067b235ac4592b973`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before_lineage, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:26`; AST `012c342466d6fabeecc54a0234545c989d2474d171bd5412494a6d304a48b406`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, root. Outputs/bindings: before.
Calls/effect boundaries: materialize.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[5].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:26`; AST `c8cc254a29092adc8d482f3de3cbf13b41d08c45dac73043ee576a3e0dd532ae`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, root. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[2]::With

Source: `infra/tests/test_roadmap_python_lineage.py:27`; AST `f97fff14c43294b6bbc45aa19847ac1b44deef62f93761ae8e9d2c26633c75b7`.

Rust module: `infra::tests::test_roadmap_python_lineage`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: after_lineage, compiled, materialize, patch, root. Outputs/bindings: after.
Calls/effect boundaries: materialize, patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[7].body[0].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python_lineage.py:27`; AST `0cc76ab81966c72fab8f5ec2d328f1e779a4b6554ceca5b1437e1ce556676cb7`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after_lineage, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python_lineage.py:28`; AST `fee9b65901b7dcbffe47cb39c0401099fd28a220cd73978b3aeab390c88bbf06`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: compiled, materialize, root. Outputs/bindings: after.
Calls/effect boundaries: materialize.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[7].body[0].body[5].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[5].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:28`; AST `c8cc254a29092adc8d482f3de3cbf13b41d08c45dac73043ee576a3e0dd532ae`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled, materialize, root. Outputs/bindings: (none).
Calls/effect boundaries: materialize.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[5].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:29`; AST `c9a9f862789180ff4bf1c09c458ba8e4da564ab61a66e4c6f1b3d6713ac79f0a`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:29`; AST `5a296ab5b62394a4bb03db76d70a9221a6ef73282b9a3c7a40b40c6a0eaafbf2`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:30`; AST `ce56077cb179b002437f4236de4232246c7f006d7b8a0f05af3dc8656fc4ca18`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:30`; AST `7369fdee3877cdd1f6f24fb635b2e608d7cfb49dc341b041685f34daa77cdd3f`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:31`; AST `12d6c11bc79c662f217d25a678ab9b7693c116533822c45c46033e20a1f91f8e`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:31`; AST `0e0dff0746870b9a939ad36ca46a3d4bd1c9e408702624c4b08fee3ae334a407`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[9]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:32`; AST `19cd72b83cea70eeabd154bb3297828daa411975a68eeded47e1b84363fe440c`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, after_lineage, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[7].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::QualificationLineageTests::test_new_failed_attempt_invalidates_route_even_when_selected_result_and_dependencies_are_unchanged::root.body[7].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:32`; AST `b0684521dc8d061213fbcde535e1e26407bcfe36eba3080dc76ae543f7aef544`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, after_lineage, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[7].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[8]::If

Source: `infra/tests/test_roadmap_python_lineage.py:35`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_python_lineage`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[8]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[8].body[0]::Expr

Source: `infra/tests/test_roadmap_python_lineage.py:36`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_python_lineage`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python_lineage.py::module::root.body[8].body[0].value::Call

Source: `infra/tests/test_roadmap_python_lineage.py:36`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_python_lineage`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: agentinfra.roadmap, agentinfra.roadmap_python_catalog, agentinfra.roadmap_work, pathlib, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
