# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 227. Inventory digest: `5e35df58fd6ea1c66c1981ff3b37e3aabc49f78c81adee311bffa4b6affa1020`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_python.py::module::root::Module

Source: `infra/tests/test_roadmap_python.py:1`; AST `03975cd5e65f32c11716b08fc626e58612e9c44bcd8111c43ee63e888f0db358`.

Rust module: `infra::tests::test_roadmap_python`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, Path, ROOT, __file__, __name__, after, all, any, ast, b, backend, base, before, binding, c, classify_nagini, code, compile, compile_roadmaps, compiled, dict, digest, directory, error, errors, expected, field, json, len, locations, maintained_python, marker, o, observed, original, original_occurrences, os, p, path, python_proof_errors, qualification, r, record, repr, research_sources, result, root, route, run, run_process, self, shared, source_closure, stat, str, sys, tempfile, unittest. Outputs/bindings: ROOT, after, b, backend, base, before, binding, c, code, compiled, directory, error, errors, expected, field, locations, marker, o, observed, original, p, path, qualification, r, record, result, root, run, shared, stat.
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, (self.package / '__init__.py').write_text, (self.package / 'dependency.py').write_text, (self.package / 'policy.py').write_text, (shared / 'python-backends.json').write_text, Path, Path(__file__).resolve, all, any, ast.parse, classify_nagini, compile, compile_roadmaps, compiled['milestones'].values, dict, digest, json.dumps, json.loads, len, maintained_python, marker.read_text, original_occurrences, p.relative_to, p.relative_to(ROOT).as_posix, path.read_text, path.write_text, python_proof_errors, qualification.read_bytes, qualification.write_text, repr, research_sources, route, run_process, self.addCleanup, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertRaises, self.assertTrue, self.package.mkdir, self.subTest, shared.mkdir, source_closure, stat.exists, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split, str, tempfile.TemporaryDirectory, unittest.main, unittest.skipUnless.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:1`; AST `0c4595ac2b2d399ad9402f9ee6781c4466c29ac1fbb678b92db3ecc99a5a6cfc`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_python.py:4`; AST `bb134ca6c8f43358b0a04f3db40a8957242456961f7c0823aff7ae7a2647bf15`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_python.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[4]::Import

Source: `infra/tests/test_roadmap_python.py:6`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[5]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_python.py:8`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_python.py:9`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[8]::Import

Source: `infra/tests/test_roadmap_python.py:10`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:12`; AST `255dfec4d6ff7dfa92dc78e143e11e331797115bca3317171a233bfe87c5edad`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:13`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:14`; AST `8b11526286d670f6db56373ac2d945a7b60b9bd911080dfa50d92d05e5ace340`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[12]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:16`; AST `89fa3cece15c85f52acf7272af1f6fb8df074282f59e31da1447d1bc4325e2b1`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[13]::ImportFrom

Source: `infra/tests/test_roadmap_python.py:17`; AST `5b90894d096758c9f19f8600da372bc7cd3d8c63d0642e575f9761c8cc9880e1`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[14]::Assign

Source: `infra/tests/test_roadmap_python.py:20`; AST `54984a8c5ee3afca40c43588fccd6a196361c5bd0f3a143eae021f3097225f2c`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[14].value.value.value::Call

Source: `infra/tests/test_roadmap_python.py:20`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[14].value.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python.py:20`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::root.body[15]::ClassDef

Source: `infra/tests/test_roadmap_python.py:23`; AST `ece22d8101d5a08642ceac88bd33099953c3b43f6104734119eb0c3541ae50f3`.

Rust module: `infra::tests::test_roadmap_python`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, Path, after, b, before, path, record, self, source_closure, tempfile, unittest. Outputs/bindings: after, b, before, path, record.
Calls/effect boundaries: (self.package / '__init__.py').write_text, (self.package / 'dependency.py').write_text, (self.package / 'policy.py').write_text, Path, path.read_text, path.write_text, self.addCleanup, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertRaises, self.assertTrue, self.package.mkdir, source_closure, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:24`; AST `4fbb6506a9d67753f82bd1fc63944fa51b4d792ac15e6d911b2fa122e8031264`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / '__init__.py').write_text, (self.package / 'dependency.py').write_text, (self.package / 'policy.py').write_text, Path, self.addCleanup, self.package.mkdir, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:25`; AST `aed684f24ac276f0e7121e6cce3c97723895a3c83e7c086cf3aab5997bac5b9b`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:25`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:26`; AST `be0fdf37b1d8171d3fa8ad7bf50e5c62c9fac9c5be724abd5499be1f56cb798e`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:26`; AST `5e2bcaf4be28e656ea35bbf68d353fc84ac3adb02be149a886951ba64dea2378`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.addCleanup.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python.py:27`; AST `35e4ba0862c162c9d0fed7ea498cab22c824665f26b8232b425d3ac3b4e1407b`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:27`; AST `df6a72f8bc4f533242bba3097d5da8d512f1b7fda6700f75ad71f93e695b95a7`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, self. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_python.py:28`; AST `625e1a2a4089be7fb9825b7c3622e4a03654df63406fbb1fa1a67b94cc92756d`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:29`; AST `ef24c1b42ea766a0722e7a0654b525c9ae1aba2fc6bc31e483ff049407b3ecb0`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.package.mkdir.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:29`; AST `74f3f6a567bc485985db9b0baeb90231daf2099cdf3cb96264522c99afe98d4b`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.package.mkdir.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python.py:30`; AST `15323a790f65732bc7e8ed53e7050d034b4753ec3b114d6d53d871f1915e064f`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python.py:30`; AST `25280b330465f0071fa94ac86c7e7295bb42e2ba8f4b2cab37f0250c4d645d5a`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / '__init__.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python.py:31`; AST `d137dace13413811d1e3f050966d4037534ece135db89e26bcb28593d3f093c5`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'dependency.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python.py:31`; AST `3c437c98660513b50864a65f91198aaba0a6a12ae133dbd563504ec8562fe1c4`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'dependency.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python.py:32`; AST `98ef985cb1bafb315f3642067f3642466898365b7ea345fb1c50ad3529441d6a`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'policy.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::setUp::root.body[15].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python.py:32`; AST `ebeaf81e422e97e684b89d9a0c33ec3723b4603f65a0dc6998f826418b3dd942`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'policy.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:34`; AST `0210a0f0c53d4d8ddb3bad98139e29b1398b096646080d6924574c5a92480c7f`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: after, b, before, self, source_closure. Outputs/bindings: after, b, before.
Calls/effect boundaries: (self.package / 'dependency.py').write_text, self.assertEqual, self.assertNotEqual, source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:35`; AST `13ee664fceb5dd9aebd7e4dfaf960cf4b5808941baf017bf1f950359a73b5bb7`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_closure. Outputs/bindings: before.
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:35`; AST `9f5fcef1ae4c316723de1c91ab2ed07c3692dd1d2c76f6a09e246284763dbe43`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:36`; AST `3f88432a5f659dc98961da83c417f91d16676a7569acf8e42646ec04b057319e`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, before, self. Outputs/bindings: b.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:36`; AST `03a7df2a8b05d94b47e53e69342e71316261c0e6620c4f6acc6363f692884e8e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, before, self. Outputs/bindings: b.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[1].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python.py:36`; AST `4813a8e54d8645387a61b8067b520c90dcf6d790cb23386b715bbe32b4fcd762`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, before. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:37`; AST `b1cd1fe7cb62610124e0efa4908f67e22ff841f23be3ac23d096a7c50dd87685`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'dependency.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:37`; AST `cbc1392069e7844d6308fa1d6e27608b03424619c8fb66187d9baa08000f57bb`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (self.package / 'dependency.py').write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[3]::Assign

Source: `infra/tests/test_roadmap_python.py:38`; AST `52a7171bdf5361408288ac1aabb294319092bf48377db7f18c7bac5f6706d386`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_closure. Outputs/bindings: after.
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:38`; AST `9f5fcef1ae4c316723de1c91ab2ed07c3692dd1d2c76f6a09e246284763dbe43`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:39`; AST `12d6c11bc79c662f217d25a678ab9b7693c116533822c45c46033e20a1f91f8e`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:39`; AST `0e0dff0746870b9a939ad36ca46a3d4bd1c9e408702624c4b08fee3ae334a407`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[5]::Expr

Source: `infra/tests/test_roadmap_python.py:40`; AST `3dc365443087918800314993a716512c06fbe7097db014a74e59ca44e634d8c7`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_whole_imported_modules_and_package_state_remain_bound::root.body[15].body[1].body[5].value::Call

Source: `infra/tests/test_roadmap_python.py:40`; AST `389774e26a27a0bdd4a7c0a0231dcbeb2657c1411fcc937f4103998c211640fe`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: after, before, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:42`; AST `cf6c4895e58c1f9a1159c6937b6b6f784d7ab18262edf2e04fcc9d61947501b3`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: record, self, source_closure. Outputs/bindings: record.
Calls/effect boundaries: self.assertEqual, self.assertFalse, self.assertTrue, source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:43`; AST `09b7b4bcdd99d5f10cb5399b521891f5b3cff61228a43e51bfab7b6088f9026b`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_closure. Outputs/bindings: record.
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:43`; AST `9f5fcef1ae4c316723de1c91ab2ed07c3692dd1d2c76f6a09e246284763dbe43`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:44`; AST `45ab41f256587af60908192ba12d24e44eb91e2c135623bc77511fd29a4ae5d6`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:44`; AST `85194c79f75ec4d8ec79493f6fb074506e006faac1fb00cbe356480f6f25bc40`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:45`; AST `41144b2ca335d47e500d1e3ab5dbb6c6c96de5484e3244c6c73d21f58d731884`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:45`; AST `3150ffcdef3101e2e6b7c6ab47c89636ac5ff4b49a4ccf43d1fa8d6b1fcd7188`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:46`; AST `cd3d15f734a1f3b1a0be297c536f87cdb7ab531bddf6982e3444526040517977`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:46`; AST `8273ba7b0522303beb185c6d3e65ee4f276b0b436cf05d4f60a8d8cb8686a63c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:47`; AST `f6aa49a50be11a73c892cbf2f9ac852c52d88ac9e89f1b0c41a9feb18c949fcb`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_unreachable_dynamic_code_and_external_effects_are_retained::root.body[15].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:47`; AST `1e44fa8e4dbd8ebe87b7f6a47c20af23aa8ef176703bec30830b3449dbd7a7c4`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:49`; AST `99f0151ad0dc324c14ee042110e4211e056b66e60c891ef3699b52676f0170cd`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, path, self, source_closure. Outputs/bindings: path.
Calls/effect boundaries: path.read_text, path.write_text, self.assertRaises, source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:50`; AST `5355703578d000a12e60c1361147598b77b813fefd34c5c8b45109deb9be5724`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:51`; AST `3161186181b580b82297e7da720dbfc6b60bb5a942eeae61f4c0b3f7ba097c1b`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:51`; AST `0ffe33a4da3235a5ba43ab9fff25202c6093574ee552dc41103c17094a275b65`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[1].value.args[0].left::Call

Source: `infra/tests/test_roadmap_python.py:51`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[2]::With

Source: `infra/tests/test_roadmap_python.py:52`; AST `aed7f56e628a470f7df2301d5e1ae588e3020c2d28184025c342027d1572123b`.

Rust module: `infra::tests::test_roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises, source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[15].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[2].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python.py:52`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:53`; AST `88a387e70d65267f50950f736635109a10a8c89bf5647c6adbcd37f2707897bb`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonSourceClosureTests::test_shadowed_target_is_not_arbitrarily_selected::root.body[15].body[3].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:53`; AST `9f5fcef1ae4c316723de1c91ab2ed07c3692dd1d2c76f6a09e246284763dbe43`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::root.body[16]::ClassDef

Source: `infra/tests/test_roadmap_python.py:56`; AST `885d458c28cd9f04e240613663a655fb9ec23142c3c37b9ab02b0d03007e6237`.

Rust module: `infra::tests::test_roadmap_python`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: Path, ROOT, all, any, ast, b, backend, base, binding, c, classify_nagini, code, compile, compile_roadmaps, compiled, dict, digest, directory, error, errors, expected, field, json, len, locations, maintained_python, marker, o, observed, original, original_occurrences, os, p, python_proof_errors, qualification, r, record, repr, research_sources, result, root, route, run, run_process, self, shared, stat, str, sys, tempfile, unittest. Outputs/bindings: b, backend, base, binding, c, code, compiled, directory, error, errors, expected, field, locations, marker, o, observed, original, p, qualification, r, record, result, root, run, shared, stat.
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, (shared / 'python-backends.json').write_text, Path, all, any, ast.parse, classify_nagini, compile, compile_roadmaps, compiled['milestones'].values, dict, digest, json.dumps, json.loads, len, maintained_python, marker.read_text, original_occurrences, p.relative_to, p.relative_to(ROOT).as_posix, python_proof_errors, qualification.read_bytes, qualification.write_text, repr, research_sources, route, run_process, self.assertEqual, self.assertFalse, self.assertNotEqual, self.assertTrue, self.subTest, shared.mkdir, stat.exists, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split, str, tempfile.TemporaryDirectory, unittest.skipUnless.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:57`; AST `a6e7dc631689849ab773ab1f2ec5bc113872287decbe7fb5c36c24f6794f5f4a`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, all, b, c, compile_roadmaps, compiled, expected, maintained_python, o, p, record, route, self. Outputs/bindings: b, c, compiled, expected, o, p, record.
Calls/effect boundaries: all, compile_roadmaps, compiled['milestones'].values, maintained_python, p.relative_to, p.relative_to(ROOT).as_posix, route, self.assertEqual, self.assertFalse, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:58`; AST `3c07c0402fa43263ec82c91b4762405ec0038e65db08c76c82a45398d7e61ed1`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, compile_roadmaps. Outputs/bindings: compiled.
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:58`; AST `d1af4336e7af420cac99b4dd6cdf27c0ceea85cd6a7b14065da627f3fa88a4d7`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compile_roadmaps. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python.py:59`; AST `15e22bf0fd94e408452ba6114b72819c9f9352332b5040dd94c792f8e9210d0a`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, compiled, route. Outputs/bindings: record.
Calls/effect boundaries: route.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:59`; AST `45a19298dae01fe8884f5335b07608018d92d3630f586bd507289a512220e55e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compiled, route. Outputs/bindings: (none).
Calls/effect boundaries: route.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python.py:60`; AST `49a73ae211366b1131acced8396c12917f4cd1f3e90126dfe1eb2a28120aac36`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: c, compiled, o. Outputs/bindings: c, expected, o.
Calls/effect boundaries: compiled['milestones'].values.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[2].value::SetComp

Source: `infra/tests/test_roadmap_python.py:60`; AST `7d5334c3ee86dd055f2cffc6b9ad4b4cb059aa8fd6f9f9ae267521b25bef1b08`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: c, compiled, o. Outputs/bindings: c, o.
Calls/effect boundaries: compiled['milestones'].values.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[2].value.generators[0].iter::Call

Source: `infra/tests/test_roadmap_python.py:60`; AST `bf82677a9c080c784f548d714826a2afcc13670e43befb5aba8687cefdedf238`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: compiled. Outputs/bindings: (none).
Calls/effect boundaries: compiled['milestones'].values.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:62`; AST `dfefa36cdaa091fd0ab0c7c6180d2ce60ad2ff7834148ff7415a1e32f8a85cd3`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: expected, o, record, self. Outputs/bindings: o.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:62`; AST `d6181ad7765dac17057b1f376fc389dc739b8fc9a4e2ecb97a7286bb11c3ffc9`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, o, record, self. Outputs/bindings: o.
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[3].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python.py:62`; AST `d514226a42292db7ad432304d570ecd264efe4fca89dc3d19dfe27c406a4d400`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: o, record. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[0].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:63`; AST `d3052ba4b1b5ca239a2af5ec2d1bb872c0b575ea6b2b71ec5c5717dd89cd074d`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, b, maintained_python, p, record, self. Outputs/bindings: b, p.
Calls/effect boundaries: maintained_python, p.relative_to, p.relative_to(ROOT).as_posix, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:63`; AST `3572350be10cfca07eae952ce900f0b050a9feae9e5cce19c23e489c54c1a170`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, b, maintained_python, p, record, self. Outputs/bindings: b, p.
Calls/effect boundaries: maintained_python, p.relative_to, p.relative_to(ROOT).as_posix, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value.args[0]::SetComp

Source: `infra/tests/test_roadmap_python.py:63`; AST `1428d8229e20fbb34644ef705a3ae5671e514dc8d71341e30f931cb8e06b6c2a`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: b, record. Outputs/bindings: b.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[0].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value.args[1]::SetComp

Source: `infra/tests/test_roadmap_python.py:63`; AST `81c2da0494dacae807f4f4fb264e75b1ff2c5f94c5c4a836726e1b218ead7a93`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: ROOT, maintained_python, p. Outputs/bindings: p.
Calls/effect boundaries: maintained_python, p.relative_to, p.relative_to(ROOT).as_posix.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[0].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value.args[1].elt::Call

Source: `infra/tests/test_roadmap_python.py:63`; AST `28336935f2ffb9beb4034e9f4a74d9d09689d9b6100580d9a47f1186879d0836`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(ROOT).as_posix.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[4].value.args[1].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value.args[1].elt.func.value::Call

Source: `infra/tests/test_roadmap_python.py:63`; AST `52c4689aa90c8885d5d4f4c522ca96e9a1a0fcec283f94d1d48c30c21346cfa2`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[4].value.args[1].elt.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[4].value.args[1].generators[0].iter::Call

Source: `infra/tests/test_roadmap_python.py:63`; AST `24d2cd10069a023ccbd0998afdf6d919bc4a740d973aba94221f926d54faf0d7`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, maintained_python. Outputs/bindings: (none).
Calls/effect boundaries: maintained_python.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[4].value.args[1].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python.py:64`; AST `0c0dae326f088f5b0834c1e0c7740420d1581c7af43b67678c4d6f8e5be6db17`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python.py:64`; AST `169af5bf5113d5c5284dac936fff046e28ce599e32b750d4e4550150c48bba92`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python.py:65`; AST `d3dde4505a7c6143dc5a359bdf2d0c88549cec51d1ab8fb2142066478d870b12`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, o, record, self. Outputs/bindings: o.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python.py:65`; AST `fb2ed3330cb0aab7cca4e43868a775d15f21a67da4b780883d333c1dacd001f9`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, o, record, self. Outputs/bindings: o.
Calls/effect boundaries: all, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:65`; AST `4e54f78dfc4aae50289c20c455ef94b7743a18588a7183d600be95103a5f4aee`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, o, record. Outputs/bindings: o.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[6].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_python.py:65`; AST `72856724ca012b2eaacd454b8f4035680379ada671d302b75ff7eeac0f04bc5a`.

Rust module: `infra::tests::test_roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: o, record. Outputs/bindings: o.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[16].body[0].body[6].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python.py:66`; AST `89cf5439dce873be875e4b62e099beff3e03d0d81736c9bf9cf2ed4835c902f4`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_routes_retain_complete_domain_and_source_denominators::root.body[16].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python.py:66`; AST `c5aea6f34065179005c6ded53612872a0d058dcb9d83980ca588242cc5d09a04`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: record, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:68`; AST `41536a3be1e0e1adce7703c3d5a712e8879afd264af8a24f691993fc658c3d74`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, digest, len, record, research_sources, self. Outputs/bindings: record.
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, digest, len, research_sources, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:69`; AST `11dd6041839cf096e108b104743af4b3f9ae9ffe64ddbda400b72d8cf41fe7e5`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, research_sources. Outputs/bindings: record.
Calls/effect boundaries: research_sources.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:69`; AST `0088831d34e35729d8600d77f8f3734adddffc8bcb23a35001713c95f990873d`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, research_sources. Outputs/bindings: (none).
Calls/effect boundaries: research_sources.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:70`; AST `ab3bbca3111d2f512129db54ab844381543c8e9cf52fd906f4f293a2d452d6b8`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:70`; AST `d12df7f53cf09fd33da7cc1ff2c43d836ff4449c2fdd1946c7b79b479ef1df03`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:70`; AST `4128bef57c942afde4eb6a385b90e6b396a7048646593098859a76125b9069e5`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:71`; AST `623dee6767cbd882a6671862b74412528980ce3e339577a40c9e6a6719ad9389`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, record, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:71`; AST `b396cfde93bca790696a2fd7f9bd23c7b05161a2f7ca807959c64e824945f6bc`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:71`; AST `d922bee3a837e8e20c512f8c29006f6b7ae10db6776061f66026866b03964273`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, record. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:72`; AST `9ee474c78b5485ca4171e9ed5168a075f2f8f60566d86d8b6fdf72cad8acf6cc`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, digest, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, digest, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:72`; AST `14d45255a8947c84fee779da12a792d7acdaee4cb21ee08ffa6507f8045d8e00`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, digest, record, self. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, digest, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[3].value.args[1]::Call

Source: `infra/tests/test_roadmap_python.py:72`; AST `0daa6e6c6afd93c8c55ee953e824807cd5eb1979bed65070b1e7388a74ff0ff0`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, digest, record. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes, digest.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_research_archive_denominator_and_original_report_retained::root.body[16].body[1].body[3].value.args[1].args[0]::Call

Source: `infra/tests/test_roadmap_python.py:72`; AST `15ec1f03e2b01ffaf85ac85bbb4d4a78f798f6a02c7af5b9d8196a395d6542ef`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, record. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / record['report']['path']).read_bytes.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[3].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:74`; AST `b1f681460f1ca12b8533c35567d8d389ea6f240bb8c388326125974951b6b803`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, len, locations, original, original_occurrences, r, self. Outputs/bindings: locations, original, r.
Calls/effect boundaries: len, original_occurrences, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:75`; AST `c70e4d493daa5c672c0b9f5ed65f89c0b567f714dd29f929dd402bbae83a4281`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, original_occurrences. Outputs/bindings: locations.
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:75`; AST `a3672af8d48a5ef13d2f72e5c9d63a7dfa51393cb5d86119e7df62f25aa6c153`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, original_occurrences. Outputs/bindings: (none).
Calls/effect boundaries: original_occurrences.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[1]::Assign

Source: `infra/tests/test_roadmap_python.py:76`; AST `9f3957e9259cfccb87cfd85f078633bf319b9d45f7abc191d5af0b0b54303a02`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: locations, r. Outputs/bindings: original, r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[1].value::ListComp

Source: `infra/tests/test_roadmap_python.py:76`; AST `5494ad08797392e5178305d8fa0d41e7fff06de53d8956d4ef308cb1d42a7da4`.

Rust module: `infra::tests::test_roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: locations, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[16].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:77`; AST `42755e5945b8aec27c002f7d05c4695378fcf70e2131b4f16508874fc14e655c`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, original, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:77`; AST `15103e40050f188f6dc34b7f1001d3448fbe56dc78053c48a431e044a6349a70`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, original, self. Outputs/bindings: (none).
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[2].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:77`; AST `a1dc84db2d8ce2128a3659e9e75049bf5e638cb183fa6f0f8955931efd6b4639`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, original. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:78`; AST `05d159254b8675d19ffa8d473fd2b60350c32518dc97a4b0f54cab01541aac18`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: original, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:78`; AST `1bdf1d0f47c14f111931d6761d08e2380ab6fd86141fc1b51f9e183711094ff4`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: original, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:79`; AST `234f503d0b34d3e208a69f6658cd8a8f5ca05f4db7a23e8cb05672fdea02a2a8`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, locations, r, self. Outputs/bindings: r.
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:79`; AST `776d0ef03c20e77e3ab45d32025ec952de158e0412a331dd3bafb544f944c3d6`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, locations, r, self. Outputs/bindings: r.
Calls/effect boundaries: len, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:79`; AST `64ec225c800a57980151227d954864ab02edc7fef95d8d5e5ddb145fccd28c52`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, locations, r. Outputs/bindings: r.
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[4].value.args[0].args[0]::SetComp

Source: `infra/tests/test_roadmap_python.py:79`; AST `15ebd0d277fbd28564c34b9930443056b7321d1357892120a007959bedc28e71`.

Rust module: `infra::tests::test_roadmap_python`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: locations, r. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered SetComp evaluation at root.body[16].body[2].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_static_original_locations_do_not_claim_dynamic_fixture_closure::root.body[16].body[2].body[4].value.args[1]::Call

Source: `infra/tests/test_roadmap_python.py:79`; AST `eb6d7709b9e51c8b7c942324010e2273b5fccb7eb27e7981e5cd01d6c78979a6`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, locations. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:81`; AST `f0c72f1ef9f03127439c176d9f703e512c700342b5c27d29d86a5e2127dc615d`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: base, classify_nagini, dict, field, self. Outputs/bindings: base, field.
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:82`; AST `7464dc39d8e67604b29a8dd7cbd9ae7d3e92f76ce3ca0c1129a308da0cbef6e8`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict. Outputs/bindings: base.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:82`; AST `4ea8c784caa8a6c33239cda9671c814d4455d2121985bcc851fc36d589a86ba8`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:84`; AST `a6c91adf23c62291e17fcf583d3f3062ed34a3fc27bf00fa6b809dc24dab8170`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, classify_nagini, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:84`; AST `21109e3c11b2307d7409dc29757bf84deb1e34f192fc97ad1d38eb7fe1fe1412`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:84`; AST `910af58a5c51b2880d7055e2fdbd43d547401f6af1fb916417c67b1f92a0db33`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[2]::For

Source: `infra/tests/test_roadmap_python.py:85`; AST `e0089d009673c084fc4161402a0aca992b79c822dae6b9d45d71b84809a5725d`.

Rust module: `infra::tests::test_roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: base, classify_nagini, dict, field, self. Outputs/bindings: field.
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[3].body[2]; no call, error or mutation may be omitted. Iteration: field in ('timed_out', 'stdout_truncated', 'stderr_truncated')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[2].body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:86`; AST `d90369ccf37c527d0dfcb8dff2666ff5d5b9cc6d4377bcf64f374ea4af993a21`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, classify_nagini, dict, field, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:86`; AST `d9d178432ca964f172ce132c444c12bff9acf4076086b7198328680e63dff9b2`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict, field, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[2].body[0].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:86`; AST `59b8932162c22af0631fe48448f0edcdba05484d71da7cebcf04a03e08f97f82`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict, field. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[2].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[2].body[0].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:86`; AST `81395f09b8718a6b695e5eed3b358e40ad732776173b5f03e61e08335971f851`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, field. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[2].body[0].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:87`; AST `796c84e8dde3111fd3fb32c8b644be653950a10c46cf6e9f0c1955e71db234fd`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, classify_nagini, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:87`; AST `d0d4ca5782f75b19b285e833ecff4f67075d0ae719009969d03e6a57aebd885d`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[3].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:87`; AST `e79d0f8376f89afe36a2eae75ee64d4e3ad4d8ac661dc772e69dbd297ebf3a37`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[3].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[3].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:87`; AST `13b725c1cb761680df22af683058ec80302e84ed9ada4d33ef45ddce4f86ba16`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[3].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:88`; AST `30f7fee39d96c0b414f22f9e4822d8a186238d70276802f0e1c87d14759c9ef4`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: base, classify_nagini, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:88`; AST `a9662c9d3f8b0ac5d953f6a5ab2d6afc805832bdc1370bd7871cd1c6d6844d3d`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[4].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:88`; AST `a7402bbbe81fe2cadb1b5d231378659c0c7ff490906639ff356525f05858b82e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, classify_nagini, dict. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[4].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_cli_success_text_cannot_hide_unsupported_or_truncated_result::root.body[16].body[3].body[4].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:88`; AST `3a8f4632361852507add4498da5ce0199a3a42d98acfc41c566cb9486af51f54`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].body[4].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:90`; AST `4c28b95ae3c399e0a01419a9d5a5f2200ea183c21caedf4f552e558fe868ef64`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: classify_nagini, dict, run, self. Outputs/bindings: run.
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:91`; AST `adb1d3825e852f7386ae6210707a8773402a1817dbc021d8ba68c4bc61022e01`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict. Outputs/bindings: run.
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:91`; AST `7b1bb2e51dd42c325a8465b898b2fd7ed75d5e6d6dd4797fd25bb6c7137e00f9`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:92`; AST `6b704ea931731cba2c60a622d1f52bd1e1f7c9e0c6af109093c6b8578d80f624`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_nagini, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:92`; AST `1fb84dfd305a90a7991c9a3d7146980e5fa1817178868ffbe415afe0a3187bbd`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_nagini, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[1].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:92`; AST `cd48f2ce8b6151947c6c5e27bf676288879df38d571ea18b73ca9d2394753b09`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_nagini, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[1].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:93`; AST `eaa3c41bf841a2543a0e48453201dcaeff4f0ea125770e6c9c30ba3c215147ab`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: classify_nagini, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:93`; AST `a88b29451760baac51db46ac9184c4b21dc9603ac9a48c8143f668debf483963`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_nagini, dict, run, self. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[2].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:93`; AST `ec977126008795fadc04067589afc2b8b27e977aaab806f9b5a5c26b769be71c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: classify_nagini, dict, run. Outputs/bindings: (none).
Calls/effect boundaries: classify_nagini, dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[2].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_failed_import_is_not_a_successful_negative_control::root.body[16].body[4].body[2].value.args[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:93`; AST `9689f0eb33f2b875516d42ae71cdfd64742caf6a17b62513433e1fa181d59d33`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, run. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].body[2].value.args[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:95`; AST `0f8a201fda79be64737a854897df3d16bfbda2be009174803cfc266392b95764`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, backend, python_proof_errors, self. Outputs/bindings: backend.
Calls/effect boundaries: python_proof_errors, self.assertEqual, self.assertTrue, self.subTest.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0]::For

Source: `infra/tests/test_roadmap_python.py:96`; AST `e58bdfa0a1dcd81267f4bedb337dc28118b39c08944cfb036bde34c5a9bc3756`.

Rust module: `infra::tests::test_roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, backend, python_proof_errors, self. Outputs/bindings: backend.
Calls/effect boundaries: python_proof_errors, self.assertTrue, self.subTest.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered For evaluation at root.body[16].body[5].body[0]; no call, error or mutation may be omitted. Iteration: backend in ('nagini', 'esbmc-python', 'deal')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0].body[0]::With

Source: `infra/tests/test_roadmap_python.py:97`; AST `9360d84f38d320a899c79536633698548f3b17c589ea584598100fbcae6544c3`.

Rust module: `infra::tests::test_roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ROOT, backend, python_proof_errors, self. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors, self.assertTrue, self.subTest.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[16].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python.py:97`; AST `51c8e43c5465cd46957f65c1f7e3f09f7eea75921ce5f558013094635d6efa8e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: backend, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:98`; AST `87ba1eea752f72e5f11ccaadf3f9c3c4f7f788d280a8be3cac1d236d914a548e`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, backend, python_proof_errors, self. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:98`; AST `ada4f445b754bb2c75576818373c6462a1224741672f3463b2d6d7c513691ef3`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, backend, python_proof_errors, self. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[0].body[0].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:98`; AST `9b5b7f357c78b20b6cb0a72841c57c52dbc6d9734ab9ae6bbe2da1767db9d837`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, backend, python_proof_errors. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[1]::Expr

Source: `infra/tests/test_roadmap_python.py:99`; AST `4dc9e574e10f0eb494ca24b3ba9ec31dc5f8e89470d8d2e643b4557b9e88dab7`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, python_proof_errors, self. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[1].value::Call

Source: `infra/tests/test_roadmap_python.py:99`; AST `e482b0136ffc9bebc6666f3a7a02ae76cc8e219131712960f78a72225dddcd7b`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, python_proof_errors, self. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors, self.assertEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_unqualified_python_backend_rejects_synthetic_proved_claim::root.body[16].body[5].body[1].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:99`; AST `e86954adea07d10b7beec9a516d7bc3b1509b9ca7e5abeb1a3ac71eab5e770cd`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, python_proof_errors. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:101`; AST `6ab8daa7480ffe50d6c9816255feed82fc4b90e39753d6b759e77c802b9421f1`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, any, binding, digest, directory, error, errors, json, python_proof_errors, qualification, root, self, shared, tempfile. Outputs/bindings: binding, directory, error, errors, qualification, root, shared.
Calls/effect boundaries: (shared / 'python-backends.json').write_text, Path, any, digest, json.dumps, python_proof_errors, qualification.read_bytes, qualification.write_text, self.assertTrue, shared.mkdir, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0]::With

Source: `infra/tests/test_roadmap_python.py:102`; AST `d6165eadc4fc7f218771e99bec4edbf33339681b292bec89515e85e5b7137fb3`.

Rust module: `infra::tests::test_roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, any, binding, digest, directory, error, errors, json, python_proof_errors, qualification, root, self, shared, tempfile. Outputs/bindings: binding, directory, error, errors, qualification, root, shared.
Calls/effect boundaries: (shared / 'python-backends.json').write_text, Path, any, digest, json.dumps, python_proof_errors, qualification.read_bytes, qualification.write_text, self.assertTrue, shared.mkdir, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[16].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python.py:102`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:103`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:103`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python.py:104`; AST `3380eb1c18d4dd87a0367b29694513b14611664db9c44eab6e802c537b35b080`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: shared.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_python.py:105`; AST `d20d143f38d9b5d82545abe3ef1d2ca636f603d0a2b93ac41056e250c71735d1`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_python.py:105`; AST `99bcba72db0838f639a464854466bfa2acd0fe9e260d2d59c8e8247715d94a84`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: shared. Outputs/bindings: (none).
Calls/effect boundaries: shared.mkdir.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_python.py:106`; AST `d279058246f39fc12670cdcb4fad6ae1581904121d0f90e44be58d07dbea3515`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: shared. Outputs/bindings: qualification.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_python.py:107`; AST `baa2f311673a5bb13f6f0aa4c4711ad53248034093b4c524e89a56826d8973e0`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, qualification. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, qualification.write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:107`; AST `89fcab93a613e2310359005c6c450b50903a9cceeb71b1d7bc246e41bd87242c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, qualification. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, qualification.write_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:107`; AST `4099511ccdb18b9f4c5112db8b4198d9d8338f93b9c455d17cd4162b637635ae`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_python.py:108`; AST `5c27b6bce3aca451ab49ac7a2aa4fdfa69cab883040ee779fd023d69e3c6e72a`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, qualification. Outputs/bindings: binding.
Calls/effect boundaries: digest, qualification.read_bytes.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[5].value.values[1]::Call

Source: `infra/tests/test_roadmap_python.py:108`; AST `af3accf52135fd7b8ad74040b9a808debc8b7c7047a6988c1fc484b64d043fbf`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, qualification. Outputs/bindings: (none).
Calls/effect boundaries: digest, qualification.read_bytes.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[5].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[5].value.values[1].args[0]::Call

Source: `infra/tests/test_roadmap_python.py:108`; AST `3fde3d6e87a6940de57d87d784c33be10e8c679aabb1e87ffd9caff7d5028eba`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: qualification. Outputs/bindings: (none).
Calls/effect boundaries: qualification.read_bytes.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[5].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_python.py:109`; AST `4117f066d6ae0dc7e19f1f4b6c428158ea4da5fd9f0eb3c94422f137c6c1aa91`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, json, shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'python-backends.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python.py:109`; AST `81ed53b15a3820f438d44bcf2650f7b97ac63ccedf11d402a0e4ec4d3120fce8`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, json, shared. Outputs/bindings: (none).
Calls/effect boundaries: (shared / 'python-backends.json').write_text, json.dumps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:109`; AST `e2511ac5189b2e740560cb9189189c0c23715d390dd3e309eb024ec82bed104f`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[7]::Assign

Source: `infra/tests/test_roadmap_python.py:110`; AST `34a82e4e9f9f0082bc8920a35ce13b7609b0007768b7ca1b922f293d857b19d6`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: binding, python_proof_errors, root. Outputs/bindings: errors.
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[6].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python.py:110`; AST `cbc8c6c12ece13878361fe7a50eb667995d032e12d549c4cdf4491edb8764c6e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: binding, python_proof_errors, root. Outputs/bindings: (none).
Calls/effect boundaries: python_proof_errors.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_python.py:111`; AST `ca28200419840cddaafe84a7d032701a4e3d89a9e8b2cfba9911e2d1092e6357`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, error, errors, self. Outputs/bindings: error.
Calls/effect boundaries: any, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_python.py:111`; AST `06fa5f8ec74509d8862653218f6f345b2c986d9ecc567e45e1a85b575f6e1e80`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, error, errors, self. Outputs/bindings: error.
Calls/effect boundaries: any, self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:111`; AST `87f5399bcb9ddd337415b65e3d5d19b7b1121671351ed06128ceddb5ffc68a0b`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, error, errors. Outputs/bindings: error.
Calls/effect boundaries: any.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].body[0].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_merely_editing_matrix_cannot_qualify_an_execution_adapter::root.body[16].body[6].body[0].body[8].value.args[0].args[0]::GeneratorExp

Source: `infra/tests/test_roadmap_python.py:111`; AST `aa720e02b59d778630d31d0df836d71c822491bb02a866695e9e7546295ca658`.

Rust module: `infra::tests::test_roadmap_python`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: error, errors. Outputs/bindings: error.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[16].body[6].body[0].body[8].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_python.py:114`; AST `4bc67071032924ed5c787f7b931c4d14c81877def6e20f6b7363d7573193e1ce`.

Rust module: `infra::tests::test_roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, ast, code, compile, directory, json, marker, observed, os, repr, result, root, run_process, self, stat, str, sys, tempfile, unittest. Outputs/bindings: code, directory, marker, observed, result, root, stat.
Calls/effect boundaries: Path, ast.parse, compile, json.loads, marker.read_text, repr, run_process, self.assertEqual, self.assertNotEqual, self.assertTrue, stat.exists, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split, str, tempfile.TemporaryDirectory, unittest.skipUnless.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0]::With

Source: `infra/tests/test_roadmap_python.py:115`; AST `2fd2945219d6c6ad8993bf089544dc583a79f1be6d9feda2faade5795a7393c3`.

Rust module: `infra::tests::test_roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, ROOT, ast, code, compile, directory, json, marker, observed, repr, result, root, run_process, self, stat, str, sys, tempfile. Outputs/bindings: code, directory, marker, observed, result, root, stat.
Calls/effect boundaries: Path, ast.parse, compile, json.loads, marker.read_text, repr, run_process, self.assertEqual, self.assertNotEqual, self.assertTrue, stat.exists, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split, str, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered With evaluation at root.body[16].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_python.py:115`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_python.py:116`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:116`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_python.py:117`; AST `e851dfaf70a40fba5518c5eccc1c10badff8ee3d7f50efe3186865689f88a32d`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: marker.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_python.py:118`; AST `6516177b742a5e9f55027ae570211a197c7e0d7a4f34a7fd83b1a60d3abd397c`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, marker, repr, root, str. Outputs/bindings: code.
Calls/effect boundaries: repr, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.left.left.left.left.right::Call

Source: `infra/tests/test_roadmap_python.py:118`; AST `33dad3440ab1c037eeb48c5ac8d56b62a69233587629e972f23fa758a46c5b39`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, repr, str. Outputs/bindings: (none).
Calls/effect boundaries: repr, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.left.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.left.left.left.left.right.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:118`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.left.left.left.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.left.left.right::Call

Source: `infra/tests/test_roadmap_python.py:120`; AST `075b99761dc2713983487b4a2e31e809b18657a065810bb9fbbaaf784f846174`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker, repr, str. Outputs/bindings: (none).
Calls/effect boundaries: repr, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.left.left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.left.left.right.args[0].left.right::Call

Source: `infra/tests/test_roadmap_python.py:120`; AST `d34c3b8b0f639960bfa05f63246a646eb93f22116fb4f4a5dce4d0b6618537dc`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker, repr, str. Outputs/bindings: (none).
Calls/effect boundaries: repr, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.left.left.right.args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.left.left.right.args[0].left.right.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:120`; AST `f20a9064b0ce02bdb5745bef7083af8623b7bfac815eba337b07fbbdc186f393`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.left.left.right.args[0].left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.right::Call

Source: `infra/tests/test_roadmap_python.py:120`; AST `caf521c3ae0ac2550d205cbc5d7e25a5efab87713697798208079810505f0486`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: repr, root, str. Outputs/bindings: (none).
Calls/effect boundaries: repr, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[2].value.left.right.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:120`; AST `0558894338b4e37e4aaf64136b1647fc227573a783699714f1608da395993d9a`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[2].value.left.right.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[3]::Expr

Source: `infra/tests/test_roadmap_python.py:121`; AST `9a00555281025cb25f7a4d5c4a0c63d67b03eb2dad1d552f25b58e5387adf032`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ast, code, compile. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, compile.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[3].value::Call

Source: `infra/tests/test_roadmap_python.py:121`; AST `a47d2696f0e9dedec4ac2dd8088ab98076d606940f242410500919cc97616c76`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, code, compile. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse, compile.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[3].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:121`; AST `48c199cd6a199217abf6af7dee1abfc15f5b06ae7ed53c17515437a9f2295310`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ast, code. Outputs/bindings: (none).
Calls/effect boundaries: ast.parse.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[4]::Assign

Source: `infra/tests/test_roadmap_python.py:122`; AST `43a0301c23032a73ad89c1871e3eb3ff7d2d980c1b35f4e94bf460f0909e9f31`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: code, root, run_process, sys. Outputs/bindings: result.
Calls/effect boundaries: run_process.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_python.py:122`; AST `be6f980a94e512ecc0d1bef0e16c1ff48e4f69e95ad786ec0e0547f5a26ad87f`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: code, root, run_process, sys. Outputs/bindings: (none).
Calls/effect boundaries: run_process.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_python.py:123`; AST `98c214209841c95c51f4f8f55f505c00553bc47246e647fe8e422ff276ee39ed`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_python.py:123`; AST `78e0b5edbd417e5c9fdf79556a4d461c5033714e65aae179bea12dbfc1fbb87d`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_python.py:124`; AST `df2e037c53c540c341e6e21982bf46f12ccfc9151bbabc4a7d8f54c3f333e20a`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, marker. Outputs/bindings: observed.
Calls/effect boundaries: json.loads, marker.read_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_python.py:124`; AST `a8c67e19b0ab02b4915e1d42b4d16711a5ab881ce114691909911e6e5d98932c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, marker. Outputs/bindings: (none).
Calls/effect boundaries: json.loads, marker.read_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_python.py:124`; AST `9a040b4676459d368f48b4c84d80701dee6b140b5424dad580e8efffc8dd652e`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker. Outputs/bindings: (none).
Calls/effect boundaries: marker.read_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_python.py:125`; AST `249c475f87c055fbb23266341ad2c0a8b2cfcd145626e6a544a9dd2e62d686f8`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_python.py:125`; AST `5c9ad80ed0deab3c4a8952c93fef31db4939137e0b4ea0a7f5edbc4380eaa79c`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertNotEqual.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[8]::Assign

Source: `infra/tests/test_roadmap_python.py:126`; AST `09ba8d17f7d0767045d2355c554897b640c2136e9d35cdf0627b95a1a36d2a1b`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, observed, str. Outputs/bindings: stat.
Calls/effect boundaries: Path, str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[7].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[8].value.left.left::Call

Source: `infra/tests/test_roadmap_python.py:126`; AST `5479588d3d91c5f0127b92c0f2259521a422a7d01cd28fff7b5c0b9f0082f883`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[8].value.left.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[8].value.left.right::Call

Source: `infra/tests/test_roadmap_python.py:126`; AST `8b40c63d7cfb073389ebea87657cd32fdf2bb4b9c0a5e9fa6e2750e08ef8a287`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[8].value.left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9]::If

Source: `infra/tests/test_roadmap_python.py:127`; AST `ed4db4c7376fb273430d64670570fae1d41369a03dd9e3b90daeae39c3cebdd2`.

Rust module: `infra::tests::test_roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, stat.exists, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[16].body[7].body[0].body[9]; no call, error or mutation may be omitted. Condition: stat.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].test::Call

Source: `infra/tests/test_roadmap_python.py:127`; AST `efcf2cf8e203def56c80567132c737c0bb06338aa2791adc08e01fcdeb6b5691`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.exists.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[9].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:128`; AST `3835b7974878d6acbb58978e33ce8ee6e585b73d9c51b06270dfbc55c4cff2af`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7].body[0].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:128`; AST `95f5e661f0de3672f512413879bd582d5d572f17648946eaf235951d254f6c83`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, stat. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].body[0].value.args[0].value::Call

Source: `infra/tests/test_roadmap_python.py:128`; AST `2b7bffcd92e4bfced04afd9c7ed6aad53c2250947a3a12715539a1e5b3929acc`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.read_text, stat.read_text().rsplit, stat.read_text().rsplit(')', 1)[1].split.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[9].body[0].value.args[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].body[0].value.args[0].value.func.value.value::Call

Source: `infra/tests/test_roadmap_python.py:128`; AST `1fa44458dc4495028a422392a38c11ee2f9161fb4e790dad3e3818bb85dc4d47`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.read_text, stat.read_text().rsplit.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[9].body[0].value.args[0].value.func.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].body[0].body[9].body[0].value.args[0].value.func.value.value.func.value::Call

Source: `infra/tests/test_roadmap_python.py:128`; AST `59005d6dd388baf964fcf4d06b4d2a327d0b3febef52e994df9cfb53dd3b9ca7`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.read_text.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].body[0].body[9].body[0].value.args[0].value.func.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::PythonQualificationTests::test_outer_timeout_cleans_inherited_nested_stage::root.body[16].body[7].decorator_list[0]::Call

Source: `infra/tests/test_roadmap_python.py:113`; AST `985aa26757eb775d72aabcfbe238dcfdb953069caac3158a02d2f37133c59fdf`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.skipUnless.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].decorator_list[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[17]::If

Source: `infra/tests/test_roadmap_python.py:131`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered If evaluation at root.body[17]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[17].body[0]::Expr

Source: `infra/tests/test_roadmap_python.py:132`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_python.py::module::root.body[17].body[0].value::Call

Source: `infra/tests/test_roadmap_python.py:132`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_portability, agentinfra.roadmap_python, agentinfra.roadmap_records, ast, json, os, pathlib, sys, tempfile, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; rustpython_parser or validated Python AST bridge
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
