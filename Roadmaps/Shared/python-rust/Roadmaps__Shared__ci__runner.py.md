# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 61. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## Roadmaps/Shared/ci/runner.py::module::root::Module

Source: `Roadmaps/Shared/ci/runner.py:1`; AST `b5735dc5223e6f3546a9c566b1674811b4d34432936a87881077c9afa05c5611`.

Rust module: `Roadmaps::Shared::ci::runner`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: CHECKS, ENGINE, Path, ROOT, RuntimeError, __file__, __name__, argv, asyncio, client, container, dagger, image, json, observed, os, path, re, results, run, source, str, subprocess, sys, version. Outputs/bindings: CHECKS, ENGINE, ROOT, argv, client, container, image, observed, path, results, source.
Calls/effect boundaries: Path, Path(__file__).resolve, RuntimeError, asyncio.run, client.container, client.container().from_, client.container().from_(image).with_directory, client.container().from_(image).with_directory('/src', source).with_workdir, client.host, client.host().directory, container.stdout, container.with_exec, dagger.Config, dagger.Connection, json.dumps, os.environ.get, path.parent.mkdir, path.write_text, re.escape, re.fullmatch, re.search, results.append, run, str, subprocess.run, version.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[0]::Expr

Source: `Roadmaps/Shared/ci/runner.py:1`; AST `667dd4767ca4dcc891cae7ea842b5354c3acf23030a30e05ba0559005ca6f47c`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[1]::ImportFrom

Source: `Roadmaps/Shared/ci/runner.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[2]::Import

Source: `Roadmaps/Shared/ci/runner.py:4`; AST `8058853a01547215468ceb8652964d4821f79273f307bd4d8f44df328511a258`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[3]::Import

Source: `Roadmaps/Shared/ci/runner.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[4]::Import

Source: `Roadmaps/Shared/ci/runner.py:6`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[5]::ImportFrom

Source: `Roadmaps/Shared/ci/runner.py:7`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[6]::Import

Source: `Roadmaps/Shared/ci/runner.py:8`; AST `6b81b4ca19c88ec507aad63f1f49291209368a9490113655a68e994c91d092c1`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[7]::Import

Source: `Roadmaps/Shared/ci/runner.py:9`; AST `9d97d469cf8d66465563e1e22c6dab3b6107819aba2d9956c7080016c1ab9c1b`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[8]::Import

Source: `Roadmaps/Shared/ci/runner.py:10`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[9]::ImportFrom

Source: `Roadmaps/Shared/ci/runner.py:11`; AST `126b75bb9f02e0476dbdf879ac4597bc43a8a0c60fb85e96ea158d727e561cda`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[10]::Assign

Source: `Roadmaps/Shared/ci/runner.py:13`; AST `eb67ab1ecb71debfc5e1b6db1ba7074660420e61718b8583a041607f10d7b92c`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: ENGINE.
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[11]::Assign

Source: `Roadmaps/Shared/ci/runner.py:14`; AST `1fdb9655d355f076050e4abaeb3d9d66183e0e169f9145ec35b79f9f443de948`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[11].value.value.value::Call

Source: `Roadmaps/Shared/ci/runner.py:14`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[11].value.value.value.func.value::Call

Source: `Roadmaps/Shared/ci/runner.py:14`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[12]::Assign

Source: `Roadmaps/Shared/ci/runner.py:15`; AST `d41c750dfbcee4976e6d2323b842b43bfd6a561a7de61f29ff503850445befb0`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: CHECKS.
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13]::AsyncFunctionDef

Source: `Roadmaps/Shared/ci/runner.py:23`; AST `a55c0fd88ade023900df43eccd82b9597caf5827586c67c96c562170492e37a8`.

Rust module: `Roadmaps::Shared::ci::runner`. async fn with explicit cancellation/lifetime contract; preserve suspension and observable completion

Inputs: CHECKS, ENGINE, ROOT, RuntimeError, argv, client, container, dagger, image, json, observed, os, path, re, results, source, str, subprocess, sys, version. Outputs/bindings: argv, client, container, image, observed, path, results, source.
Calls/effect boundaries: RuntimeError, client.container, client.container().from_, client.container().from_(image).with_directory, client.container().from_(image).with_directory('/src', source).with_workdir, client.host, client.host().directory, container.stdout, container.with_exec, dagger.Config, dagger.Connection, json.dumps, os.environ.get, path.parent.mkdir, path.write_text, re.escape, re.fullmatch, re.search, results.append, str, subprocess.run, version.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered AsyncFunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[0]::Import

Source: `Roadmaps/Shared/ci/runner.py:24`; AST `b4acfdaf25a34df90a7fe52d277958f4d5fc835d6536e3ec05793e755cd524e3`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Import evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[1]::Assign

Source: `Roadmaps/Shared/ci/runner.py:25`; AST `a1830af564785726fc3999aea45331ead8b128a1206fe5fa12d56546056db376`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: subprocess. Outputs/bindings: observed.
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[1].value.value::Call

Source: `Roadmaps/Shared/ci/runner.py:25`; AST `a2a0a3c7158d2b53c88e354a1f10b3441cade714cb0e04dfc3047f81a798c492`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: subprocess. Outputs/bindings: (none).
Calls/effect boundaries: subprocess.run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2]::If

Source: `Roadmaps/Shared/ci/runner.py:26`; AST `1a218070cb0c254adf289275b2a581ac827e8299a7c48f2d38735b7f89f14bb8`.

Rust module: `Roadmaps::Shared::ci::runner`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ENGINE, RuntimeError, observed, re, version. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, re.escape, re.search, version.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[2]; no call, error or mutation may be omitted. Condition: not re.search('\\bv' + re.escape(ENGINE) + '\\b', observed) or version('dagger-io') != ENGINE
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2].test.values[0].operand::Call

Source: `Roadmaps/Shared/ci/runner.py:26`; AST `1b931b67beadd86532082cfdcc7899806e534fdb39b408b7a06d908e8cf8e6dd`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENGINE, observed, re. Outputs/bindings: (none).
Calls/effect boundaries: re.escape, re.search.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].test.values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2].test.values[0].operand.args[0].left.right::Call

Source: `Roadmaps/Shared/ci/runner.py:26`; AST `8336b66ab298c9a518cd15a578b4238462fdd223991900a45f0ea0e3e70424a8`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENGINE, re. Outputs/bindings: (none).
Calls/effect boundaries: re.escape.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].test.values[0].operand.args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2].test.values[1].left::Call

Source: `Roadmaps/Shared/ci/runner.py:26`; AST `eea21c50c90b18adb90735298d46f6cc970ed6b7ccf8402836eaed4a247e55fb`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: version. Outputs/bindings: (none).
Calls/effect boundaries: version.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2].body[0]::Raise

Source: `Roadmaps/Shared/ci/runner.py:27`; AST `ef90eb1ef418cbe40153ebe773e308207e9a48f67d6c939f6651125a2c1e497e`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[2].body[0].exc::Call

Source: `Roadmaps/Shared/ci/runner.py:27`; AST `2d89d0f401f3e01807d6e124dd89d77a893aaf95b7a5997607c9d6b83adcb487`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[2].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[3]::Assign

Source: `Roadmaps/Shared/ci/runner.py:28`; AST `2fd42f1e9175929ee9eee7f597a6e10adfb9f30c89e2682e4c7a209c63725adb`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: image.
Calls/effect boundaries: os.environ.get.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[3].value::Call

Source: `Roadmaps/Shared/ci/runner.py:28`; AST `00648507f61b96c461f3514d1006921cf09e5598aed19757edca2a21017111b5`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.environ.get.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[4]::If

Source: `Roadmaps/Shared/ci/runner.py:29`; AST `8038d14d9ed337467749a4a94646208fdd43fdf6f36ddb7c1341b0a1a28a5bcd`.

Rust module: `Roadmaps::Shared::ci::runner`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: RuntimeError, image, re. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError, re.fullmatch.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered If evaluation at root.body[13].body[4]; no call, error or mutation may be omitted. Condition: not re.fullmatch('[^\\s]+@sha256:[a-f0-9]{64}', image)
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[4].test.operand::Call

Source: `Roadmaps/Shared/ci/runner.py:29`; AST `68564eb7eabc12063e216312b7d9000905ef76357fb9f8e14c094489694a2c34`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: image, re. Outputs/bindings: (none).
Calls/effect boundaries: re.fullmatch.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[4].body[0]::Raise

Source: `Roadmaps/Shared/ci/runner.py:30`; AST `98ca676bcf815af3d72b43c4d7e359b48b3b7e943f7d4db0a2f6ce8660d11303`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Raise evaluation at root.body[13].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[4].body[0].exc::Call

Source: `Roadmaps/Shared/ci/runner.py:30`; AST `fdc92115e7ea0e8cc6b53d6eea0d3002a0b3f2ef49792bb770c041165bb9bbfc`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: RuntimeError. Outputs/bindings: (none).
Calls/effect boundaries: RuntimeError.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[4].body[0].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5]::AsyncWith

Source: `Roadmaps/Shared/ci/runner.py:31`; AST `d6264fb5e1062d347c37135a9fe2c7717615c066aa56717fefc78281d70855a7`.

Rust module: `Roadmaps::Shared::ci::runner`. async enter/exit protocol with explicit awaited cleanup and cancellation outcomes

Inputs: CHECKS, ENGINE, ROOT, argv, client, container, dagger, image, json, path, results, source, str, sys. Outputs/bindings: argv, client, container, path, results, source.
Calls/effect boundaries: client.container, client.container().from_, client.container().from_(image).with_directory, client.container().from_(image).with_directory('/src', source).with_workdir, client.host, client.host().directory, container.stdout, container.with_exec, dagger.Config, dagger.Connection, json.dumps, path.parent.mkdir, path.write_text, results.append, str.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered AsyncWith evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].items[0].context_expr::Call

Source: `Roadmaps/Shared/ci/runner.py:31`; AST `f9108f26ff12fb6581c2ae65e967c8ac7197c46f6d951564f88f53aca9db102d`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dagger, sys. Outputs/bindings: (none).
Calls/effect boundaries: dagger.Config, dagger.Connection.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].items[0].context_expr.args[0]::Call

Source: `Roadmaps/Shared/ci/runner.py:31`; AST `e6a0e168126b07860ab02ed184b65f0ec5434f88f7de1f2666fafbea66a6f99b`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dagger, sys. Outputs/bindings: (none).
Calls/effect boundaries: dagger.Config.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].items[0].context_expr.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[0]::Assign

Source: `Roadmaps/Shared/ci/runner.py:32`; AST `78a08ab3f4b7f463532e9973f237b217069a2a1b616a75a1827f7ba2d96288e6`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, client, str. Outputs/bindings: source.
Calls/effect boundaries: client.host, client.host().directory, str.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[0].value::Call

Source: `Roadmaps/Shared/ci/runner.py:32`; AST `a0da41c5e0c50365493f7b3d56c7517fd095770d717d313aa1eae3f5f7c459d3`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, client, str. Outputs/bindings: (none).
Calls/effect boundaries: client.host, client.host().directory, str.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[0].value.func.value::Call

Source: `Roadmaps/Shared/ci/runner.py:32`; AST `3ae79d3b9c1a8dbda426e5db5fe7417982b592b6d37797ede3ac6bd55bfed4ca`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client. Outputs/bindings: (none).
Calls/effect boundaries: client.host.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[0].value.args[0]::Call

Source: `Roadmaps/Shared/ci/runner.py:32`; AST `b14c2aff9d1e6e74488f78058c8a47f8f4a5ac37c88d46af67adb15b7fda7971`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[1]::Assign

Source: `Roadmaps/Shared/ci/runner.py:33`; AST `8d6c2b275b577f28b2b5cfa07aea7fa2c09a14fe65c23dd22a559381767f7d49`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, image, source. Outputs/bindings: container.
Calls/effect boundaries: client.container, client.container().from_, client.container().from_(image).with_directory, client.container().from_(image).with_directory('/src', source).with_workdir.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[1].value::Call

Source: `Roadmaps/Shared/ci/runner.py:33`; AST `b5a9696fac5466af47d9aaf5bf129bf9631986084acb3c81d543425da47f1ca0`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, image, source. Outputs/bindings: (none).
Calls/effect boundaries: client.container, client.container().from_, client.container().from_(image).with_directory, client.container().from_(image).with_directory('/src', source).with_workdir.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[1].value.func.value::Call

Source: `Roadmaps/Shared/ci/runner.py:33`; AST `9ffe16d90ca39990f1c803bdea9dced4878168d53ede78465b9932034bce6350`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, image, source. Outputs/bindings: (none).
Calls/effect boundaries: client.container, client.container().from_, client.container().from_(image).with_directory.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[1].value.func.value.func.value::Call

Source: `Roadmaps/Shared/ci/runner.py:33`; AST `72e79d82fb726e2f855bc27993ba61364e6060c024f08fcc7f6faaa91c59e834`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, image. Outputs/bindings: (none).
Calls/effect boundaries: client.container, client.container().from_.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[1].value.func.value.func.value.func.value::Call

Source: `Roadmaps/Shared/ci/runner.py:33`; AST `88aaf0b0b496d6a80a5ca34e8e6f3f5277183ed7e6ee3f929f9404a84f939429`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client. Outputs/bindings: (none).
Calls/effect boundaries: client.container.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[1].value.func.value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[2]::Assign

Source: `Roadmaps/Shared/ci/runner.py:34`; AST `22db4c1a505af52193564f42b387b3d0022747f08b16e68836ec99078f026c4d`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: results.
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3]::For

Source: `Roadmaps/Shared/ci/runner.py:35`; AST `d44f49c47f6ba76c815bbe395c7f5b2f2d837d1e7b012362a4bf55eea96bcfa6`.

Rust module: `Roadmaps::Shared::ci::runner`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: CHECKS, argv, container, results. Outputs/bindings: argv, container.
Calls/effect boundaries: container.stdout, container.with_exec, results.append.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered For evaluation at root.body[13].body[5].body[3]; no call, error or mutation may be omitted. Iteration: argv in CHECKS
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3].body[0]::Assign

Source: `Roadmaps/Shared/ci/runner.py:36`; AST `8a4fb244ed81a629fc1af61175e917a7305c09f3ee8ce9a5a83fe2258ac1f268`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, container. Outputs/bindings: container.
Calls/effect boundaries: container.with_exec.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3].body[0].value::Call

Source: `Roadmaps/Shared/ci/runner.py:36`; AST `c1b73eddba27d549a7c982a2ccc2e6f9dde1c447e60f9684183066a035114972`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, container. Outputs/bindings: (none).
Calls/effect boundaries: container.with_exec.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3].body[1]::Expr

Source: `Roadmaps/Shared/ci/runner.py:37`; AST `cc6e0d0149d943a0a0c4ac1547f186f5fdd542a9aa2636fcf04b7ddd45613460`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, container, results. Outputs/bindings: (none).
Calls/effect boundaries: container.stdout, results.append.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3].body[1].value::Call

Source: `Roadmaps/Shared/ci/runner.py:37`; AST `267a7568b45adf06ed9d42518f7fd700aa51ca4989aab02238a488b68f96c2e2`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, container, results. Outputs/bindings: (none).
Calls/effect boundaries: container.stdout, results.append.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[3].body[1].value.args[0].values[1].value::Call

Source: `Roadmaps/Shared/ci/runner.py:37`; AST `d0089aed42a67b72912e7f06d9e896e18ddbb37af099b1089890e032397b3b5f`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: container. Outputs/bindings: (none).
Calls/effect boundaries: container.stdout.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[3].body[1].value.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[4]::Assign

Source: `Roadmaps/Shared/ci/runner.py:38`; AST `51da09a4d9cbe5872d3a53dccd853538822aba34deb25a698fbde86107b99e05`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[5]::Expr

Source: `Roadmaps/Shared/ci/runner.py:39`; AST `ee4624f1df91400daa13a3f4fa8ccf0654522660a49483e139d870f1d98cac38`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[5].value::Call

Source: `Roadmaps/Shared/ci/runner.py:39`; AST `f32fa3bf8bd728879b5ee78564c0e339658253e810165c3df033c0892f416875`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.parent.mkdir.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[6]::Expr

Source: `Roadmaps/Shared/ci/runner.py:40`; AST `b7fc7b1938d8deb21a0110e5db75a46b9844976b1c3bd66d1090251ea692db11`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ENGINE, image, json, path, results. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[6].value::Call

Source: `Roadmaps/Shared/ci/runner.py:40`; AST `0500cf45b5e4153f1bcc92c73d11103620043bf64af205cda864193240b52114`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENGINE, image, json, path, results. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, path.write_text.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::run::root.body[13].body[5].body[6].value.args[0].left::Call

Source: `Roadmaps/Shared/ci/runner.py:40`; AST `398a33a96ae09ed0a66bac21caf73767b1e3c7d6df3f3169a3fa67562e4b997c`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ENGINE, image, json, results. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[6].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[14]::If

Source: `Roadmaps/Shared/ci/runner.py:44`; AST `c7050524aa1b2676332526c235d6c57d9fb517e2fce3c6f88313af9c09391d88`.

Rust module: `Roadmaps::Shared::ci::runner`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, asyncio, run. Outputs/bindings: (none).
Calls/effect boundaries: asyncio.run, run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered If evaluation at root.body[14]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[14].body[0]::Expr

Source: `Roadmaps/Shared/ci/runner.py:45`; AST `07855d0497b36dd0ce7b14e9509e29d705eacfa3b5983313cd90ea7fe4d973c5`.

Rust module: `Roadmaps::Shared::ci::runner`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asyncio, run. Outputs/bindings: (none).
Calls/effect boundaries: asyncio.run, run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[14].body[0].value::Call

Source: `Roadmaps/Shared/ci/runner.py:45`; AST `559140925f53e7cbc4e957b76933845846db2c686b065914982474d6d0a0c6b7`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asyncio, run. Outputs/bindings: (none).
Calls/effect boundaries: asyncio.run, run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## Roadmaps/Shared/ci/runner.py::module::root.body[14].body[0].value.args[0]::Call

Source: `Roadmaps/Shared/ci/runner.py:45`; AST `55b1cf18eaecd7f71af0e4f4a5272cc9dd9094805094b0ec9cbaf4e3ace621c7`.

Rust module: `Roadmaps::Shared::ci::runner`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: run. Outputs/bindings: (none).
Calls/effect boundaries: run.
Dependencies: __future__, asyncio, dagger, importlib.metadata, json, os, pathlib, re, subprocess, sys.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::process::Command with explicit process-group owner; regex
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
