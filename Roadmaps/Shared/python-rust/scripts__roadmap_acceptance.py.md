# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 172. Inventory digest: `b7d832566bf12cadc88ed093606c5a0d9f06a3ee35eccee694e040b37bd7ac72`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_acceptance.py::module::root::Module

Source: `scripts/roadmap_acceptance.py:1`; AST `6a92b7ae4ebfcbd71c00ecc8a120c53278ab8718f74c4cf2c4599c0e84e8fbc6`.

Rust module: `scripts::roadmap_acceptance`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: HOST_EXCLUSIONS, Path, ROOT, RecordedResult, SystemExit, __doc__, __file__, __name__, accepted, all, argparse, args, atomic_write_json, authority_inventory, bool, candidate, confined_path, dict, digest, err, expected, file_binding, flatten, getattr, isinstance, kwargs, len, list, main, module, modules, name, occurrences, p, parser, print, reason, reconcile_inventory, reconciliation, record, result, row, save_inventory, saved, self, set, snapshot, sorted, sources, str, subtest, suite, super, sys, test, tests, unittest. Outputs/bindings: HOST_EXCLUSIONS, ROOT, accepted, args, expected, module, modules, name, occurrences, p, parser, reconciliation, record, result, row, saved, snapshot, sources, suite, test.
Calls/effect boundaries: (ROOT / 'infra/tests').rglob, HOST_EXCLUSIONS.get, Path, Path(__file__).resolve, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, SystemExit, all, argparse.ArgumentParser, atomic_write_json, authority_inventory, bool, confined_path, digest, file_binding, flatten, getattr, isinstance, len, list, main, name.startswith, p.relative_to, p.relative_to(ROOT).as_posix, parser.add_argument, parser.parse_args, print, reconcile_inventory, result.occurrences.values, result.wasSuccessful, row.get, save_inventory, self.occurrences.setdefault, self.occurrences.setdefault(test.id(), {'id': test.id()}).update, self.occurrences[test.id()].setdefault, self.occurrences[test.id()].setdefault('subtests', []).append, set, sorted, str, super, super().__init__, super().addError, super().addExpectedFailure, super().addFailure, super().addSkip, super().addSubTest, super().addSuccess, super().addUnexpectedSuccess, super().startTest, sys.modules.copy, sys.modules.copy().items, sys.path.insert, test.id, tests, unittest.TextTestRunner, unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run, unittest.defaultTestLoader.discover.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[0]::Expr

Source: `scripts/roadmap_acceptance.py:1`; AST `f552e46899c62868e7b0a710c749127dec982d9e5d151a7575592c7c70bf0b61`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[1]::ImportFrom

Source: `scripts/roadmap_acceptance.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[2]::Import

Source: `scripts/roadmap_acceptance.py:4`; AST `356e6775028bc09e699d8b986887aaebc5e3e8e414a507fe911e3ba7da1264d9`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[3]::ImportFrom

Source: `scripts/roadmap_acceptance.py:5`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[4]::Import

Source: `scripts/roadmap_acceptance.py:6`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[5]::Import

Source: `scripts/roadmap_acceptance.py:7`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[6]::Assign

Source: `scripts/roadmap_acceptance.py:9`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[6].value.value.value::Call

Source: `scripts/roadmap_acceptance.py:9`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[6].value.value.value.func.value::Call

Source: `scripts/roadmap_acceptance.py:9`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[6].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[7]::Expr

Source: `scripts/roadmap_acceptance.py:10`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[7].value::Call

Source: `scripts/roadmap_acceptance.py:10`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[7].value.args[1]::Call

Source: `scripts/roadmap_acceptance.py:10`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[7].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[8]::ImportFrom

Source: `scripts/roadmap_acceptance.py:11`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[9]::ImportFrom

Source: `scripts/roadmap_acceptance.py:12`; AST `a23fabf8627d93bc33005193098baf9280ce9279a57105fd03837ec7324cff1a`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[10]::ImportFrom

Source: `scripts/roadmap_acceptance.py:13`; AST `32e526b08ff1955a80f6d151d3eb295d985718fd117a315adbc46d9642a5c59d`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[11]::ImportFrom

Source: `scripts/roadmap_acceptance.py:14`; AST `860451982277a7f5c435b7fc36a0eb328ab43d13fe8858ce9091906ca6dcc079`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[12]::Assign

Source: `scripts/roadmap_acceptance.py:17`; AST `52b8ce51e91a9fd9f1ecccec08788b960145dcb77c32b8a7ca1e005ac01b5fa6`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: HOST_EXCLUSIONS.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13]::FunctionDef

Source: `scripts/roadmap_acceptance.py:25`; AST `5f199fdcc24f674ca41c8beb4580f5137e5657e1335b7f1c15041837703d6a91`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: flatten, isinstance, suite, test, unittest. Outputs/bindings: test.
Calls/effect boundaries: flatten, isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0]::For

Source: `scripts/roadmap_acceptance.py:26`; AST `91f535b79c35e12edd3ef3a1291050b989cb15cefab124cc09b9303b3e8019c2`.

Rust module: `scripts::roadmap_acceptance`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: flatten, isinstance, suite, test, unittest. Outputs/bindings: test.
Calls/effect boundaries: flatten, isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered For evaluation at root.body[13].body[0]; no call, error or mutation may be omitted. Iteration: test in suite
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0].body[0]::If

Source: `scripts/roadmap_acceptance.py:27`; AST `54c78683d89e47c93cf97073735bed53f71906252023ea59cdeae49890d4d8eb`.

Rust module: `scripts::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: flatten, isinstance, test, unittest. Outputs/bindings: (none).
Calls/effect boundaries: flatten, isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered If evaluation at root.body[13].body[0].body[0]; no call, error or mutation may be omitted. Condition: isinstance(test, unittest.TestSuite)
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0].body[0].test::Call

Source: `scripts/roadmap_acceptance.py:27`; AST `8fc52e892682555d02a90ac8e7125d6c1dfff2a67ecf8e23b9b621c8565d10dd`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, test, unittest. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0].body[0].body[0]::Expr

Source: `scripts/roadmap_acceptance.py:28`; AST `695fbf27b39e32f74dee14d7b1d8b0610267389365fd566f9e71f67341087bd0`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: flatten, test. Outputs/bindings: (none).
Calls/effect boundaries: flatten.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0].body[0].body[0].value.value::Call

Source: `scripts/roadmap_acceptance.py:28`; AST `72d55253a869bc28808be280bb737d6252f139339dfac44423a557ed452c4b51`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flatten, test. Outputs/bindings: (none).
Calls/effect boundaries: flatten.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].body[0].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::flatten::root.body[13].body[0].body[0].orelse[0]::Expr

Source: `scripts/roadmap_acceptance.py:30`; AST `9f74a410c72a348341a66f7d0769ddf47b7e43cc8bda9e9c954c13a467b4b926`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0].body[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::root.body[14]::ClassDef

Source: `scripts/roadmap_acceptance.py:33`; AST `926feb22cb91a050daa350980cddbd8ccbeb94d9556ebd9dfaa75dcaecafea20`.

Rust module: `scripts::roadmap_acceptance`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: HOST_EXCLUSIONS, args, err, kwargs, reason, self, str, subtest, super, test, unittest. Outputs/bindings: (none).
Calls/effect boundaries: HOST_EXCLUSIONS.get, self.occurrences.setdefault, self.occurrences.setdefault(test.id(), {'id': test.id()}).update, self.occurrences[test.id()].setdefault, self.occurrences[test.id()].setdefault('subtests', []).append, str, super, super().__init__, super().addError, super().addExpectedFailure, super().addFailure, super().addSkip, super().addSubTest, super().addSuccess, super().addUnexpectedSuccess, super().startTest, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ClassDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::__init__::root.body[14].body[0]::FunctionDef

Source: `scripts/roadmap_acceptance.py:34`; AST `c829c5603332a48931afbe06f449b17bf77b7ff85449dfe0f9a221ba492c2302`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: args, kwargs, self, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::__init__::root.body[14].body[0].body[0]::Expr

Source: `scripts/roadmap_acceptance.py:35`; AST `635ea7d92f8e9144948685667f5feb06123a9625ad20d4bd5737914a9af40560`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, kwargs, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::__init__::root.body[14].body[0].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:35`; AST `7d8a81412703a68419d654c517d645ac77b261060ab45a7cc8ae1f9de881953f`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, kwargs, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::__init__::root.body[14].body[0].body[0].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:35`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::__init__::root.body[14].body[0].body[1]::Assign

Source: `scripts/roadmap_acceptance.py:36`; AST `4c50fa2b8cf84576b967d4df62da4e02a66943f24088f419f5629ab029feee58`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1]::FunctionDef

Source: `scripts/roadmap_acceptance.py:38`; AST `c4744e29fd67351dda76811d37f0f0d382140c82d181fc99109259fd9d9178c9`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().startTest, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:39`; AST `96b5332d617d1f5cbb82fda7c489f2c87c5452082ce116fca628522fabe94874`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[0].targets[0].slice::Call

Source: `scripts/roadmap_acceptance.py:39`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].targets[0].slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[0].value.values[0]::Call

Source: `scripts/roadmap_acceptance.py:39`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:40`; AST `df050aee81a6a1c24dfb798610e7e03f368ba0aa47605fe8120608eeec239d1d`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().startTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:40`; AST `ff42cbd55ab3d9a6aad4c37b172533f6d3ba27994aca2f424a2130dcb0a6803f`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().startTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::startTest::root.body[14].body[1].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:40`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2]::FunctionDef

Source: `scripts/roadmap_acceptance.py:42`; AST `d430ba1b71f7a3807baab149b1fa6bf091afd4befc3d19d988320eb4061b7040`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSuccess, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:43`; AST `188e180b2c6ce87fd16fe225b7177e638ab321545c8c84c9ae459e34d181eabd`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2].body[0].targets[0].value.slice::Call

Source: `scripts/roadmap_acceptance.py:43`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].targets[0].value.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:44`; AST `461cce933e28fadf5cc06f55af1e9eb4dab6585acf677f7ae2842e828ded3143`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSuccess.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:44`; AST `5b1c546376650d9a0c41024829fc93c36fcda23496bdbbfd1bfed3ca2c57f2a1`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSuccess.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSuccess::root.body[14].body[2].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:44`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3]::FunctionDef

Source: `scripts/roadmap_acceptance.py:46`; AST `1beefdae4d3d6783372658e9bded9a942359f5b5bea39e6b64ad3c79cdf066f9`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: err, self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, super, super().addFailure, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:47`; AST `efd8952c2ea8fb0a0c9d600868130130fe03acb4fd82427f94a13a0d2c81f851`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[0].targets[0].value::Call

Source: `scripts/roadmap_acceptance.py:47`; AST `f596717deb73421a5de089303df6e88a02987820f7172b7c85e2a5400cc7f82a`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].targets[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[0].targets[0].value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:47`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].targets[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[0].targets[0].value.args[1].values[0]::Call

Source: `scripts/roadmap_acceptance.py:47`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[0].targets[0].value.args[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:48`; AST `3ce696164f5c1c58ba74d4c6a6e00228bf91582baf30d4a2e9cc5679160a9b67`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addFailure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:48`; AST `adbcb6f8820cea384a9f224a3ff20c7e52999049e28fa0f2753a0ebeb7711241`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addFailure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addFailure::root.body[14].body[3].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:48`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4]::FunctionDef

Source: `scripts/roadmap_acceptance.py:50`; AST `69221e4c028368a46716c10b33a01193932497b445ae905a39ad374ba1f26ac0`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: err, self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, super, super().addError, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:51`; AST `12fa8dd46d23340ce29ab75bf01bb54ba03e80846a793057799b47b525e2ac8c`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[0].targets[0].value::Call

Source: `scripts/roadmap_acceptance.py:51`; AST `f596717deb73421a5de089303df6e88a02987820f7172b7c85e2a5400cc7f82a`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].targets[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[0].targets[0].value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:51`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].targets[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[0].targets[0].value.args[1].values[0]::Call

Source: `scripts/roadmap_acceptance.py:51`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[0].targets[0].value.args[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:52`; AST `7570721e9f11a44c4cf8b8f8349b15636ba61bf03291c34b59f985f9fe90d05d`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:52`; AST `66006232720a10b2e7ac2c5cc6d43c8bf4a5a1dae7f58b69902f1f17003a5de0`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addError.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addError::root.body[14].body[4].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:52`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5]::FunctionDef

Source: `scripts/roadmap_acceptance.py:54`; AST `8c87a0cd8dc98e4deb127611c5e8bc607a761934eb8e6d26d2d6dcdea37974db`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: HOST_EXCLUSIONS, reason, self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: HOST_EXCLUSIONS.get, self.occurrences.setdefault, self.occurrences.setdefault(test.id(), {'id': test.id()}).update, super, super().addSkip, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0]::Expr

Source: `scripts/roadmap_acceptance.py:55`; AST `f3fbbe493f6f57b208f32ab415771f80d9cb3145bcc0e4d84eaff9bc0849e22b`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: HOST_EXCLUSIONS, reason, self, test. Outputs/bindings: (none).
Calls/effect boundaries: HOST_EXCLUSIONS.get, self.occurrences.setdefault, self.occurrences.setdefault(test.id(), {'id': test.id()}).update, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:55`; AST `75179f57c151f4ccb2d25bfe53ff912338c35e61e5acd765f078a39306d0b554`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: HOST_EXCLUSIONS, reason, self, test. Outputs/bindings: (none).
Calls/effect boundaries: HOST_EXCLUSIONS.get, self.occurrences.setdefault, self.occurrences.setdefault(test.id(), {'id': test.id()}).update, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:55`; AST `f596717deb73421a5de089303df6e88a02987820f7172b7c85e2a5400cc7f82a`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences.setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value.func.value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:55`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value.func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value.func.value.args[1].values[0]::Call

Source: `scripts/roadmap_acceptance.py:55`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value.func.value.args[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value.keywords[2].value.left::Call

Source: `scripts/roadmap_acceptance.py:56`; AST `85320410604eaa1f049d0dfad789da04584e375926130a7d7c335fb5cf695883`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: HOST_EXCLUSIONS, test. Outputs/bindings: (none).
Calls/effect boundaries: HOST_EXCLUSIONS.get, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value.keywords[2].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[0].value.keywords[2].value.left.args[0]::Call

Source: `scripts/roadmap_acceptance.py:56`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[0].value.keywords[2].value.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:57`; AST `4a0ad56366cccabd2e913bfcaee6eff5a0ce74844a376a93f9ba7092a1a2e03f`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: reason, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSkip.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:57`; AST `f43ca999bf0bcf76d663807525b76a7b61a9eae197e8ce393b7f8e32850e3ed6`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: reason, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSkip.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSkip::root.body[14].body[5].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:57`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6]::FunctionDef

Source: `scripts/roadmap_acceptance.py:59`; AST `4dd5878bad2090d857cbeddcfe7fa2f61b87317df44966036e590646f1830bd3`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: err, self, str, subtest, super, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences[test.id()].setdefault, self.occurrences[test.id()].setdefault('subtests', []).append, str, super, super().addSubTest, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[0]::Expr

Source: `scripts/roadmap_acceptance.py:60`; AST `59ccd8c44383c253cf164c25cfb00820fc4dbeb6055b46bbbe8accdca20d439f`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: err, self, str, subtest, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences[test.id()].setdefault, self.occurrences[test.id()].setdefault('subtests', []).append, str, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:60`; AST `e7c1031a8a74ccf789e0b9ab492b6839534bffe6e5bae9046169fe3d34769cae`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: err, self, str, subtest, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences[test.id()].setdefault, self.occurrences[test.id()].setdefault('subtests', []).append, str, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[0].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:60`; AST `3ecf5a202cc678eed650ce357abc4c2819d598f0c7e12f6013277066ed32d8a0`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: self.occurrences[test.id()].setdefault, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[0].value.func.value.func.value.slice::Call

Source: `scripts/roadmap_acceptance.py:60`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.func.value.func.value.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[0].value.args[0].values[0]::Call

Source: `scripts/roadmap_acceptance.py:60`; AST `f1f2c29b1f4f8926a3834cc28e75e409ba95d8311da4e31ef67dfa2160197d36`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, subtest. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[1]::If

Source: `scripts/roadmap_acceptance.py:61`; AST `787a17d7a0ca2baf3ff03b830bc543c6147b12f438f24d23576b08a6a7324f86`.

Rust module: `scripts::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: err, self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered If evaluation at root.body[14].body[6].body[1]; no call, error or mutation may be omitted. Condition: err is not None
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[1].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:62`; AST `0dd3512f8d7bae86156da7abc64de3c12edee6a2b158c67338058282c6bb7ef1`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[1].body[0].targets[0].value.slice::Call

Source: `scripts/roadmap_acceptance.py:62`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[1].body[0].targets[0].value.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[2]::Expr

Source: `scripts/roadmap_acceptance.py:63`; AST `4c379290125672e9211948fdff91c7cb5cfebe289f4843d35fabc951d5d448da`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: err, subtest, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSubTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[2].value::Call

Source: `scripts/roadmap_acceptance.py:63`; AST `ede473d0509bdc317b55f01aa988f6746a67320c6eb7a4674f02b7798b0f77ce`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: err, subtest, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addSubTest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addSubTest::root.body[14].body[6].body[2].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:63`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7]::FunctionDef

Source: `scripts/roadmap_acceptance.py:65`; AST `aa0fb8561fb90f86f3923c7b69e06b44972dd16e6c170539d173ec170884755b`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: err, self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addExpectedFailure, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:66`; AST `c5c2fd9a979202fc3efbb6769776103747131c682eed0d04a5ce02fc8b639748`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7].body[0].targets[0].value.slice::Call

Source: `scripts/roadmap_acceptance.py:66`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[0].targets[0].value.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:67`; AST `ce294097c2794491763cc428314206f26ed0eda486641ff13160e3474bde97c5`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addExpectedFailure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:67`; AST `491f016b11d934b156f1ed6b35f5615ec9c72186453fc9d4f346f224347ea680`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: err, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addExpectedFailure.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addExpectedFailure::root.body[14].body[7].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:67`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[7].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8]::FunctionDef

Source: `scripts/roadmap_acceptance.py:69`; AST `207bc73168d512ae3c3b2258fdf530a320157536027d06ddf0cbbc03fccd8662`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: self, super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addUnexpectedSuccess, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:70`; AST `d56512f85fca175bfd13238dd14d24a38569a1b89c17da58644b0d5187fc9234`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8].body[0].targets[0].value.slice::Call

Source: `scripts/roadmap_acceptance.py:70`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[0].targets[0].value.slice; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:71`; AST `7a5729b87e592af6e25445c231a2a98adb0a4058140e7bd251b79e7cd3525fef`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addUnexpectedSuccess.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:71`; AST `f757d319c0acffd634adedcf93ddd826de7f9b326b1fe61eada5de5a1bf2478f`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super, test. Outputs/bindings: (none).
Calls/effect boundaries: super, super().addUnexpectedSuccess.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::RecordedResult::addUnexpectedSuccess::root.body[14].body[8].body[1].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:71`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15]::FunctionDef

Source: `scripts/roadmap_acceptance.py:74`; AST `6199aab2272b6c52fa196e8a4f62a93a7386564e6adda1cc06f095edbee75998`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, RecordedResult, accepted, all, bool, candidate, dict, digest, expected, file_binding, flatten, getattr, len, list, module, modules, name, occurrences, p, result, row, set, sorted, sources, str, suite, sys, test, unittest. Outputs/bindings: accepted, expected, module, modules, name, occurrences, p, result, row, sources, suite, test.
Calls/effect boundaries: (ROOT / 'infra/tests').rglob, Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, all, bool, digest, file_binding, flatten, getattr, len, list, name.startswith, p.relative_to, p.relative_to(ROOT).as_posix, result.occurrences.values, result.wasSuccessful, row.get, set, sorted, str, sys.modules.copy, sys.modules.copy().items, test.id, unittest.TextTestRunner, unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run, unittest.defaultTestLoader.discover.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:75`; AST `9b8a0f1235857ab32ded334c625d1412bed0d4a4a1728951355bba68aa95bf32`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, unittest. Outputs/bindings: suite.
Calls/effect boundaries: str, unittest.defaultTestLoader.discover.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:75`; AST `02f81ee4c6cbc0c30daaff48a26d6b838bed9a10ff847e8e260080b0f43833e7`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, unittest. Outputs/bindings: (none).
Calls/effect boundaries: str, unittest.defaultTestLoader.discover.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[0].value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:75`; AST `2ba7aee10892b0ada63b61c612f1f6f353356d238b09aa18ea973bbe7291d270`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[1]::Assign

Source: `scripts/roadmap_acceptance.py:76`; AST `6db9c70097ca34c23d3972f5b657ae8da6f03c649f1e9a12b2a94c17de25c8ee`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: flatten, suite, test. Outputs/bindings: expected, test.
Calls/effect boundaries: flatten, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[1].value::ListComp

Source: `scripts/roadmap_acceptance.py:76`; AST `87a2c63cd6b928c08335d91f75c5403671a32e01ce153b859c734f6fbbeaaed2`.

Rust module: `scripts::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: flatten, suite, test. Outputs/bindings: test.
Calls/effect boundaries: flatten, test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[1].value.elt::Call

Source: `scripts/roadmap_acceptance.py:76`; AST `0af97fdf80417b26c716c4596f2e18a6390bbf7a111726bba807bd9cb7708aec`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: test. Outputs/bindings: (none).
Calls/effect boundaries: test.id.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[1].value.generators[0].iter::Call

Source: `scripts/roadmap_acceptance.py:76`; AST `e97de10ada3150d10cbc1ba5284eaaeac40e150c2ca7dd9e6087c17fc0948ec3`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: flatten, suite. Outputs/bindings: (none).
Calls/effect boundaries: flatten.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2]::Assign

Source: `scripts/roadmap_acceptance.py:77`; AST `e062c82e4cae1659ea073aadb88130b32089dfc08496a32957672add5b283493`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, file_binding, p, sorted. Outputs/bindings: p, sources.
Calls/effect boundaries: (ROOT / 'infra/tests').rglob, file_binding, p.relative_to, p.relative_to(ROOT).as_posix, sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value::ListComp

Source: `scripts/roadmap_acceptance.py:77`; AST `62410304621c82792c85de29c1fa337e300c060aa749d2cb04b3b9eb8d7af2a4`.

Rust module: `scripts::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: ROOT, file_binding, p, sorted. Outputs/bindings: p.
Calls/effect boundaries: (ROOT / 'infra/tests').rglob, file_binding, p.relative_to, p.relative_to(ROOT).as_posix, sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value.elt::Call

Source: `scripts/roadmap_acceptance.py:77`; AST `08b14937fc27463c9a251769b9c5046721d987804a080a24c8eaf98656ba4b66`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, file_binding, p. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(ROOT).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value.elt.args[1]::Call

Source: `scripts/roadmap_acceptance.py:77`; AST `28336935f2ffb9beb4034e9f4a74d9d09689d9b6100580d9a47f1186879d0836`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(ROOT).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value.elt.args[1].func.value::Call

Source: `scripts/roadmap_acceptance.py:77`; AST `52c4689aa90c8885d5d4f4c522ca96e9a1a0fcec283f94d1d48c30c21346cfa2`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, p. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value.generators[0].iter::Call

Source: `scripts/roadmap_acceptance.py:77`; AST `231e0119f9750f48782ee307af92060731e5b86d2da447ed8de3bb6653d628fc`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'infra/tests').rglob, sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[2].value.generators[0].iter.args[0]::Call

Source: `scripts/roadmap_acceptance.py:77`; AST `8e718849d56ab653411b55011f220e66cbcb45836deb1990393dc1127b141276`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'infra/tests').rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.generators[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[3]::Assign

Source: `scripts/roadmap_acceptance.py:78`; AST `ec4f84861f0fc94ea7a95ac85eaf445c1fdaf101ab0cb6eeb51824bb4f7d91f1`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RecordedResult, suite, unittest. Outputs/bindings: result.
Calls/effect boundaries: unittest.TextTestRunner, unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[3].value::Call

Source: `scripts/roadmap_acceptance.py:78`; AST `84598235db209dcd79e36c0a8c7cdb9135ce86f3677624438ee15c235d703fac`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RecordedResult, suite, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.TextTestRunner, unittest.TextTestRunner(verbosity=2, resultclass=RecordedResult).run.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[3].value.func.value::Call

Source: `scripts/roadmap_acceptance.py:78`; AST `65e3c5f4caef3b3d1d5b57a564e5e89ee90fe80f91f08f11ab2862711fc84e26`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RecordedResult, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.TextTestRunner.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[4]::Assign

Source: `scripts/roadmap_acceptance.py:79`; AST `6f721cf383ea4f9898c1c766a574fb6c26c71ae8442a2e4d6837bbd14bf5bbc6`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: list, result. Outputs/bindings: occurrences.
Calls/effect boundaries: list, result.occurrences.values.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[4].value::Call

Source: `scripts/roadmap_acceptance.py:79`; AST `087e3ac0c176f33a768067decf0c96bf43ff0371566f42595e93dd224478fbaa`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: list, result. Outputs/bindings: (none).
Calls/effect boundaries: list, result.occurrences.values.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[4].value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:79`; AST `a041f1c04f70d3b5114ce42e128a54f5e4bd4d1bd55a54a90ed12de6cb7e0c3d`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.occurrences.values.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5]::Assign

Source: `scripts/roadmap_acceptance.py:80`; AST `b4f8fcafdb7927a471cfb32f334fe6c8f73827df1d7aa22e43b564f665f74cd3`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, ROOT, file_binding, getattr, module, name, sorted, str, sys. Outputs/bindings: module, modules, name.
Calls/effect boundaries: Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, file_binding, getattr, name.startswith, sorted, str, sys.modules.copy, sys.modules.copy().items.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value::ListComp

Source: `scripts/roadmap_acceptance.py:80`; AST `0822cf176a67fc01c865649c9dcc7115ff89c0aca16112a7335c0202eb3962e1`.

Rust module: `scripts::roadmap_acceptance`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: Path, ROOT, file_binding, getattr, module, name, sorted, str, sys. Outputs/bindings: module, name.
Calls/effect boundaries: Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, file_binding, getattr, name.startswith, sorted, str, sys.modules.copy, sys.modules.copy().items.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered ListComp evaluation at root.body[15].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.elt::Call

Source: `scripts/roadmap_acceptance.py:80`; AST `92fa146ebd32a771589a174daf15c868a3d7c18f0fd34836aae2390d08933b2f`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, ROOT, file_binding, module, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, file_binding, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.elt.args[1]::Call

Source: `scripts/roadmap_acceptance.py:80`; AST `cba8d1d751fc93f9064bc6eb4091ceb46f842ad4c1ad64b3c6296f36e5cf4641`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, ROOT, module, str. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.elt.args[1].args[0]::Call

Source: `scripts/roadmap_acceptance.py:80`; AST `7e3b1958cdac75d79a02662f30bb27c701e476658c3b1f6f623278f77b3fe4a9`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, ROOT, module. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.__file__).resolve, Path(module.__file__).resolve().relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.elt.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.elt.args[1].args[0].func.value::Call

Source: `scripts/roadmap_acceptance.py:80`; AST `a88217a2898dc1356d1202c351439dd00ae2e5d3e7f5cff464fb3eff5264047d`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(module.__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.elt.args[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.elt.args[1].args[0].func.value.func.value::Call

Source: `scripts/roadmap_acceptance.py:80`; AST `165492e7bd40b6ed9d42272ab9954e3d4c737a72215049a4ec74746b4290a7fa`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, module. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.elt.args[1].args[0].func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.generators[0].iter::Call

Source: `scripts/roadmap_acceptance.py:81`; AST `11405134f9bed46e5677f8398785f57280acc3ddf4bcff424f80875be779544a`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sorted, sys. Outputs/bindings: (none).
Calls/effect boundaries: sorted, sys.modules.copy, sys.modules.copy().items.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.generators[0].iter.args[0]::Call

Source: `scripts/roadmap_acceptance.py:81`; AST `329827cae8545b0b2e84b08d70fae53202579d546d2a980c6c80fd971f224091`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sys. Outputs/bindings: (none).
Calls/effect boundaries: sys.modules.copy, sys.modules.copy().items.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.generators[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.generators[0].iter.args[0].func.value::Call

Source: `scripts/roadmap_acceptance.py:81`; AST `92b80affc22a1acc0760d9f6d8c0260b951d684d44f7528abfb4d54dde47b315`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sys. Outputs/bindings: (none).
Calls/effect boundaries: sys.modules.copy.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.generators[0].iter.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.generators[0].ifs[0].values[0].values[1]::Call

Source: `scripts/roadmap_acceptance.py:82`; AST `bb3d7b4f32f84639595ebad9f2e7b7dc42384496202da72b3b6642b2c43b60fb`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name. Outputs/bindings: (none).
Calls/effect boundaries: name.startswith.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.generators[0].ifs[0].values[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[5].value.generators[0].ifs[0].values[1]::Call

Source: `scripts/roadmap_acceptance.py:82`; AST `bbc45607650a7db93420a2df19b40ce949db06df3d988f7b2dcdfcabe2ba2723`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, module. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[5].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6]::Assign

Source: `scripts/roadmap_acceptance.py:83`; AST `7b7a314913de2fae17955c73621d8addd2eb70410674480fc3d3d21b95f516cf`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, bool, expected, len, occurrences, result, row, set. Outputs/bindings: accepted, row.
Calls/effect boundaries: all, bool, len, result.wasSuccessful, row.get, set.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[0]::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `8d1d2ee4fa1bf4be7289761f56da64f1412743b10882123358b5a30f31d3762e`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bool, expected. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[1].left::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `c2d06b163e3f45e9d7be910cb5ac5a89b21e57724763b4159be61fb15e2f5005`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[1].comparators[0]::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `92c7b105ab8208e6c0d99003aa501423395c1925384705c62d883a1c21cf675e`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, len, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[1].comparators[0].args[0]::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[1].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[2].left::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `8065006d3e7f0aec9df46549354158a7684ad8f3e04977773498c5d7231e93b7`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: expected, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[2].comparators[0]::Call

Source: `scripts/roadmap_acceptance.py:83`; AST `1ba96593030ef0efa580d3c893e804f95cdc4ec3b742eb82f7f525da9607abe4`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[2].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[3]::Call

Source: `scripts/roadmap_acceptance.py:84`; AST `16fd9381ba179434922b22a0cf1a6e506610e6b5820f6e1ce88bb639f6018a95`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: result.wasSuccessful.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[4]::Call

Source: `scripts/roadmap_acceptance.py:84`; AST `cc53569ad748decf7cc201d47b93a85a48b4b6334e2546ac15b86a74dcad8781`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, occurrences, row. Outputs/bindings: row.
Calls/effect boundaries: all, row.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[4].args[0]::GeneratorExp

Source: `scripts/roadmap_acceptance.py:84`; AST `b92caba25df6bb00f63668a17d8d8aa32115f69a347ad2e62c3199e4b5cc4538`.

Rust module: `scripts::roadmap_acceptance`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: occurrences, row. Outputs/bindings: row.
Calls/effect boundaries: row.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[6].value.values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[6].value.values[4].args[0].elt.values[1].values[1]::Call

Source: `scripts/roadmap_acceptance.py:85`; AST `b88bd35d28b53c75eccfc5513e04f7c123f933dbbd241454d65c612386a21b7b`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[6].value.values[4].args[0].elt.values[1].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[7]::Return

Source: `scripts/roadmap_acceptance.py:86`; AST `d0c4431070a989d7be784498aa613e7118bbfd32b10ac2905c7a2bf34ea890bd`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: accepted, candidate, digest, expected, modules, occurrences, sources, sys. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Return evaluation at root.body[15].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::tests::root.body[15].body[7].value.values[8]::Call

Source: `scripts/roadmap_acceptance.py:88`; AST `117d48706f1e227a74861f0e9557a4b9c36ecdcdb6f79e2f6a952f7a3cb29fc0`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, modules. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[15].body[7].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16]::FunctionDef

Source: `scripts/roadmap_acceptance.py:92`; AST `aad604cdf232d897f3a2c94d2564f2517e52fe184b4d43faaa9504d4a05a3c7c`.

Rust module: `scripts::roadmap_acceptance`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ROOT, __doc__, argparse, args, atomic_write_json, authority_inventory, confined_path, parser, print, reconcile_inventory, reconciliation, record, save_inventory, saved, snapshot, tests. Outputs/bindings: args, parser, reconciliation, record, saved, snapshot.
Calls/effect boundaries: argparse.ArgumentParser, atomic_write_json, authority_inventory, confined_path, parser.add_argument, parser.parse_args, print, reconcile_inventory, save_inventory, tests.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:93`; AST `c4ad6d457d8034b25dcc473a40ed9c6629dab3a54fd3b776e18da1d1367bd02c`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: parser.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:93`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[1]::Expr

Source: `scripts/roadmap_acceptance.py:94`; AST `c39b1977ce3e28a3aa46ddb190bd44fa0966edf0f3d83620f3f9cee507d67573`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[1].value::Call

Source: `scripts/roadmap_acceptance.py:94`; AST `f45ed6d2872e967980c0c2557696c86b402b6abb19a651791df8aac83dafa0cf`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[2]::Expr

Source: `scripts/roadmap_acceptance.py:95`; AST `9da33d77a9d730d1b0a37192c8581046a68572dcd897195379ae8e318be418ad`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[2].value::Call

Source: `scripts/roadmap_acceptance.py:95`; AST `fec4fbf48af0ce6f50e4b9bb90b76836907b3da18e1361a79d252cbbf372ac6f`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[3]::Expr

Source: `scripts/roadmap_acceptance.py:96`; AST `4dc5801b9512d0ab4f7d67781330b07dcfe712734bf0b719389f03a9217552b6`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[3].value::Call

Source: `scripts/roadmap_acceptance.py:96`; AST `1ec65a7b2bb9c75b74e5e087b7144be3df10847cfcd4b35415c851ac404d3884`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[4]::Assign

Source: `scripts/roadmap_acceptance.py:97`; AST `6275c8d1600da776fb862cf3f5fef974e2559c70800565172097404dcea6fef6`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: args.
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[4].value::Call

Source: `scripts/roadmap_acceptance.py:97`; AST `c865e8043798bf46a3b13d6774886772cbfabc2836b109a02aef4d3c2ad2a7ef`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5]::If

Source: `scripts/roadmap_acceptance.py:98`; AST `13e04ea50e4882cc8437c10d510bb3d443e1254ba6fdda1d0b40ca79e7a4dcbf`.

Rust module: `scripts::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, authority_inventory, reconcile_inventory, reconciliation, save_inventory, saved, snapshot, tests. Outputs/bindings: reconciliation, record, saved, snapshot.
Calls/effect boundaries: authority_inventory, reconcile_inventory, save_inventory, tests.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered If evaluation at root.body[16].body[5]; no call, error or mutation may be omitted. Condition: args.action == 'tests'
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].body[0]::Assign

Source: `scripts/roadmap_acceptance.py:99`; AST `a2805cf7851b03fbb1f47ad3981d1803708e21585411b021ecd4fdd0e2e2e3d0`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, tests. Outputs/bindings: record.
Calls/effect boundaries: tests.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].body[0].value::Call

Source: `scripts/roadmap_acceptance.py:99`; AST `10d7f5f19ffef7959a4c11dae22582179116f32264c14206258af5ef1f112a80`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, tests. Outputs/bindings: (none).
Calls/effect boundaries: tests.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[0]::Assign

Source: `scripts/roadmap_acceptance.py:101`; AST `ed59ea8b308948e04feffd4eced9314e9ec3b9403bf395c6608a146ce08a62d4`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, authority_inventory. Outputs/bindings: snapshot.
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[0].value::Call

Source: `scripts/roadmap_acceptance.py:101`; AST `09e31a6fd5e6ba6906966e5f2db33b8e9165f19a5dc43caf2ffcf411a54de0c7`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, authority_inventory. Outputs/bindings: (none).
Calls/effect boundaries: authority_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[1]::Assign

Source: `scripts/roadmap_acceptance.py:102`; AST `1699e3f558320a3e222257425a9d40f6c175f00c5d3233670384cfe6e95be22d`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, reconcile_inventory, snapshot. Outputs/bindings: reconciliation.
Calls/effect boundaries: reconcile_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[1].value::Call

Source: `scripts/roadmap_acceptance.py:102`; AST `d1ba92367fc57ebd8e1b8484c6989a1515430ae592b3521486d772ff420bc04c`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, reconcile_inventory, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: reconcile_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[2]::Assign

Source: `scripts/roadmap_acceptance.py:103`; AST `905b2905b166a8c792f41d3ff132e66a9b67095d751b4704718b7d9185b661d2`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, save_inventory, snapshot. Outputs/bindings: saved.
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].orelse[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[2].value::Call

Source: `scripts/roadmap_acceptance.py:103`; AST `53fd71f091aaaae0b1ef5d6e6e9f1a0282eecf120b097af39a9c0c4e78a0a54a`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, save_inventory, snapshot. Outputs/bindings: (none).
Calls/effect boundaries: save_inventory.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[5].orelse[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[5].orelse[3]::Assign

Source: `scripts/roadmap_acceptance.py:104`; AST `3b21fd1aec37c08fbf466a5f1b6eebec1bb72995c46fb8a736916e4f85301231`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, reconciliation, saved, snapshot. Outputs/bindings: record.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[5].orelse[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[6]::Expr

Source: `scripts/roadmap_acceptance.py:107`; AST `2788f7d1a826115b2255675302e6c2cd93f4df2a5223f3eaecb94d4c11b4b788`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, atomic_write_json, confined_path, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[6].value::Call

Source: `scripts/roadmap_acceptance.py:107`; AST `1209d46f3f10722f678ef162b5edbdfa00556b405784c29b195e774046189b74`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, atomic_write_json, confined_path, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[6].value.args[0]::Call

Source: `scripts/roadmap_acceptance.py:107`; AST `bd2c4103df935f33b6c3362a61ace084743aa0c8c3bc6058f572e1ed907f0aa0`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[7]::Expr

Source: `scripts/roadmap_acceptance.py:108`; AST `b0f7dd5e5f5a5edd93cf6a083bcc2136e5aa195ecb743cf5b8505b0d1225caf8`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, print, record. Outputs/bindings: (none).
Calls/effect boundaries: print.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[7].value::Call

Source: `scripts/roadmap_acceptance.py:108`; AST `72ce84139cb09ba9c273d0099df618e38541753c5d16580adde52257c4bcfccf`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, print, record. Outputs/bindings: (none).
Calls/effect boundaries: print.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[16].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::main::root.body[16].body[8]::Return

Source: `scripts/roadmap_acceptance.py:109`; AST `e3c23a4cb174760afeabee197da6ef199226fffa523cc853725c745cbc5aa884`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: record. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Return evaluation at root.body[16].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[17]::If

Source: `scripts/roadmap_acceptance.py:112`; AST `f0ea0be627ebd2887d7f161de9c610e749cbd38d176e8efffefbc0424d175c46`.

Rust module: `scripts::roadmap_acceptance`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: SystemExit, __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered If evaluation at root.body[17]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[17].body[0]::Raise

Source: `scripts/roadmap_acceptance.py:113`; AST `0634336e225749743986a4f7a082980f4f2712d05fe8333bc0c5cc9f00697679`.

Rust module: `scripts::roadmap_acceptance`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SystemExit, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Raise evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[17].body[0].exc::Call

Source: `scripts/roadmap_acceptance.py:113`; AST `ff6163839ec73a868582955a0c13ef79bd60ed979b4984a53f1d521fdca2e714`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SystemExit, main. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit, main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_acceptance.py::module::root.body[17].body[0].exc.args[0]::Call

Source: `scripts/roadmap_acceptance.py:113`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `scripts::roadmap_acceptance`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.roadmap_inventory, agentinfra.roadmap_records, agentinfra.security, argparse, pathlib, sys, unittest.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].exc.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
