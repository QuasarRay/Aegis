# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 349. Inventory digest: `aa064348a8890b7949c06405ee63d5aa9506e1c764b31538cbe8d80f5017d12e`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_python.py::module::root::Module

Source: `scripts/roadmap_python.py:1`; AST `88b90463af7890c1a7ebe00755f656e7c897236bf4eb3a682d1d45d74587b1e2`.

Rust module: `scripts::roadmap_python`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Exception, Path, ROOT, TRANSPORT, __doc__, __file__, __name__, _download, archive, argparse, args, argv, artifacts, asdict, atomic_write_json, b, binding, bindings_current, bool, bundle, checked, classify_deal, classify_nagini, compile_roadmaps, confined_path, deadline, dependencies, details, dict, digest, directory, download_with_mirrors, entry, environment, exc, file_binding, files, fixture, float, installed, java, java_root, java_version, json, len, list, lock, main, map, minimal_subprocess_env, nagini, name, observed, observed_path, os, outcomes, output, p, package, parser, path, print, profile, provision, provision_deal, provision_esbmc, python, qualify, qualify_deal, qualify_esbmc, r, read_download_policy, read_json, require, result, result_path, root, route, run_recipe_stage, runs, sorted, source, source_closure, str, sys, tarfile, time, toolchain, toolchain_path, type, venv, virtual, wheels. Outputs/bindings: ROOT, archive, args, argv, artifacts, binding, bundle, checked, deadline, dependencies, details, directory, entry, environment, files, fixture, installed, java, java_root, java_version, lock, nagini, name, observed, observed_path, outcomes, output, p, package, parser, path, profile, python, r, result, result_path, runs, source, toolchain, virtual, wheels.
Calls/effect boundaries: (virtual / 'bin/python').exists, Path, Path(__file__).resolve, _download, argparse.ArgumentParser, artifacts.append, artifacts.extend, asdict, atomic_write_json, bindings_current, bool, bundle.extractall, classify_deal, classify_nagini, compile_roadmaps, confined_path, dependencies.append, details.get, details.update, dict, digest, directory.mkdir, directory.rglob, download_with_mirrors, environment.get, file_binding, java_root.exists, java_root.glob, java_root.mkdir, json.dumps, len, list, lock.get, main, map, minimal_subprocess_env, nagini.is_file, observed_path.is_file, observed_path.relative_to, observed_path.relative_to(root).as_posix, os.uname, output.parent.mkdir, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, parser.add_argument, parser.parse_args, path.relative_to, path.relative_to(root).as_posix, print, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, read_download_policy, read_json, require, result_path.relative_to, result_path.relative_to(root).as_posix, route, run_recipe_stage, runs.append, sorted, source.relative_to, source.relative_to(root).as_posix, source_closure, str, sys.path.insert, tarfile.open, time.monotonic, toolchain.get, type, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[0]::Expr

Source: `scripts/roadmap_python.py:1`; AST `ee755cd0940776fe3a1a0c68b859a397b05712cbabad8237f936984c1fcfedbd`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[1]::ImportFrom

Source: `scripts/roadmap_python.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[2]::Import

Source: `scripts/roadmap_python.py:4`; AST `356e6775028bc09e699d8b986887aaebc5e3e8e414a507fe911e3ba7da1264d9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[3]::ImportFrom

Source: `scripts/roadmap_python.py:5`; AST `400d7764c2a2b8cabf9a4dc4cd172f3f6e19abcbe53e771b676ad31a327775fa`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[4]::Import

Source: `scripts/roadmap_python.py:6`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[5]::Import

Source: `scripts/roadmap_python.py:7`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[6]::ImportFrom

Source: `scripts/roadmap_python.py:8`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[7]::Import

Source: `scripts/roadmap_python.py:9`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[8]::Import

Source: `scripts/roadmap_python.py:10`; AST `741092dea1f6a53333762688bf68b559454505d7bd20d5f8a7c366b2137afcb4`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[9]::Import

Source: `scripts/roadmap_python.py:11`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[10]::Import

Source: `scripts/roadmap_python.py:12`; AST `ed2cb5c0bad66165f89629cf1ddc37e5077e2360bde054e7e311c6e64bed20c6`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[11]::Assign

Source: `scripts/roadmap_python.py:14`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[11].value.value.value::Call

Source: `scripts/roadmap_python.py:14`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[11].value.value.value.func.value::Call

Source: `scripts/roadmap_python.py:14`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[11].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[12]::Expr

Source: `scripts/roadmap_python.py:15`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[12].value::Call

Source: `scripts/roadmap_python.py:15`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[12].value.args[1]::Call

Source: `scripts/roadmap_python.py:15`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[12].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[13]::ImportFrom

Source: `scripts/roadmap_python.py:17`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[14]::ImportFrom

Source: `scripts/roadmap_python.py:18`; AST `53de7f6c4c3d9d3208c4dde7e7ab94a698ffba0be3741058ffc6fca32b8ec724`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[15]::ImportFrom

Source: `scripts/roadmap_python.py:19`; AST `db5c8677a4f676e011786557ebf779dfd621dafd3f5394ec9f88c9673bebca4e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[16]::ImportFrom

Source: `scripts/roadmap_python.py:20`; AST `3b1f096af51b088fc8db1bcf6f2df1bf3d578425197b6db1f15386d0b11cf950`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[17]::ImportFrom

Source: `scripts/roadmap_python.py:21`; AST `d0e0e5470a192f3d6dc1679135eb1ba58e8cb95180ed34037ed9805c7a05bb48`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[18]::ImportFrom

Source: `scripts/roadmap_python.py:22`; AST `014ea31600ee4ce517fb1ebb731da33a2656bc0082578a99cd659f6888d056ec`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[19]::ImportFrom

Source: `scripts/roadmap_python.py:23`; AST `e0ffff08081556b53bbf2f6e7c9f8aea08955e05b121baaa0cd5b75e05c5cd1b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::_download::root.body[20]::FunctionDef

Source: `scripts/roadmap_python.py:26`; AST `d28a704cb38b4d4f5cc85082fb41c2de5858a823d5ba53d9642143292e7b278d`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, deadline, dict, directory, download_with_mirrors, entry, float, root. Outputs/bindings: (none).
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::_download::root.body[20].body[0]::Return

Source: `scripts/roadmap_python.py:27`; AST `e022cd6430e9175171f6b2047d651410cb90ab168db8b94b2815516513c6bffd`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, directory, download_with_mirrors, entry, root. Outputs/bindings: (none).
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Return evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::_download::root.body[20].body[0].value::Call

Source: `scripts/roadmap_python.py:27`; AST `ecdf811dc0e8f10dbca615185baefd4e156fca20a4ed943477638f8e67d2cbb3`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, directory, download_with_mirrors, entry, root. Outputs/bindings: (none).
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21]::FunctionDef

Source: `scripts/roadmap_python.py:30`; AST `aa40cd197a32f46610169c9ff9025efa4a5b59be948fc99ae53aa2864a8e0747`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, TRANSPORT, _download, archive, asdict, atomic_write_json, b, bundle, checked, confined_path, deadline, dict, digest, directory, environment, file_binding, files, installed, java, java_root, java_version, len, list, lock, map, minimal_subprocess_env, nagini, os, output, p, package, python, read_download_policy, read_json, require, root, run_recipe_stage, sorted, str, sys, tarfile, time, venv, virtual, wheels. Outputs/bindings: archive, bundle, checked, deadline, directory, environment, files, installed, java, java_root, java_version, lock, nagini, p, package, python, virtual, wheels.
Calls/effect boundaries: (virtual / 'bin/python').exists, _download, asdict, atomic_write_json, bundle.extractall, confined_path, digest, directory.mkdir, directory.rglob, environment.get, file_binding, java_root.exists, java_root.glob, java_root.mkdir, len, list, lock.get, map, minimal_subprocess_env, nagini.is_file, os.uname, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, read_download_policy, read_json, require, run_recipe_stage, sorted, str, tarfile.open, time.monotonic, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[0]::Assign

Source: `scripts/roadmap_python.py:31`; AST `12d5ec69abaab032129666677f867b5883c89baf70c20643fab4540d0b76211f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, root. Outputs/bindings: lock.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[0].value::Call

Source: `scripts/roadmap_python.py:31`; AST `73c93a7e0c5cdf869ef0a412192e2e46a7e703b41ec73fe6664664654da15f7c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[1]::Expr

Source: `scripts/roadmap_python.py:32`; AST `9ccf7d43785cff82610609928b7ab58b86f155047f96bdfc3a1feccf03c1b595`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TRANSPORT, lock, require. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[1].value::Call

Source: `scripts/roadmap_python.py:32`; AST `b7a2ce8fcdd81337195a76be5553779892319213c282f0ebbc117556120432a6`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TRANSPORT, lock, require. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[1].value.args[0].left::Call

Source: `scripts/roadmap_python.py:32`; AST `0f5caa8d721fa57ccd111022f4dd4a6cb35818790520adfc04f1aa7246c5f0d0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[2]::Expr

Source: `scripts/roadmap_python.py:33`; AST `9e0e5736bb9983c902cba54d2bd6461ef5d8c81e33aba712f99e1c4e1d605074`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[2].value::Call

Source: `scripts/roadmap_python.py:33`; AST `68e33f52e333ee23abc947a223960ebb645128def6fee8a4273ee46218a8dd51`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[2].value.args[0].values[1].left.value::Call

Source: `scripts/roadmap_python.py:33`; AST `3870b6eca1eb32f0495f3ce63519015697c5abaab1b7c0cd315823eb5f223d84`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.uname.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value.args[0].values[1].left.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[3]::Assign

Source: `scripts/roadmap_python.py:34`; AST `25dde2f2000cf13fa153089ebc269c28ff4c71eb11f48d0e51267674e8ab9e4b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, digest, lock, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[3].value::Call

Source: `scripts/roadmap_python.py:34`; AST `569a0811fffb867b4486dd51b2097029cedf418479d554355f84603f82f77e3e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, digest, lock, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[3].value.args[1].right::Call

Source: `scripts/roadmap_python.py:34`; AST `5bc6a77705554ea369323608f0973231236c18cf659990724b2fdbdbb8e7067e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, lock. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value.args[1].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[4]::Expr

Source: `scripts/roadmap_python.py:35`; AST `3a400253aadde423a42d9e21da0e9ba55a3fe64614ae692874cebc9a5aa91183`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[4].value::Call

Source: `scripts/roadmap_python.py:35`; AST `7f8492ad27b11def9f8bffa8aea0180c657a9152ccc4f6a4269a7601584575c2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[5]::Assign

Source: `scripts/roadmap_python.py:36`; AST `4bf1f8e6c36f98f38e92ec4bca5e754fb5c2256335263ba3ca08b43b415056ba`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_download_policy, root, time. Outputs/bindings: deadline.
Calls/effect boundaries: read_download_policy, time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[5].value.left::Call

Source: `scripts/roadmap_python.py:36`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[5].value.right.value::Call

Source: `scripts/roadmap_python.py:36`; AST `d98a9d8f02719fd4afc66431e19bae5e085c1a1947d40c1d0c9c099b5cc2ace2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_download_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_download_policy.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value.right.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[6]::Assign

Source: `scripts/roadmap_python.py:37`; AST `c75e25187fa2f39910362a91d7b1e04db2a354b3fbe651214d5d7fbec6e94201`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _download, deadline, directory, lock, package, root. Outputs/bindings: package, wheels.
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[6].value::ListComp

Source: `scripts/roadmap_python.py:37`; AST `f8140aa6786534e15b48097ba000446ec6ede43011d1b6bf3db14885d639964f`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _download, deadline, directory, lock, package, root. Outputs/bindings: package.
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[21].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[6].value.elt::Call

Source: `scripts/roadmap_python.py:37`; AST `eea62404d3f843211bc88883172c08107d001bdddb1a58e9dbc8908bf88469cd`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _download, deadline, directory, package, root. Outputs/bindings: (none).
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[7]::Assign

Source: `scripts/roadmap_python.py:38`; AST `262c927e68b9078c3e519de1dbf82a1e95ab939d1fbc53c70d52ae76af1d6f6b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _download, deadline, directory, lock, root. Outputs/bindings: archive.
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[7].value::Call

Source: `scripts/roadmap_python.py:38`; AST `64cc7a376570d4ca3e1b4b5a8213317a81469a151a8bd6cc0aeff9ec47675b62`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _download, deadline, directory, lock, root. Outputs/bindings: (none).
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[8]::Assign

Source: `scripts/roadmap_python.py:39`; AST `d3cc52c90db1f1928405c05692d42381ed87e83c1f9f6ffac90181e5f034fff0`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: java_root.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9]::If

Source: `scripts/roadmap_python.py:40`; AST `6899dd8e2b611fd450e6369821675d6ebf092b6859d94353459e1cda64cfa256`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: archive, bundle, java_root, tarfile. Outputs/bindings: bundle.
Calls/effect boundaries: bundle.extractall, java_root.exists, java_root.mkdir, tarfile.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[21].body[9]; no call, error or mutation may be omitted. Condition: not java_root.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].test.operand::Call

Source: `scripts/roadmap_python.py:40`; AST `aaf36e2dc6ac82abec1bb41df3748c628d777a2d6c2d9755fa7edb46fb34b339`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java_root. Outputs/bindings: (none).
Calls/effect boundaries: java_root.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[0]::Expr

Source: `scripts/roadmap_python.py:41`; AST `463a43de360947e0f649b91afee9b2badd23abf78e4ac2ba69e64507e2fc0726`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: java_root. Outputs/bindings: (none).
Calls/effect boundaries: java_root.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[0].value::Call

Source: `scripts/roadmap_python.py:41`; AST `40eaa9b4abef3aa26eab8aa1ad71f3ac2dc027b4235fa38f17da91e221a4b1f0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java_root. Outputs/bindings: (none).
Calls/effect boundaries: java_root.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[1]::With

Source: `scripts/roadmap_python.py:42`; AST `bdd37e3653d75d20fecaf0a6a167f21de44810a101b875563a7fa7ec39f8d05b`.

Rust module: `scripts::roadmap_python`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: archive, bundle, java_root, tarfile. Outputs/bindings: bundle.
Calls/effect boundaries: bundle.extractall, tarfile.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered With evaluation at root.body[21].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[1].items[0].context_expr::Call

Source: `scripts/roadmap_python.py:42`; AST `3c8391d0eaf5af0677fb97c67e2a3eb2e92c9d87a7e7d6e4e78c91cb3e4c6110`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, tarfile. Outputs/bindings: (none).
Calls/effect boundaries: tarfile.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[1].body[0]::Expr

Source: `scripts/roadmap_python.py:44`; AST `24c63511e0a2a00281b46fed07cc63c7f0cf0f2b381b6d477424f9ada6fbfc4c`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bundle, java_root. Outputs/bindings: (none).
Calls/effect boundaries: bundle.extractall.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[9].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[9].body[1].body[0].value::Call

Source: `scripts/roadmap_python.py:44`; AST `694d4f9394e047a2d234dcd0fe7028aa105758011bec96dfa6d6972dd9c900a5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bundle, java_root. Outputs/bindings: (none).
Calls/effect boundaries: bundle.extractall.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[10]::Assign

Source: `scripts/roadmap_python.py:45`; AST `2c8e900f5ef5e3907f245da2baed62b94ff18b679acd18692f99e617dc291f1b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: java_root, list. Outputs/bindings: java.
Calls/effect boundaries: java_root.glob, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[10].value::Call

Source: `scripts/roadmap_python.py:45`; AST `6581e21b9a50a9c7a3e96805cf07b75687746b28287906a7d2ceda04e45cf0fd`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java_root, list. Outputs/bindings: (none).
Calls/effect boundaries: java_root.glob, list.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[10].value.args[0]::Call

Source: `scripts/roadmap_python.py:45`; AST `7a0235404ef97384d747b7b3428906885897a8c63232a6f089f29015001d6618`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java_root. Outputs/bindings: (none).
Calls/effect boundaries: java_root.glob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[11]::Expr

Source: `scripts/roadmap_python.py:46`; AST `e5cd31eb88fc5d409c53c7db56b1206a7dcebbbbcc8b4bd277b8266cb954a12c`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: java, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[11].value::Call

Source: `scripts/roadmap_python.py:46`; AST `37c14c35e6c7c208ec0086ec35e870ea2918933da98e4ba330ff1d86d8b066f4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[11].value.args[0].left::Call

Source: `scripts/roadmap_python.py:46`; AST `52455ca097d7927563ef90b8ad30f992a6fe1d495fcc1c957aa18f0db4a6977f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[12]::Assign

Source: `scripts/roadmap_python.py:47`; AST `c5ce3a3825c8be699118482ba623dfa47cdfb3b652f6c00d672d5296e7cbbaf7`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: minimal_subprocess_env. Outputs/bindings: environment.
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[12].value::Call

Source: `scripts/roadmap_python.py:47`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[13]::Assign

Source: `scripts/roadmap_python.py:48`; AST `320b60ead6c9ffead9066c501e28af5ac3999bef21fdd04d84c4bc9d16746125`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, java, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[13].value::Call

Source: `scripts/roadmap_python.py:48`; AST `ffccc88666d12e32be1c925b8298efc1262835433fa53f444086aa09dc1bc1d4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[14]::Assign

Source: `scripts/roadmap_python.py:49`; AST `dc1143f0b907d12fb6c1fa3e221c0973b5c8222717c4ec9a5c92cdce766e5485`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, java, os, str. Outputs/bindings: (none).
Calls/effect boundaries: environment.get, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[14].value.left.left::Call

Source: `scripts/roadmap_python.py:49`; AST `46510e702b169524526e7849f931cbaf1ac328c3fb7f7e82093b9197fc0c79b1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[14].value.left.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[14].value.right::Call

Source: `scripts/roadmap_python.py:49`; AST `98397f4f8e3a33633361c989a89c15d7fc81f39bb4cb1cefc9fd7ff4483eb560`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, os. Outputs/bindings: (none).
Calls/effect boundaries: environment.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[14].value.right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[15]::Assign

Source: `scripts/roadmap_python.py:50`; AST `f491671042bf13023e90b12a116a6d242a3085a2710df436f1f87431e2892182`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[16]::Assign

Source: `scripts/roadmap_python.py:51`; AST `b2b20845ca3c33880841af77a8dbd450bfed5a844c0692cd30cff6f52380a646`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: virtual.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[17]::If

Source: `scripts/roadmap_python.py:52`; AST `ef8a109a479ce8ff2656c8acccd7cfbf5d59f4dbf4a3026268220be20bb98214`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[21].body[17]; no call, error or mutation may be omitted. Condition: not (virtual / 'bin/python').exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[17].test.operand::Call

Source: `scripts/roadmap_python.py:52`; AST `11bd605d4b8042dcd6fa6abc11a7f8cb4cad169d97c1b84a16d2d67a7e3620cc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[17].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[17].body[0]::Expr

Source: `scripts/roadmap_python.py:53`; AST `92c90ec98733d58f9e12e19512aca7cdb916986d543f7f7a77af60aa471b6937`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[17].body[0].value::Call

Source: `scripts/roadmap_python.py:53`; AST `9d8c6758a1dc49b67a4c2545e4ab0a411f7954299c88c80381698e340636c690`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[17].body[0].value.func.value::Call

Source: `scripts/roadmap_python.py:53`; AST `c8c152ecb6c87d3d058f6bff59b9baee7727e29c264936c80874fedc8e1ce948`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[17].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[18]::Assign

Source: `scripts/roadmap_python.py:54`; AST `43559ae3e722df57ae62c2fc9cf97a4fe964a0d51d8e984447c1c6f5697edad4`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: virtual. Outputs/bindings: python.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[19]::Assign

Source: `scripts/roadmap_python.py:55`; AST `9c456b538f15090f53eeb65917bdbb645a9ad6e7b62eb97f160a4013789857e3`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, map, python, root, run_recipe_stage, str, wheels. Outputs/bindings: installed.
Calls/effect boundaries: map, run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[19]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[19].value::Call

Source: `scripts/roadmap_python.py:55`; AST `73438fd0ec6151fc90bc7d4a7b944563023a67dacae40dd57f4d785bd8948cf3`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, map, python, root, run_recipe_stage, str, wheels. Outputs/bindings: (none).
Calls/effect boundaries: map, run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[19].value.args[0].elts[0]::Call

Source: `scripts/roadmap_python.py:55`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[19].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[19].value.args[0].elts[7].value::Call

Source: `scripts/roadmap_python.py:55`; AST `a89a4d10f15fcf45dcb987d9b119d10ddbaa50d5511754be6250fd2c6014f9a5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: map, str, wheels. Outputs/bindings: (none).
Calls/effect boundaries: map.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[19].value.args[0].elts[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[20]::Expr

Source: `scripts/roadmap_python.py:57`; AST `6525cb86f41821490047391ab538aac5ee86696f9b16c23029737ac14e7ad2f9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, installed, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[20]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[20].value::Call

Source: `scripts/roadmap_python.py:57`; AST `12b3595fe2c4f6136efdeca4934a9dcb3700b60000f9d817a814d8a42a3d971d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, installed, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[20].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[20].value.args[1]::Call

Source: `scripts/roadmap_python.py:57`; AST `210612c034811b63a835caa940178524670109d2eb9db647878df9d8a94d06eb`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, installed. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[20].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[21]::Expr

Source: `scripts/roadmap_python.py:58`; AST `ba02caac0342c6f6094484192641e6790382b9262c47138d83350c331adacc72`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: installed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[21]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[21].value::Call

Source: `scripts/roadmap_python.py:58`; AST `db4f91c819f503378eb5f809158a102d00770dd824a6a4284a989c4456b2a043`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: installed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[21].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[22]::Assign

Source: `scripts/roadmap_python.py:59`; AST `493da46a219f19b7f5bdd1138fecfb3bb3ccb3c7b529261290c4a044ce469e49`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, python, root, run_recipe_stage, str. Outputs/bindings: checked.
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[22].value::Call

Source: `scripts/roadmap_python.py:59`; AST `dd4de1a0a528a97c3568522568f6a965c0486418e9f76425172021a6eea16c98`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, python, root, run_recipe_stage, str. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[22].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[22].value.args[0].elts[0]::Call

Source: `scripts/roadmap_python.py:59`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[22].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[23]::Expr

Source: `scripts/roadmap_python.py:60`; AST `e909733d7a6043cd3ab5f6d77c2a1502855909b208ff94e242238337b14a0e1c`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, checked, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[23].value::Call

Source: `scripts/roadmap_python.py:60`; AST `e31bb174b57a2aa0b11b83a77fbd2ff1db86d1dfa77117b8257d85ef20d93b6f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, checked, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[23].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[23].value.args[1]::Call

Source: `scripts/roadmap_python.py:60`; AST `4755b4bc2b7f511969405f25485d99b34b581cf45528e03fbf996bde6adbb64f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, checked. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[23].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[24]::Expr

Source: `scripts/roadmap_python.py:61`; AST `bf1faeb0d97405a7dd349ea52b08f6a5be6fc05237906f5b5ef9ef0c9926d016`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[24].value::Call

Source: `scripts/roadmap_python.py:61`; AST `2e5da455232d352225ab2f047b59aa0ded236ded1e438000fe97987109871f6e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[24].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[25]::Assign

Source: `scripts/roadmap_python.py:62`; AST `8d6b99ebe0739502e293a2458fe4b24a56b77a8b12cedb77b096196dae16c18d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: virtual. Outputs/bindings: nagini.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[26]::Expr

Source: `scripts/roadmap_python.py:63`; AST `01153b8a5350c660efe2b40f1b6b8a4b5d2ada4fdc7eaaf0a3ff1f61eb7b4947`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: nagini, require. Outputs/bindings: (none).
Calls/effect boundaries: nagini.is_file, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[26]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[26].value::Call

Source: `scripts/roadmap_python.py:63`; AST `bc7cd4e0ffff81ce65c6b5ebcd21a3d9cd013b79fb7ccb3b694a228e9816232f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nagini, require. Outputs/bindings: (none).
Calls/effect boundaries: nagini.is_file, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[26].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[26].value.args[0]::Call

Source: `scripts/roadmap_python.py:63`; AST `5cfe2bb0518d7b16930c9d70c64c42779026880fa9efad14d5f45bdf1d5043dd`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nagini. Outputs/bindings: (none).
Calls/effect boundaries: nagini.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[26].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[27]::Assign

Source: `scripts/roadmap_python.py:64`; AST `6784f9ed4d30ba5b37959d31f07ba211d597a3e9027c850776fdebf2084211b2`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, java, root, run_recipe_stage, str. Outputs/bindings: java_version.
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[27]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[27].value::Call

Source: `scripts/roadmap_python.py:64`; AST `03478a40a25ce0504d91aa0b65d5634be59b927b16154d80bb37346e6d61c440`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, java, root, run_recipe_stage, str. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[27].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[27].value.args[0].elts[0]::Call

Source: `scripts/roadmap_python.py:64`; AST `f1215bbe8582f5c84b9bde4d3b862538cde992af6634f5a06426ba2e53cfa7b4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[27].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[28]::Expr

Source: `scripts/roadmap_python.py:65`; AST `ba3d9e4b2d17aab3cafd35d7bb89e762613de1f0402b27b5e5d4605cc2669afb`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, java_version, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[28]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[28].value::Call

Source: `scripts/roadmap_python.py:65`; AST `c05d46da111d99a4d0d2f8ae7b7e33275dfb1f06c986657d59f059a5e40dfdc7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, java_version, output, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[28].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[28].value.args[1]::Call

Source: `scripts/roadmap_python.py:65`; AST `6887d4124266ff8b13724d9ad263bdbfe66ec635b6e156e4ced0990bd77028eb`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, java_version. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[28].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[29]::Expr

Source: `scripts/roadmap_python.py:66`; AST `f1d55b3f1dbc1efe00c489aecac5c43c9940e29048cfbdaef0acb93228454d04`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: java_version, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[29]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[29].value::Call

Source: `scripts/roadmap_python.py:66`; AST `59a4fe7c1292ba27b4c598bb315d1610d3a031ee4d7afcb69a098d8fc627e0c8`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java_version, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[29].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30]::Assign

Source: `scripts/roadmap_python.py:67`; AST `1cbbac69aff269a10d9ffd430fa4d7d8d712dfe64169e614609a90f04d918b5d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, file_binding, p, root. Outputs/bindings: files, p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[30]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value::ListComp

Source: `scripts/roadmap_python.py:67`; AST `24b9656771e727034dde025d62ba4150c889c9fca7fc388c6617099dac654b23`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: directory, file_binding, p, root. Outputs/bindings: p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[21].body[30].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.elt::Call

Source: `scripts/roadmap_python.py:67`; AST `eb79f32bd6462ca7c8c36dc6e41d01e5b8e63c36372e4a980ce6e1c1502388a6`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, p, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.elt.args[1]::Call

Source: `scripts/roadmap_python.py:67`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.elt.args[1].func.value::Call

Source: `scripts/roadmap_python.py:67`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.generators[0].iter::Call

Source: `scripts/roadmap_python.py:67`; AST `41d06ab308b2a9f6afc10dd35a5e6c7ba671d5befff73c0a5a1caa71363e86d7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_python.py:67`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[30].value.generators[0].ifs[0].values[1].operand::Call

Source: `scripts/roadmap_python.py:67`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[30].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31]::Return

Source: `scripts/roadmap_python.py:68`; AST `e5f765a0e3bacb6e1434d62d85bf1a2c30e6c259ee1d52dc6b135b9d1bd1e04b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: b, environment, file_binding, files, java, nagini, output, p, python, root, sorted, str. Outputs/bindings: p.
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix, sorted, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Return evaluation at root.body[21].body[31]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[1]::Call

Source: `scripts/roadmap_python.py:68`; AST `010d88ec2f699d93192e7aa2a4ad3a0ff5caec569a6080c1db6912798e33bff1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[2]::Call

Source: `scripts/roadmap_python.py:69`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[3]::Call

Source: `scripts/roadmap_python.py:69`; AST `3b1216b53a3d540b94fa9808acc8350b92344fa373698cf6bade25de0af87030`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: nagini, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[4]::Call

Source: `scripts/roadmap_python.py:69`; AST `f1215bbe8582f5c84b9bde4d3b862538cde992af6634f5a06426ba2e53cfa7b4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: java, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[6]::Call

Source: `scripts/roadmap_python.py:70`; AST `a5616fd6a71280cc0021ec98e0e0aa0aaf2df557f2242b1ce25a206fc8069837`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[6].keywords[0].value::Lambda

Source: `scripts/roadmap_python.py:70`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `scripts::roadmap_python`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Lambda evaluation at root.body[21].body[31].value.values[6].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[7]::ListComp

Source: `scripts/roadmap_python.py:71`; AST `8b04a3d0dd685aa5e04e7b66e63a5bc8be4ae2b08da8d39ee33ebb53178feb98`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: file_binding, output, p, root. Outputs/bindings: p.
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[21].body[31].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[7].elt::Call

Source: `scripts/roadmap_python.py:71`; AST `eb79f32bd6462ca7c8c36dc6e41d01e5b8e63c36372e4a980ce6e1c1502388a6`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, p, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[7].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[7].elt.args[1]::Call

Source: `scripts/roadmap_python.py:71`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[7].elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision::root.body[21].body[31].value.values[7].elt.args[1].func.value::Call

Source: `scripts/roadmap_python.py:71`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[21].body[31].value.values[7].elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22]::FunctionDef

Source: `scripts/roadmap_python.py:74`; AST `70089cd9fd9b5737021f7c834bf90360f0d873ed1a9395374121766ea88301af`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, asdict, atomic_write_json, bindings_current, classify_nagini, confined_path, dict, environment, file_binding, name, outcomes, output, path, r, read_json, require, result, root, run_recipe_stage, runs, source, source_closure, str, toolchain, toolchain_path. Outputs/bindings: environment, name, outcomes, path, r, result, runs, source, toolchain.
Calls/effect boundaries: asdict, atomic_write_json, bindings_current, classify_nagini, confined_path, dict, file_binding, path.relative_to, path.relative_to(root).as_posix, read_json, require, run_recipe_stage, runs.append, source.relative_to, source.relative_to(root).as_posix, source_closure, str, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[22]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[0]::ImportFrom

Source: `scripts/roadmap_python.py:75`; AST `c6e174db190e1f7a5b03692c2207b27dec7b5d6aff6a54225de2fb27245d25c8`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[22].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[1]::Assign

Source: `scripts/roadmap_python.py:76`; AST `306834594d91496c2087b429d7388547edeb1770e5e25cd42ecffc9433459f0e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: toolchain.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[1].value::Call

Source: `scripts/roadmap_python.py:76`; AST `cef1490a0865a886283dc1abfdd972486c9964aa9e05ad3933980f4f22e59e83`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[1].value.args[0]::Call

Source: `scripts/roadmap_python.py:76`; AST `224b2b021d2f344194abcb6afa9f4b3ede25cf388cb616010c2eade7e5ad9cbc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[2]::Expr

Source: `scripts/roadmap_python.py:77`; AST `e9e189d7fd25cf618c2a8648993cd18646fcb0f4525d06ffc1ce4cdd20d7670a`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[2].value::Call

Source: `scripts/roadmap_python.py:77`; AST `cc00c5e7a09a1cb623684e8863557edffc7e05c682883e85ad0356f23c5c7d76`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[2].value.args[0].values[0].left::Call

Source: `scripts/roadmap_python.py:77`; AST `d80367ddfb01184b29a244b9798c54812da40b621eb6b5ee31d30a9dcc39ffde`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[2].value.args[0].values[1]::Call

Source: `scripts/roadmap_python.py:77`; AST `64e1b5503b253dbdee4864571a094096e1f33de17822726e8510f2260e79d70c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[2].value.args[0].values[2]::Call

Source: `scripts/roadmap_python.py:78`; AST `7f46eb67eba00ce282498e09bbb444da3dee6994e8fa34c81526f04c5ef6ae64`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[3]::Assign

Source: `scripts/roadmap_python.py:79`; AST `1537ccbd1bc08accb2da96895f104c95d8887aa8a9532ce75a46f0e921cd4e32`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: runs.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4]::For

Source: `scripts/roadmap_python.py:80`; AST `a7da313865b07105d257c2485a308d6616e98a6e919c8de68d923de02a452668`.

Rust module: `scripts::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: asdict, atomic_write_json, classify_nagini, dict, environment, file_binding, name, output, path, result, root, run_recipe_stage, runs, source, str, toolchain. Outputs/bindings: environment, name, path, result, source.
Calls/effect boundaries: asdict, atomic_write_json, classify_nagini, dict, file_binding, path.relative_to, path.relative_to(root).as_posix, run_recipe_stage, runs.append, source.relative_to, source.relative_to(root).as_posix, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered For evaluation at root.body[22].body[4]; no call, error or mutation may be omitted. Iteration: name in ('policy_positive.py', 'policy_negative.py')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[0]::Assign

Source: `scripts/roadmap_python.py:81`; AST `f3f503d1b5d5a11feb6a65d179b71be0b7131338d42c04b2dd8461e9d00d7b4f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, root. Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[1]::Assign

Source: `scripts/roadmap_python.py:82`; AST `b0f5a976c353ff46b9e952e0affda5bff4199b4dd0749c53cd4b0291d896dfa9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, root, str, toolchain. Outputs/bindings: environment.
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[1].value::Call

Source: `scripts/roadmap_python.py:82`; AST `57ea3b8b55992d9f462c6a087dd4b01ec531e2d04433853ec0023e1d080c2914`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, root, str, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[1].value.keywords[0].value::Call

Source: `scripts/roadmap_python.py:82`; AST `5e78564dad6f72b4fffe70a2682a87198ad49cb6d6eea55e10061b531d18c330`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[1].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[1].value.keywords[1].value::Call

Source: `scripts/roadmap_python.py:82`; AST `5e78564dad6f72b4fffe70a2682a87198ad49cb6d6eea55e10061b531d18c330`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[1].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[2]::Assign

Source: `scripts/roadmap_python.py:83`; AST `aba5ac24d901ecee632ad10b0fab17caf825727cb4d5e738e6e28e1467026eef`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, root, run_recipe_stage, source, str, toolchain. Outputs/bindings: result.
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[2].value::Call

Source: `scripts/roadmap_python.py:83`; AST `d53df10d40e28345b61020aa7282bbd5945264c89762d01d4f926a523b85764a`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, root, run_recipe_stage, source, str, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[2].value.args[0].elts[4]::Call

Source: `scripts/roadmap_python.py:83`; AST `5e78564dad6f72b4fffe70a2682a87198ad49cb6d6eea55e10061b531d18c330`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[2].value.args[0].elts[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[2].value.args[0].elts[5]::Call

Source: `scripts/roadmap_python.py:83`; AST `e84c9c7864af0fee24e28123120dae12990caa3a9145d280b7a0f55e8d6cb247`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[2].value.args[0].elts[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[3]::Assign

Source: `scripts/roadmap_python.py:85`; AST `39a26a80de8225c82c7f971e249275b7d9fbf528e6ccf2c2b57f5a7d8b262434`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[4]::Expr

Source: `scripts/roadmap_python.py:86`; AST `bdf64811b95b939af6ea7eee41b9e91eea1f56f98d54e9f689f3d30d19491963`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[4].value::Call

Source: `scripts/roadmap_python.py:86`; AST `4298a9f4fcb2b3067e14867dbddab90daed2957656839048e079cfe3c3b3ef03`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[4].value.args[1]::Call

Source: `scripts/roadmap_python.py:86`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5]::Expr

Source: `scripts/roadmap_python.py:87`; AST `53c50e339c85918f7b7605153f26d08f17e98c4bf4237abfee33758bc23d4d31`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, classify_nagini, file_binding, name, path, result, root, runs, source. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_nagini, file_binding, path.relative_to, path.relative_to(root).as_posix, runs.append, source.relative_to, source.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[22].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value::Call

Source: `scripts/roadmap_python.py:87`; AST `d8fd96c71d1a67e428fa12e7281c4e784ca82fe952a3d3d22051b13187d54957`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, classify_nagini, file_binding, name, path, result, root, runs, source. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_nagini, file_binding, path.relative_to, path.relative_to(root).as_posix, runs.append, source.relative_to, source.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[0]::Call

Source: `scripts/roadmap_python.py:87`; AST `024f6e539e30fb0a95524dc8f02b61f03c77b125404a19d509194caff0e1b386`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root, source. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, source.relative_to, source.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[0].args[1]::Call

Source: `scripts/roadmap_python.py:87`; AST `1f0db1566b0b42680a7861e89191e5cbc3898bfd922c928ce672947d457af197`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source. Outputs/bindings: (none).
Calls/effect boundaries: source.relative_to, source.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[0].args[1].func.value::Call

Source: `scripts/roadmap_python.py:87`; AST `fb0676198be242c6af2ee7fb4f0304edb4a20957b913b02277e1f8ddff4b54b0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source. Outputs/bindings: (none).
Calls/effect boundaries: source.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[2]::Call

Source: `scripts/roadmap_python.py:89`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[2].args[1]::Call

Source: `scripts/roadmap_python.py:89`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[2].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[2].args[1].func.value::Call

Source: `scripts/roadmap_python.py:89`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[2].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[3]::Call

Source: `scripts/roadmap_python.py:89`; AST `758996ba9d1b0205a3fa645d144d02dfb210eb453b8617239c1dfaa9682419f9`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, classify_nagini, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_nagini.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[4].body[5].value.args[0].values[3].args[0]::Call

Source: `scripts/roadmap_python.py:89`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[4].body[5].value.args[0].values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[5]::Assign

Source: `scripts/roadmap_python.py:90`; AST `341e386ad5d1c9fca275cff7c223f70f756305b9006490f5b5a1f9a4c6161b4d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: r, runs. Outputs/bindings: outcomes, r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[22].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[5].value::ListComp

Source: `scripts/roadmap_python.py:90`; AST `611d10573a0bc72804c2e865ef7c979c3533644f2f65966a172f3033d11468bd`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, runs. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[22].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6]::Return

Source: `scripts/roadmap_python.py:91`; AST `ac67412aa7806e2d93f23020b7c26fa190f4318b121c4ebfd8c5ae7b0b8095aa`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, outcomes, r, root, runs, source_closure, toolchain_path. Outputs/bindings: r.
Calls/effect boundaries: file_binding, source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Return evaluation at root.body[22].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6].value.values[2]::Call

Source: `scripts/roadmap_python.py:92`; AST `9541f4c9d8dff7d7ff3112bf1ab4deb4b2305a0241438b75b655ce54f3816385`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6].value.values[3]::Call

Source: `scripts/roadmap_python.py:93`; AST `5490821019984d7c4f8f46ec5cf3fa43c46111d139cff228c93af8e6fae119fb`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6].value.values[4]::Call

Source: `scripts/roadmap_python.py:94`; AST `d1ab105f67a191a692ccfa7349ad4ff83b44f59a053df2c13003cd86b60ff40f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[22].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6].value.values[6].left::ListComp

Source: `scripts/roadmap_python.py:95`; AST `a428dbdca04d294088d60fb88883268bfe74937c3772e04253bd37a29b6a2449`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, runs. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[22].body[6].value.values[6].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify::root.body[22].body[6].value.values[6].right::ListComp

Source: `scripts/roadmap_python.py:95`; AST `9e672898d76c9c52a33593090c6aa33543d77fc3c60c51aff43282e1aa3f74b9`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: r, runs. Outputs/bindings: r.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[22].body[6].value.values[6].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23]::FunctionDef

Source: `scripts/roadmap_python.py:99`; AST `fdc303f85e7ea173896df35d04bc70699d43a536117de16e52aa129d0ab4b0f2`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, TRANSPORT, _download, argv, artifacts, asdict, atomic_write_json, b, confined_path, deadline, dict, digest, directory, entry, environment, file_binding, files, lock, map, minimal_subprocess_env, name, os, output, p, path, profile, python, read_download_policy, read_json, require, result, root, run_recipe_stage, sorted, str, sys, time, venv, virtual, wheels. Outputs/bindings: argv, artifacts, deadline, directory, entry, environment, files, lock, name, p, path, profile, python, result, virtual, wheels.
Calls/effect boundaries: (virtual / 'bin/python').exists, _download, artifacts.append, asdict, atomic_write_json, confined_path, dict, digest, directory.mkdir, directory.rglob, file_binding, lock.get, map, minimal_subprocess_env, os.uname, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, path.relative_to, path.relative_to(root).as_posix, read_download_policy, read_json, require, run_recipe_stage, sorted, str, time.monotonic, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[0]::Assign

Source: `scripts/roadmap_python.py:100`; AST `a606f4a772ef53afc0e084c72e7d050779d0b4e2926c7b81865faf1b003aa839`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[1]::Assign

Source: `scripts/roadmap_python.py:101`; AST `7aecf23f5d65b5be9f380a1a662abcf9abfce99ab389cd2ea6066f6663437a44`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, read_json, root. Outputs/bindings: lock.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[1].value::Call

Source: `scripts/roadmap_python.py:101`; AST `6fd2eb6d22afaa8b938ef1733d08c0a4e3d0f1703f57a7ba8d12fd1d75c03749`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[2]::Expr

Source: `scripts/roadmap_python.py:102`; AST `0a8a26b80506eb92a57fae58356ea3b05048e1dac32dccbaf8e7d4e062f5d814`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TRANSPORT, lock, os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[2].value::Call

Source: `scripts/roadmap_python.py:102`; AST `45cd8f8e414e3c5637fe11f7e048ae0cd9e312017c4bb1c18c0ae4b05ad943c5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TRANSPORT, lock, os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[2].value.args[0].values[0].left::Call

Source: `scripts/roadmap_python.py:102`; AST `391afc41ac06cfbbb7183fbada92250cec99cb0f89877d6370006cc407c99917`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[2].value.args[0].values[1].left::Call

Source: `scripts/roadmap_python.py:102`; AST `0f5caa8d721fa57ccd111022f4dd4a6cb35818790520adfc04f1aa7246c5f0d0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[2].value.args[0].values[3].left.value::Call

Source: `scripts/roadmap_python.py:103`; AST `3870b6eca1eb32f0495f3ce63519015697c5abaab1b7c0cd315823eb5f223d84`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.uname.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value.args[0].values[3].left.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[3]::Assign

Source: `scripts/roadmap_python.py:105`; AST `845d7f2a79ff7fda9729973db68496a4dab6671c9ea1750c3151256a0f1196b7`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, digest, lock, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[3].value::Call

Source: `scripts/roadmap_python.py:105`; AST `c8a095e8031297a508213ffd4e4d6727167e6338d73f9e8826651d07591f31b2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, digest, lock, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[3].value.args[1].right::Call

Source: `scripts/roadmap_python.py:105`; AST `5bc6a77705554ea369323608f0973231236c18cf659990724b2fdbdbb8e7067e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, lock. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].value.args[1].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[4]::Expr

Source: `scripts/roadmap_python.py:106`; AST `3a400253aadde423a42d9e21da0e9ba55a3fe64614ae692874cebc9a5aa91183`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[4].value::Call

Source: `scripts/roadmap_python.py:106`; AST `7f8492ad27b11def9f8bffa8aea0180c657a9152ccc4f6a4269a7601584575c2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[5]::Assign

Source: `scripts/roadmap_python.py:107`; AST `4bf1f8e6c36f98f38e92ec4bca5e754fb5c2256335263ba3ca08b43b415056ba`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_download_policy, root, time. Outputs/bindings: deadline.
Calls/effect boundaries: read_download_policy, time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[5].value.left::Call

Source: `scripts/roadmap_python.py:107`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[5].value.right.value::Call

Source: `scripts/roadmap_python.py:107`; AST `d98a9d8f02719fd4afc66431e19bae5e085c1a1947d40c1d0c9c099b5cc2ace2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_download_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_download_policy.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[5].value.right.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[6]::Assign

Source: `scripts/roadmap_python.py:108`; AST `4c53f4b0dd4c8e5282e064eee656626a245618a62acbe257418c1b09873c94da`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _download, deadline, directory, entry, lock, root. Outputs/bindings: entry, wheels.
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[6].value::ListComp

Source: `scripts/roadmap_python.py:108`; AST `18a42b45580125a3f194b2f927adebb12c6040b3ae1c63ab5bd1d3c18566e611`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: _download, deadline, directory, entry, lock, root. Outputs/bindings: entry.
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[23].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[6].value.elt::Call

Source: `scripts/roadmap_python.py:108`; AST `ce5bc5576656e15229112cf6232fd1e4208d310b097dafa38c400d964ee17e6b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _download, deadline, directory, entry, root. Outputs/bindings: (none).
Calls/effect boundaries: _download.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[7]::Assign

Source: `scripts/roadmap_python.py:109`; AST `b2b20845ca3c33880841af77a8dbd450bfed5a844c0692cd30cff6f52380a646`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: virtual.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[8]::If

Source: `scripts/roadmap_python.py:110`; AST `ef8a109a479ce8ff2656c8acccd7cfbf5d59f4dbf4a3026268220be20bb98214`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[23].body[8]; no call, error or mutation may be omitted. Condition: not (virtual / 'bin/python').exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[8].test.operand::Call

Source: `scripts/roadmap_python.py:110`; AST `11bd605d4b8042dcd6fa6abc11a7f8cb4cad169d97c1b84a16d2d67a7e3620cc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[8].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[8].body[0]::Expr

Source: `scripts/roadmap_python.py:111`; AST `92c90ec98733d58f9e12e19512aca7cdb916986d543f7f7a77af60aa471b6937`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[8].body[0].value::Call

Source: `scripts/roadmap_python.py:111`; AST `9d8c6758a1dc49b67a4c2545e4ab0a411f7954299c88c80381698e340636c690`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[8].body[0].value.func.value::Call

Source: `scripts/roadmap_python.py:111`; AST `c8c152ecb6c87d3d058f6bff59b9baee7727e29c264936c80874fedc8e1ce948`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[8].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[9]::Assign

Source: `scripts/roadmap_python.py:112`; AST `43559ae3e722df57ae62c2fc9cf97a4fe964a0d51d8e984447c1c6f5697edad4`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: virtual. Outputs/bindings: python.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[10]::Assign

Source: `scripts/roadmap_python.py:113`; AST `90741055731cbeff50b1bfc7ce711dd5785e69026a59df14f5d64d15e9ae2357`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, minimal_subprocess_env. Outputs/bindings: environment.
Calls/effect boundaries: dict, minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[10].value::Call

Source: `scripts/roadmap_python.py:113`; AST `c5a0a6503fc8a5d3eacd42fdb4d780b2e8a2999d1aa5a4c4f797810639f816e5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: dict, minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[10].value.args[0]::Call

Source: `scripts/roadmap_python.py:113`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[10].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[11]::Assign

Source: `scripts/roadmap_python.py:114`; AST `e73c528694ffe6c1c84fbb9c5ff044ae0c34a914494eadac59b06b6361649f86`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: artifacts.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12]::For

Source: `scripts/roadmap_python.py:115`; AST `e2bddb51ed36a29d4e55cde03fb91aa0ec41cddd5a98ed1713d30dfaaa496e4d`.

Rust module: `scripts::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: argv, artifacts, asdict, atomic_write_json, environment, file_binding, map, name, output, path, python, require, result, root, run_recipe_stage, str, wheels. Outputs/bindings: argv, name, path, result.
Calls/effect boundaries: artifacts.append, asdict, atomic_write_json, file_binding, map, path.relative_to, path.relative_to(root).as_posix, require, run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered For evaluation at root.body[23].body[12]; no call, error or mutation may be omitted. Iteration: (name, argv) in (('pip-result.json', [str(python), '-B', '-m', 'pip', 'install', '--no-index', '--no-deps', *map(str, wheels)]), ('pip-check.json', [str(python), '-B', '-m', 'pip', 'check']))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].iter.elts[0].elts[1].elts[0]::Call

Source: `scripts/roadmap_python.py:115`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].iter.elts[0].elts[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].iter.elts[0].elts[1].elts[7].value::Call

Source: `scripts/roadmap_python.py:115`; AST `a89a4d10f15fcf45dcb987d9b119d10ddbaa50d5511754be6250fd2c6014f9a5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: map, str, wheels. Outputs/bindings: (none).
Calls/effect boundaries: map.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].iter.elts[0].elts[1].elts[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].iter.elts[1].elts[1].elts[0]::Call

Source: `scripts/roadmap_python.py:116`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].iter.elts[1].elts[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[0]::Assign

Source: `scripts/roadmap_python.py:117`; AST `f802c75c13444cf33fce4ad0ed80bf5ebea0a9cbda411ba7a80ff595533d76b8`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, environment, root, run_recipe_stage. Outputs/bindings: result.
Calls/effect boundaries: run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[0].value::Call

Source: `scripts/roadmap_python.py:117`; AST `bac19288464b2af15e29ca4705aaea6181d029c19012982d97b42b281688e44d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, environment, root, run_recipe_stage. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[1]::Assign

Source: `scripts/roadmap_python.py:118`; AST `ac0bc25cee3c3769a8aa769d7aba83147b4f929c077f08642b3fd8ead84b76a2`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[2]::Expr

Source: `scripts/roadmap_python.py:119`; AST `bdf64811b95b939af6ea7eee41b9e91eea1f56f98d54e9f689f3d30d19491963`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[2].value::Call

Source: `scripts/roadmap_python.py:119`; AST `4298a9f4fcb2b3067e14867dbddab90daed2957656839048e079cfe3c3b3ef03`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[2].value.args[1]::Call

Source: `scripts/roadmap_python.py:119`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[3]::Expr

Source: `scripts/roadmap_python.py:120`; AST `2fc28c9d3bb8691ddc6e6a5a99873506f698d9fc5ca9b29c6b631fd7fb891e85`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append, file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[3].value::Call

Source: `scripts/roadmap_python.py:120`; AST `efeb05caed238acf36201da7b921c24980b7cc5422c0ec64affe731fbca1892e`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append, file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[3].value.args[0]::Call

Source: `scripts/roadmap_python.py:120`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[3].value.args[0].args[1]::Call

Source: `scripts/roadmap_python.py:120`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[3].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[3].value.args[0].args[1].func.value::Call

Source: `scripts/roadmap_python.py:120`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[3].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[4]::Expr

Source: `scripts/roadmap_python.py:121`; AST `a5c1243fde311297599e86d43f6f0ff83403cac3d549a0b72e353645512b6405`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[12].body[4].value::Call

Source: `scripts/roadmap_python.py:121`; AST `91471b5eb09b18e17692ec7f9bad0aa8e7104e423abbbde653755f92959534b5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13]::Assign

Source: `scripts/roadmap_python.py:123`; AST `1cbbac69aff269a10d9ffd430fa4d7d8d712dfe64169e614609a90f04d918b5d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, file_binding, p, root. Outputs/bindings: files, p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value::ListComp

Source: `scripts/roadmap_python.py:123`; AST `24b9656771e727034dde025d62ba4150c889c9fca7fc388c6617099dac654b23`.

Rust module: `scripts::roadmap_python`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: directory, file_binding, p, root. Outputs/bindings: p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[23].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.elt::Call

Source: `scripts/roadmap_python.py:123`; AST `eb79f32bd6462ca7c8c36dc6e41d01e5b8e63c36372e4a980ce6e1c1502388a6`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, p, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.elt.args[1]::Call

Source: `scripts/roadmap_python.py:123`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.elt.args[1].func.value::Call

Source: `scripts/roadmap_python.py:123`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.generators[0].iter::Call

Source: `scripts/roadmap_python.py:123`; AST `41d06ab308b2a9f6afc10dd35a5e6c7ba671d5befff73c0a5a1caa71363e86d7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_python.py:124`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[13].value.generators[0].ifs[0].values[1].operand::Call

Source: `scripts/roadmap_python.py:124`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[13].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[14]::Return

Source: `scripts/roadmap_python.py:125`; AST `d8fb0dfff48d91373ce7c9285c8596afd3cfb3491e9167792e1c0b46a06ca190`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, b, environment, file_binding, files, profile, python, root, sorted, str. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, sorted, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Return evaluation at root.body[23].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[14].value.values[2]::Call

Source: `scripts/roadmap_python.py:125`; AST `bbac3d3e2068529355b1ab743fb0e27184efd487afe79aa051c725805e327339`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[14].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[14].value.values[3]::Call

Source: `scripts/roadmap_python.py:126`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[14].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[14].value.values[5]::Call

Source: `scripts/roadmap_python.py:126`; AST `a5616fd6a71280cc0021ec98e0e0aa0aaf2df557f2242b1ce25a206fc8069837`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[14].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::provision_deal::root.body[23].body[14].value.values[5].keywords[0].value::Lambda

Source: `scripts/roadmap_python.py:126`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `scripts::roadmap_python`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Lambda evaluation at root.body[23].body[14].value.values[5].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24]::FunctionDef

Source: `scripts/roadmap_python.py:129`; AST `189bb90f811d553d0afb8ac2d842ee2aaed5b490072d1e495f71f03b917b6438`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, artifacts, asdict, atomic_write_json, binding, bindings_current, classify_deal, confined_path, dependencies, dict, environment, file_binding, fixture, len, name, observed, observed_path, output, read_json, require, result, result_path, root, run_recipe_stage, runs, source_closure, str, toolchain, toolchain_path. Outputs/bindings: artifacts, binding, dependencies, environment, fixture, name, observed, observed_path, result, result_path, runs, toolchain.
Calls/effect boundaries: artifacts.extend, asdict, atomic_write_json, bindings_current, classify_deal, confined_path, dependencies.append, dict, file_binding, len, observed_path.is_file, observed_path.relative_to, observed_path.relative_to(root).as_posix, read_json, require, result_path.relative_to, result_path.relative_to(root).as_posix, run_recipe_stage, runs.append, source_closure, str, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[24]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[0]::ImportFrom

Source: `scripts/roadmap_python.py:130`; AST `c6e174db190e1f7a5b03692c2207b27dec7b5d6aff6a54225de2fb27245d25c8`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[1]::Assign

Source: `scripts/roadmap_python.py:131`; AST `9c4ed075341df239cefc71fc85e737c489c52b1edf0734eae30e1f6ed63824be`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, root, toolchain_path. Outputs/bindings: binding.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[1].value::Call

Source: `scripts/roadmap_python.py:131`; AST `d1ab105f67a191a692ccfa7349ad4ff83b44f59a053df2c13003cd86b60ff40f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[2]::Assign

Source: `scripts/roadmap_python.py:132`; AST `306834594d91496c2087b429d7388547edeb1770e5e25cd42ecffc9433459f0e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: toolchain.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[2].value::Call

Source: `scripts/roadmap_python.py:132`; AST `cef1490a0865a886283dc1abfdd972486c9964aa9e05ad3933980f4f22e59e83`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[2].value.args[0]::Call

Source: `scripts/roadmap_python.py:132`; AST `224b2b021d2f344194abcb6afa9f4b3ede25cf388cb616010c2eade7e5ad9cbc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[3]::Expr

Source: `scripts/roadmap_python.py:133`; AST `cf2095c22195981ba08ebc18c8fe28ad99833e62f8b4fd7451df11cbebfc38f0`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[3].value::Call

Source: `scripts/roadmap_python.py:133`; AST `f98ac6c65678c113a950c5579f63b95e1589b01c837c7e67deec78b930bf1ee6`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[3].value.args[0].values[0].left::Call

Source: `scripts/roadmap_python.py:133`; AST `a1570292a8fc75ba5ee5d3c375d6190adbc55c1d07ea99d6aa2674ae094cc85b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[3].value.args[0].values[1].left::Call

Source: `scripts/roadmap_python.py:133`; AST `d80367ddfb01184b29a244b9798c54812da40b621eb6b5ee31d30a9dcc39ffde`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[3].value.args[0].values[2]::Call

Source: `scripts/roadmap_python.py:134`; AST `eaa22374d32a9f53d86375fd8b957817f509b6715f81bf2b7cf491a514306a1c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[3].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[4]::Assign

Source: `scripts/roadmap_python.py:135`; AST `17b32c4c49775e968c12298fd4b6e8bd96e47be5f177cdce50ea94c7faa0c167`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: artifacts, runs.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5]::For

Source: `scripts/roadmap_python.py:136`; AST `80711ac1abc22e738a41cf19220399072cab8d7ec3cbb002be74b693c08f6484`.

Rust module: `scripts::roadmap_python`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: artifacts, asdict, atomic_write_json, classify_deal, dependencies, dict, environment, file_binding, fixture, len, name, observed, observed_path, output, read_json, result, result_path, root, run_recipe_stage, runs, str, toolchain. Outputs/bindings: dependencies, environment, fixture, name, observed, observed_path, result, result_path.
Calls/effect boundaries: artifacts.extend, asdict, atomic_write_json, classify_deal, dependencies.append, dict, file_binding, len, observed_path.is_file, observed_path.relative_to, observed_path.relative_to(root).as_posix, read_json, result_path.relative_to, result_path.relative_to(root).as_posix, run_recipe_stage, runs.append, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered For evaluation at root.body[24].body[5]; no call, error or mutation may be omitted. Iteration: name in ('policy_deal_positive.py', 'policy_deal_negative.py')
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[0]::Assign

Source: `scripts/roadmap_python.py:137`; AST `7077b03c695e271045a9bb384fbd97125542515450b2a10511862a77efb2b403`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, name, root. Outputs/bindings: fixture.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[0].value::Call

Source: `scripts/roadmap_python.py:137`; AST `b0a7348dff571b978183e11d8fd0eca126d3a255189c19f890c1933cf16fc626`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, name, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[1]::Assign

Source: `scripts/roadmap_python.py:138`; AST `ad81e47c20d9c17a897dde7c9e8cf07e07ad7db99f6958adaa6ac92847c912ab`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: observed_path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[2]::Assign

Source: `scripts/roadmap_python.py:139`; AST `9347fa70e47d26b03dbcee0c7d1745424cd50b1bf09c8caddaa0eead93f4d9ee`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, root, str, toolchain. Outputs/bindings: environment.
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[2].value::Call

Source: `scripts/roadmap_python.py:139`; AST `16088de01e02bae46fa5180a27baf07590f959a32d214ff60c7ad8a91f216506`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, root, str, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[2].value.keywords[0].value::Call

Source: `scripts/roadmap_python.py:139`; AST `5e78564dad6f72b4fffe70a2682a87198ad49cb6d6eea55e10061b531d18c330`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[2].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[3]::Assign

Source: `scripts/roadmap_python.py:140`; AST `8e242f6ed42bba1c2c1cef646370da55d03d091f9b2369db60f3da293a686828`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, fixture, observed_path, root, run_recipe_stage, toolchain. Outputs/bindings: result.
Calls/effect boundaries: observed_path.relative_to, observed_path.relative_to(root).as_posix, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[3].value::Call

Source: `scripts/roadmap_python.py:140`; AST `624d672349731e77cd6626b2ba21309a66c68ba5df4358fcaa83c561adbf6841`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, fixture, observed_path, root, run_recipe_stage, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.relative_to, observed_path.relative_to(root).as_posix, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[3].value.args[0].elts[6]::Call

Source: `scripts/roadmap_python.py:141`; AST `744ad34d1dd930380b95f62e5cdfa77e43e1dd85b64064bd8731ab8c2ee829ea`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[3].value.args[0].elts[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[3].value.args[0].elts[6].func.value::Call

Source: `scripts/roadmap_python.py:141`; AST `ad64743c5828a6afdc8300d853fe734360b715509e61dea27352e4eee848675d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[3].value.args[0].elts[6].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[4]::Assign

Source: `scripts/roadmap_python.py:143`; AST `900964ea1d3bdd4e277e8dea84bebfda6e6a7d88231a0dce597c93c14e34de4f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: result_path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[5]::Expr

Source: `scripts/roadmap_python.py:144`; AST `9294b3a1af10534fe4f456bf2012878322ecc5fc2d6526c2fd2f001cc3d92d81`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, result, result_path, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[5].value::Call

Source: `scripts/roadmap_python.py:144`; AST `ef0a5efe724204845a5730a080a264d37b5c5206b2db0a67702920a59f090c63`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, result, result_path, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[5].value.args[1]::Call

Source: `scripts/roadmap_python.py:144`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[6]::Assign

Source: `scripts/roadmap_python.py:145`; AST `41ab27ef9f9800d3666b43dd3f1533e03b64debd04f652df3372ce4f659dd5ac`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observed_path, read_json. Outputs/bindings: observed.
Calls/effect boundaries: observed_path.is_file, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[6].value.test::Call

Source: `scripts/roadmap_python.py:145`; AST `9f113d86aea2d40617e2d8874ddd1bee86d4cb81a923656e8d4c374cabe2be72`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[6].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[6].value.body::Call

Source: `scripts/roadmap_python.py:145`; AST `b6ad5173e7bf9ac69109c922ed0f7b03d3003e847a2f0625a9a96f78270321b0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[6].value.body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[7]::Assign

Source: `scripts/roadmap_python.py:146`; AST `e128a6533114b99a906142499ccd0998d27da2aee77019d3bdc2456acb1b46f5`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, fixture, result_path, root. Outputs/bindings: dependencies.
Calls/effect boundaries: file_binding, result_path.relative_to, result_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[24].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[7].value.elts[1]::Call

Source: `scripts/roadmap_python.py:146`; AST `f95820ee354a28ac49b9b76c1f96761ed99f45071499ba3555908fb46ba17020`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, result_path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, result_path.relative_to, result_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[7].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[7].value.elts[1].args[1]::Call

Source: `scripts/roadmap_python.py:146`; AST `5848da8a3673fa298a0710ca48301cce9b87133aea7b05a8cc8ed0a38e8ecfe2`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result_path, root. Outputs/bindings: (none).
Calls/effect boundaries: result_path.relative_to, result_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[7].value.elts[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[7].value.elts[1].args[1].func.value::Call

Source: `scripts/roadmap_python.py:146`; AST `83e7299a5bfac5eeb5774f1ab68d9e6dae3550a2290f3c9ce2fdd27c5a49e0ad`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: result_path, root. Outputs/bindings: (none).
Calls/effect boundaries: result_path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[7].value.elts[1].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8]::If

Source: `scripts/roadmap_python.py:147`; AST `f954467616f50db0022030a677e30b8e53af376e1593d0ccb0df97446937b87a`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: dependencies, file_binding, observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.append, file_binding, observed_path.is_file, observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[24].body[5].body[8]; no call, error or mutation may be omitted. Condition: observed_path.is_file()
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].test::Call

Source: `scripts/roadmap_python.py:147`; AST `9f113d86aea2d40617e2d8874ddd1bee86d4cb81a923656e8d4c374cabe2be72`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[8].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].body[0]::Expr

Source: `scripts/roadmap_python.py:148`; AST `956bcd9cf522a0f01fe411492aeb25eb85464a652945994c5cba5d83ecaa6761`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dependencies, file_binding, observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.append, file_binding, observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].body[0].value::Call

Source: `scripts/roadmap_python.py:148`; AST `52bf8cc9b8fe9cea645f3941c7e3b888e61da28bed987e40be0955a90692501b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, file_binding, observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: dependencies.append, file_binding, observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].body[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:148`; AST `fade9c579d8b8064fd497f2de8d0c9960ed44b98e77b2647a6340880dadf7711`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[8].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].body[0].value.args[0].args[1]::Call

Source: `scripts/roadmap_python.py:148`; AST `744ad34d1dd930380b95f62e5cdfa77e43e1dd85b64064bd8731ab8c2ee829ea`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.relative_to, observed_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[8].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[8].body[0].value.args[0].args[1].func.value::Call

Source: `scripts/roadmap_python.py:148`; AST `ad64743c5828a6afdc8300d853fe734360b715509e61dea27352e4eee848675d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observed_path, root. Outputs/bindings: (none).
Calls/effect boundaries: observed_path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[8].body[0].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[9]::Expr

Source: `scripts/roadmap_python.py:149`; AST `bb37692e36285d0a6c330562b6d3fb9ed483ec69f8f23bb924a1389e5726a187`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, dependencies. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.extend.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[9].value::Call

Source: `scripts/roadmap_python.py:149`; AST `edf46d989fb2367484cb35dbaaf7ea53b4fe6d8ad4732d7867f1073916a69c12`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, dependencies. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.extend.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[10]::Expr

Source: `scripts/roadmap_python.py:150`; AST `11f080f47ea5b3b800d47fe472fb33597abc365f6674f4aeded2b8b313c373c5`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, classify_deal, dependencies, fixture, len, name, observed, result, runs. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_deal, len, runs.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[10].value::Call

Source: `scripts/roadmap_python.py:150`; AST `cf5d5e66ad463f72165a35b7e35ea21b55ced4e84940325aa1877fd3b13478ae`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, classify_deal, dependencies, fixture, len, name, observed, result, runs. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_deal, len, runs.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[10].value.args[0].values[3].test.left::Call

Source: `scripts/roadmap_python.py:151`; AST `5c4d38e06072bc25cc32b98e2fcb6778dfb58ca4d71fee56c61f12724a7eda1c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dependencies, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[10].value.args[0].values[3].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[10].value.args[0].values[4]::Call

Source: `scripts/roadmap_python.py:152`; AST `b9d8abb1b57fe50b08618db4f50fe4fb961790a35b4b8b2d97e3f155328da441`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, classify_deal, observed, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[10].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[5].body[10].value.args[0].values[4].args[0]::Call

Source: `scripts/roadmap_python.py:152`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[5].body[10].value.args[0].values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[6]::Return

Source: `scripts/roadmap_python.py:153`; AST `bf188af11f010a4bb9396b575970d7a1b84baa65a27fa82641f46720407e5dcf`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, binding, file_binding, root, runs, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Return evaluation at root.body[24].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[6].value.values[4]::Call

Source: `scripts/roadmap_python.py:154`; AST `9541f4c9d8dff7d7ff3112bf1ab4deb4b2305a0241438b75b655ce54f3816385`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::qualify_deal::root.body[24].body[6].value.values[5]::Call

Source: `scripts/roadmap_python.py:155`; AST `5490821019984d7c4f8f46ec5cf3fa43c46111d139cff228c93af8e6fae119fb`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[6].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25]::FunctionDef

Source: `scripts/roadmap_python.py:159`; AST `bed630188283a1744195e6fad55e43e3dad60967fb8a4a0330563c9fd313902b`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, ROOT, __doc__, argparse, args, atomic_write_json, bool, compile_roadmaps, confined_path, details, exc, json, output, parser, print, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route, str, type. Outputs/bindings: args, details, output, parser.
Calls/effect boundaries: argparse.ArgumentParser, atomic_write_json, bool, compile_roadmaps, confined_path, details.get, details.update, json.dumps, output.parent.mkdir, parser.add_argument, parser.parse_args, print, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[25]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[0]::Assign

Source: `scripts/roadmap_python.py:160`; AST `c4ad6d457d8034b25dcc473a40ed9c6629dab3a54fd3b776e18da1d1367bd02c`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: parser.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[0].value::Call

Source: `scripts/roadmap_python.py:160`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[1]::Expr

Source: `scripts/roadmap_python.py:161`; AST `3e287a158070b26c2e31fd8ef530c434386e56f8f78ca643fa454882496d2a13`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[1].value::Call

Source: `scripts/roadmap_python.py:161`; AST `f66d69ec5c94764edaf6659017764a1726f66a2e42cf7916df59aeabb542e68d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[2]::Expr

Source: `scripts/roadmap_python.py:162`; AST `9da33d77a9d730d1b0a37192c8581046a68572dcd897195379ae8e318be418ad`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[2].value::Call

Source: `scripts/roadmap_python.py:162`; AST `fec4fbf48af0ce6f50e4b9bb90b76836907b3da18e1361a79d252cbbf372ac6f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[3]::Expr

Source: `scripts/roadmap_python.py:163`; AST `4dc5801b9512d0ab4f7d67781330b07dcfe712734bf0b719389f03a9217552b6`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[3].value::Call

Source: `scripts/roadmap_python.py:163`; AST `1ec65a7b2bb9c75b74e5e087b7144be3df10847cfcd4b35415c851ac404d3884`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[4]::Expr

Source: `scripts/roadmap_python.py:164`; AST `334d61d2a2921110e942f4b169bd41c606a6dcf8bf223999192ee16fcfa3f13d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[4].value::Call

Source: `scripts/roadmap_python.py:164`; AST `d50d0fb713f1431e5fd238d232cd28f2372ff3974d16a51737ddd35ebf72866b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[5]::Expr

Source: `scripts/roadmap_python.py:165`; AST `5dc3037bf8b79a57f092f7b592d3da2c5e19754b0ea1174afb23e01bbe2e8727`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[5].value::Call

Source: `scripts/roadmap_python.py:165`; AST `0093743eff5ed56ff5408b72767e2320decccba39058574af1c0a270f9f8cc58`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[6]::Assign

Source: `scripts/roadmap_python.py:166`; AST `6275c8d1600da776fb862cf3f5fef974e2559c70800565172097404dcea6fef6`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: args.
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[6].value::Call

Source: `scripts/roadmap_python.py:166`; AST `c865e8043798bf46a3b13d6774886772cbfabc2836b109a02aef4d3c2ad2a7ef`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[7]::Assign

Source: `scripts/roadmap_python.py:167`; AST `1c8d0649b621e001ff440b9c0f08a698a279ede4b45e9d820632f0857b61d38e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, confined_path. Outputs/bindings: output.
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[7].value::Call

Source: `scripts/roadmap_python.py:167`; AST `bd2c4103df935f33b6c3362a61ace084743aa0c8c3bc6058f572e1ed907f0aa0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[8]::Expr

Source: `scripts/roadmap_python.py:168`; AST `6af0c3e1e37a1b2c9b2db5132d01973127cd24470e65d3e6fe35c25bc4a76da1`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[8].value::Call

Source: `scripts/roadmap_python.py:168`; AST `d9f4729bd6e66ce526bcb76f0d13fb2682526e87f6f7b46bb656321930d9ccc7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[9]::Assign

Source: `scripts/roadmap_python.py:169`; AST `39634edd3c7ba1237a1afafca500bbb58118c20552bb325d9598839d8adb42ce`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args. Outputs/bindings: details.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[25].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10]::Try

Source: `scripts/roadmap_python.py:170`; AST `b9584f5b9ba44687d51084a30bfbe597b34c10fd2c16b7d172d90ae19fbd91f6`.

Rust module: `scripts::roadmap_python`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, ROOT, args, atomic_write_json, bool, compile_roadmaps, details, exc, output, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route, str, type. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, bool, compile_roadmaps, details.update, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Try evaluation at root.body[25].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0]::If

Source: `scripts/roadmap_python.py:171`; AST `eacfdb8dae137e592780ebc07d46519a5423a5fdd4d754731fc782f632ec94cb`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, bool, compile_roadmaps, details, output, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route. Outputs/bindings: (none).
Calls/effect boundaries: bool, compile_roadmaps, details.update, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[25].body[10].body[0]; no call, error or mutation may be omitted. Condition: args.action == 'route'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].body[0]::Expr

Source: `scripts/roadmap_python.py:172`; AST `ce7c36f5f5093f5b7ea1ad960bf5bf011e30fbdb474c9a9363121b5b3bf46132`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, compile_roadmaps, details, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, details.update, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].body[0].value::Call

Source: `scripts/roadmap_python.py:172`; AST `da59b9c4bbdd827cd9163ec13c8e08c42eb7d1a06f27fc7bc733e4a6a22d6536`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, compile_roadmaps, details, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, details.update, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].body[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:172`; AST `112f39238a3a26dc73094c89ccb8036b839b309f64ca2ca3ca696f88068e40e8`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, compile_roadmaps, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].body[0].value.args[0].args[1]::Call

Source: `scripts/roadmap_python.py:172`; AST `d1af4336e7af420cac99b4dd6cdf27c0ceea85cd6a7b14065da627f3fa88a4d7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compile_roadmaps. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0]::If

Source: `scripts/roadmap_python.py:173`; AST `23602eab3dcbbc551ceddd803367a0cff62ea160e10bfdcfb04ccf79e2a923ad`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, bool, details, output, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, details.update, provision, provision_deal, provision_esbmc, qualify, qualify_deal, qualify_esbmc, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[25].body[10].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: args.action == 'toolchain'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0]::If

Source: `scripts/roadmap_python.py:174`; AST `15173224edc5e1edb98052f37ffad140ca878ba0d2d677aca424b3c1d850c306`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, details, output, provision, provision_deal, provision_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision, provision_deal, provision_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[25].body[10].body[0].orelse[0].body[0]; no call, error or mutation may be omitted. Condition: args.backend == 'esbmc-python'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].body[0]::ImportFrom

Source: `scripts/roadmap_python.py:175`; AST `6207cdc881598bc33fe609621a25e3552446cae0e7720c9ac5348d683785676d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[25].body[10].body[0].orelse[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].body[1]::Expr

Source: `scripts/roadmap_python.py:176`; AST `9b356dc29851b1b3ad75a69ec625c24a5900459e50ca1b9bfff4c635a2995eb2`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, details, output, provision_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].orelse[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].body[1].value::Call

Source: `scripts/roadmap_python.py:176`; AST `c987678f05cb0697a86735c62987a5f6ed8ce948fd03fddb13ab781ade0f64b4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, details, output, provision_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].body[1].value.args[0]::Call

Source: `scripts/roadmap_python.py:176`; AST `cd5e604c882701697deba32e40d2196b23ab1f127f8fa518d4716bc019792b04`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, output, provision_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: provision_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].body[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].orelse[0]::Expr

Source: `scripts/roadmap_python.py:178`; AST `680e9027b15c384f5fc41633b9614d42e41e821bf9376fe4bac17fa73916a05f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, details, output, provision, provision_deal. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision, provision_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].orelse[0].body[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value::Call

Source: `scripts/roadmap_python.py:178`; AST `2bf371865962d5e027ef3ce2a7da5359de26602ade6086fb688a524d0f83e824`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, details, output, provision, provision_deal. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision, provision_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value.args[0].body::Call

Source: `scripts/roadmap_python.py:178`; AST `d94639f6493217e74bf80cdfa2a959eeb3f218fa4ca5c7093284cc667397e71b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, output, provision_deal. Outputs/bindings: (none).
Calls/effect boundaries: provision_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value.args[0].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value.args[0].orelse::Call

Source: `scripts/roadmap_python.py:178`; AST `09b3dfd74d54b6851cf97079981e7c8bb8d4845057644b7e6e243cbcb800af4c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, output, provision. Outputs/bindings: (none).
Calls/effect boundaries: provision.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].body[0].orelse[0].value.args[0].orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[0]::Expr

Source: `scripts/roadmap_python.py:180`; AST `c0b1de1c66ad89ca7f1f70d0b698ed66f4e64fbea18cd0e60e87e2207009735f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, bool, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[0].value::Call

Source: `scripts/roadmap_python.py:180`; AST `1b79322c8c38826bdf7e5dbcc641f3ee711c2b278192923d5f437e7cc8bb8cc4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, bool, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:180`; AST `fd5b4b44bde615f9fc60e6bd97ae64e8173f8e63fb481e5b52ea35a5d294897a`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, bool. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1]::If

Source: `scripts/roadmap_python.py:181`; AST `b5bc23753a217f428966a5a7c2b0d39984a866e4f84e126984c9db0f31f698d5`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, details, output, qualify, qualify_deal, qualify_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify, qualify_deal, qualify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1]; no call, error or mutation may be omitted. Condition: args.backend == 'esbmc-python'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].body[0]::ImportFrom

Source: `scripts/roadmap_python.py:182`; AST `247f37d36bbe27c02921b915730692701130ecb46bb5b46b4d7a191fc0615070`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].body[1]::Expr

Source: `scripts/roadmap_python.py:183`; AST `d85303d48ac0e6bc2e0ff51d97fb17e2cc54f0187d54813d9b8019f1ed51123b`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, details, output, qualify_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].body[1].value::Call

Source: `scripts/roadmap_python.py:183`; AST `f32a0af395cc3353e01d9c0c4fba9aa5485fece446e758e54829c4ac64ec5cce`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, details, output, qualify_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].body[1].value.args[0]::Call

Source: `scripts/roadmap_python.py:183`; AST `4ff976d5c442eeff4394ec5174c7192465a5f4e41359b563bd3e2fe2c88647e5`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, output, qualify_esbmc. Outputs/bindings: (none).
Calls/effect boundaries: qualify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0]::Expr

Source: `scripts/roadmap_python.py:185`; AST `e55c0b5284d95a7e3ccecf3e1f326eaf3f8acde6e3a63a837fcc33aca258041e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, details, output, qualify, qualify_deal. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify, qualify_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value::Call

Source: `scripts/roadmap_python.py:185`; AST `e2b091252750078d32db773cb19be0c311f97752f8cc1398786c527897f8c498`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, details, output, qualify, qualify_deal. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify, qualify_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value.args[0].body::Call

Source: `scripts/roadmap_python.py:185`; AST `9bff276eb84b0b28a4104177cd37c4973943cfc8e2da4c3e018119759c23e109`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, output, qualify_deal. Outputs/bindings: (none).
Calls/effect boundaries: qualify_deal.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value.args[0].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value.args[0].orelse::Call

Source: `scripts/roadmap_python.py:185`; AST `9493480b6d44dbcd3995fce5128ec6af3d336a1d5281e866e5172d6920055f44`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, output, qualify. Outputs/bindings: (none).
Calls/effect boundaries: qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].body[0].orelse[0].orelse[1].orelse[0].value.args[0].orelse; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0]::ExceptHandler

Source: `scripts/roadmap_python.py:186`; AST `be0e352e3eb5a6555cd8a4462cb28790a828f68813c1d94c7e9375175fcc67a2`.

Rust module: `scripts::roadmap_python`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, ROOT, atomic_write_json, details, exc, output, str, type. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[25].body[10].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[0]::Expr

Source: `scripts/roadmap_python.py:187`; AST `abeed5042a73141808d86ad9c758a4deb65df21e35308b4f121f6f848e00979f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: details, exc, str, type. Outputs/bindings: (none).
Calls/effect boundaries: details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[0].value::Call

Source: `scripts/roadmap_python.py:187`; AST `7aa41abb1d2ef7061383da1ef31927f8ef7b9fe56f8de7461eb92953d27ab474`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details, exc, str, type. Outputs/bindings: (none).
Calls/effect boundaries: details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[0].value.keywords[1].value.values[0].value::Call

Source: `scripts/roadmap_python.py:187`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].handlers[0].body[0].value.keywords[1].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[0].value.keywords[1].value.values[1]::Call

Source: `scripts/roadmap_python.py:187`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].handlers[0].body[0].value.keywords[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[1]::Expr

Source: `scripts/roadmap_python.py:188`; AST `6827e0538d8a875ec70f86a195629043358a77d80a9ad92988899f3a044623a9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[10].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[1].value::Call

Source: `scripts/roadmap_python.py:188`; AST `60bb52616de20a8c1388546ef8f467481955ceced2d321546afa06ee8106c189`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[10].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[10].handlers[0].body[2]::Raise

Source: `scripts/roadmap_python.py:189`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Raise evaluation at root.body[25].body[10].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[11]::Expr

Source: `scripts/roadmap_python.py:190`; AST `6827e0538d8a875ec70f86a195629043358a77d80a9ad92988899f3a044623a9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[11].value::Call

Source: `scripts/roadmap_python.py:190`; AST `60bb52616de20a8c1388546ef8f467481955ceced2d321546afa06ee8106c189`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[12]::Expr

Source: `scripts/roadmap_python.py:191`; AST `7e5045f4dd975b10c3b4cf83aafd6c94dac43df4c4bea2d3562833171c07f130`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, details, json, print. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps, print.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[25].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[12].value::Call

Source: `scripts/roadmap_python.py:191`; AST `9baa38ad91607bc2d039cb848ddc7837d1bb1d352b50c1e675262f311c081040`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, details, json, print. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps, print.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[12].value.args[0]::Call

Source: `scripts/roadmap_python.py:191`; AST `7954c862fdca8377761218c9b25cae511aa0de78f299f3b3d752f49ae76540cc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, details, json. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[12].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[25].body[12].value.args[0].args[0].values[1]::Call

Source: `scripts/roadmap_python.py:191`; AST `f63476f469df30469ab052e394bf48bef4cca66f10e12ebb537b6d3ab4725243`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[25].body[12].value.args[0].args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[26]::If

Source: `scripts/roadmap_python.py:194`; AST `3340fd16ba41ba1ddf3989cd136a498b72a97f7796e0f7fad6e815585dbc1c52`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[26]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[26].body[0]::Expr

Source: `scripts/roadmap_python.py:195`; AST `26412f54b9dfeb741e0d31e60ab8bd5c087bc77b2e3192f46a2fa84cd9152b86`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[26].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[26].body[0].value::Call

Source: `scripts/roadmap_python.py:195`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, roadmap_esbmc, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[26].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
