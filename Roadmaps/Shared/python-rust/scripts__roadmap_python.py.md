# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 222. Inventory digest: `0cf9e62b03d46f249e86936e74082082d824becfdeb4be704efb6bf3367d86c9`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_python.py::module::root::Module

Source: `scripts/roadmap_python.py:1`; AST `c79b6c06f2382ae2f2e1269d16e625970a291395c8a738f4ec022d2e3d98ac73`.

Rust module: `scripts::roadmap_python`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Exception, Path, ROOT, TRANSPORT, __doc__, __file__, __name__, _download, archive, argparse, args, asdict, atomic_write_json, b, bindings_current, bool, bundle, checked, classify_nagini, compile_roadmaps, confined_path, deadline, details, dict, digest, directory, download_with_mirrors, entry, environment, exc, file_binding, files, float, installed, java, java_root, java_version, json, len, list, lock, main, map, minimal_subprocess_env, nagini, name, os, outcomes, output, p, package, parser, path, print, provision, python, qualify, r, read_download_policy, read_json, require, result, root, route, run_recipe_stage, runs, sorted, source, source_closure, str, sys, tarfile, time, toolchain, toolchain_path, type, venv, virtual, wheels. Outputs/bindings: ROOT, archive, args, bundle, checked, deadline, details, directory, environment, files, installed, java, java_root, java_version, lock, nagini, name, outcomes, output, p, package, parser, path, python, r, result, runs, source, toolchain, virtual, wheels.
Calls/effect boundaries: (virtual / 'bin/python').exists, Path, Path(__file__).resolve, _download, argparse.ArgumentParser, asdict, atomic_write_json, bindings_current, bool, bundle.extractall, classify_nagini, compile_roadmaps, confined_path, details.get, details.update, dict, digest, directory.mkdir, directory.rglob, download_with_mirrors, environment.get, file_binding, java_root.exists, java_root.glob, java_root.mkdir, json.dumps, len, list, lock.get, main, map, minimal_subprocess_env, nagini.is_file, os.uname, output.parent.mkdir, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, parser.add_argument, parser.parse_args, path.relative_to, path.relative_to(root).as_posix, print, provision, qualify, read_download_policy, read_json, require, route, run_recipe_stage, runs.append, sorted, source.relative_to, source.relative_to(root).as_posix, source_closure, str, sys.path.insert, tarfile.open, time.monotonic, toolchain.get, type, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[17]::ImportFrom

Source: `scripts/roadmap_python.py:21`; AST `25afd1dbfce98be3d5b7acbd39e170d0d6e0991f86b8cf497cc55ad2774dfacd`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

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
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered ListComp evaluation at root.body[22].body[6].value.values[6].right; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23]::FunctionDef

Source: `scripts/roadmap_python.py:99`; AST `0b6b80e7ff6e76768fef00483ee0b001914df764faf8afe2ace8efbcdb5aa78d`.

Rust module: `scripts::roadmap_python`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, ROOT, __doc__, argparse, args, atomic_write_json, bool, compile_roadmaps, confined_path, details, exc, json, output, parser, print, provision, qualify, require, route, str, type. Outputs/bindings: args, details, output, parser.
Calls/effect boundaries: argparse.ArgumentParser, atomic_write_json, bool, compile_roadmaps, confined_path, details.get, details.update, json.dumps, output.parent.mkdir, parser.add_argument, parser.parse_args, print, provision, qualify, require, route, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered FunctionDef evaluation at root.body[23]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[0]::Assign

Source: `scripts/roadmap_python.py:100`; AST `c4ad6d457d8034b25dcc473a40ed9c6629dab3a54fd3b776e18da1d1367bd02c`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: __doc__, argparse. Outputs/bindings: parser.
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[0].value::Call

Source: `scripts/roadmap_python.py:100`; AST `d39f39ff7d74d107a287f654b8e1af65d84cce415404e0fd0bba007cadaa9678`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: __doc__, argparse. Outputs/bindings: (none).
Calls/effect boundaries: argparse.ArgumentParser.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[1]::Expr

Source: `scripts/roadmap_python.py:101`; AST `3e287a158070b26c2e31fd8ef530c434386e56f8f78ca643fa454882496d2a13`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[1].value::Call

Source: `scripts/roadmap_python.py:101`; AST `f66d69ec5c94764edaf6659017764a1726f66a2e42cf7916df59aeabb542e68d`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[2]::Expr

Source: `scripts/roadmap_python.py:102`; AST `9da33d77a9d730d1b0a37192c8581046a68572dcd897195379ae8e318be418ad`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[2].value::Call

Source: `scripts/roadmap_python.py:102`; AST `fec4fbf48af0ce6f50e4b9bb90b76836907b3da18e1361a79d252cbbf372ac6f`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[3]::Expr

Source: `scripts/roadmap_python.py:103`; AST `4dc5801b9512d0ab4f7d67781330b07dcfe712734bf0b719389f03a9217552b6`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[3].value::Call

Source: `scripts/roadmap_python.py:103`; AST `1ec65a7b2bb9c75b74e5e087b7144be3df10847cfcd4b35415c851ac404d3884`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[4]::Expr

Source: `scripts/roadmap_python.py:104`; AST `334d61d2a2921110e942f4b169bd41c606a6dcf8bf223999192ee16fcfa3f13d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[4].value::Call

Source: `scripts/roadmap_python.py:104`; AST `d50d0fb713f1431e5fd238d232cd28f2372ff3974d16a51737ddd35ebf72866b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.add_argument.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[5]::Assign

Source: `scripts/roadmap_python.py:105`; AST `6275c8d1600da776fb862cf3f5fef974e2559c70800565172097404dcea6fef6`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parser. Outputs/bindings: args.
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[5].value::Call

Source: `scripts/roadmap_python.py:105`; AST `c865e8043798bf46a3b13d6774886772cbfabc2836b109a02aef4d3c2ad2a7ef`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parser. Outputs/bindings: (none).
Calls/effect boundaries: parser.parse_args.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[6]::Assign

Source: `scripts/roadmap_python.py:106`; AST `1c8d0649b621e001ff440b9c0f08a698a279ede4b45e9d820632f0857b61d38e`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, confined_path. Outputs/bindings: output.
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[6].value::Call

Source: `scripts/roadmap_python.py:106`; AST `bd2c4103df935f33b6c3362a61ace084743aa0c8c3bc6058f572e1ed907f0aa0`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, confined_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[7]::Expr

Source: `scripts/roadmap_python.py:107`; AST `6af0c3e1e37a1b2c9b2db5132d01973127cd24470e65d3e6fe35c25bc4a76da1`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[7].value::Call

Source: `scripts/roadmap_python.py:107`; AST `d9f4729bd6e66ce526bcb76f0d13fb2682526e87f6f7b46bb656321930d9ccc7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output. Outputs/bindings: (none).
Calls/effect boundaries: output.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[8]::Assign

Source: `scripts/roadmap_python.py:108`; AST `39634edd3c7ba1237a1afafca500bbb58118c20552bb325d9598839d8adb42ce`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args. Outputs/bindings: details.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Assign evaluation at root.body[23].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9]::Try

Source: `scripts/roadmap_python.py:109`; AST `c036ffd9f110f3f5507fa20f21f68fb691ceebe2cb9b88574759acd868f47410`.

Rust module: `scripts::roadmap_python`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, ROOT, args, atomic_write_json, bool, compile_roadmaps, details, exc, output, provision, qualify, require, route, str, type. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, bool, compile_roadmaps, details.update, provision, qualify, require, route, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Try evaluation at root.body[23].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0]::If

Source: `scripts/roadmap_python.py:110`; AST `66b4043d3972858bb61529321cf26f6bd6a9bf468929bc7b6fbc3ce690a94278`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, bool, compile_roadmaps, details, output, provision, qualify, require, route. Outputs/bindings: (none).
Calls/effect boundaries: bool, compile_roadmaps, details.update, provision, qualify, require, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[23].body[9].body[0]; no call, error or mutation may be omitted. Condition: args.action == 'route'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].body[0]::Expr

Source: `scripts/roadmap_python.py:111`; AST `ce7c36f5f5093f5b7ea1ad960bf5bf011e30fbdb474c9a9363121b5b3bf46132`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, compile_roadmaps, details, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, details.update, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].body[0].value::Call

Source: `scripts/roadmap_python.py:111`; AST `da59b9c4bbdd827cd9163ec13c8e08c42eb7d1a06f27fc7bc733e4a6a22d6536`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, compile_roadmaps, details, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, details.update, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].body[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:111`; AST `112f39238a3a26dc73094c89ccb8036b839b309f64ca2ca3ca696f88068e40e8`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, compile_roadmaps, route. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps, route.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].body[0].value.args[0].args[1]::Call

Source: `scripts/roadmap_python.py:111`; AST `d1af4336e7af420cac99b4dd6cdf27c0ceea85cd6a7b14065da627f3fa88a4d7`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, compile_roadmaps. Outputs/bindings: (none).
Calls/effect boundaries: compile_roadmaps.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].body[0].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0]::If

Source: `scripts/roadmap_python.py:112`; AST `12b14c070b37d2dd658b9d2bd396e8bcbf7428cc9450c3f23bc34a991ca3fd29`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ROOT, args, bool, details, output, provision, qualify, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, details.update, provision, qualify, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[23].body[9].body[0].orelse[0]; no call, error or mutation may be omitted. Condition: args.action == 'toolchain'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].body[0]::Expr

Source: `scripts/roadmap_python.py:113`; AST `f975bfafb821ef9723ad90741556f0e8268dd7890172d1c8ddd139d13a57b65f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, details, output, provision. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].body[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].body[0].value::Call

Source: `scripts/roadmap_python.py:113`; AST `c45df3fea944eb5622169e3e5c4f8812420a1275146869e2df10388bc3fc20fe`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, details, output, provision. Outputs/bindings: (none).
Calls/effect boundaries: details.update, provision.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].body[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:113`; AST `09b3dfd74d54b6851cf97079981e7c8bb8d4845057644b7e6e243cbcb800af4c`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, output, provision. Outputs/bindings: (none).
Calls/effect boundaries: provision.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[0]::Expr

Source: `scripts/roadmap_python.py:115`; AST `c0b1de1c66ad89ca7f1f70d0b698ed66f4e64fbea18cd0e60e87e2207009735f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, bool, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].body[0].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[0].value::Call

Source: `scripts/roadmap_python.py:115`; AST `1b79322c8c38826bdf7e5dbcc641f3ee711c2b278192923d5f437e7cc8bb8cc4`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, bool, require. Outputs/bindings: (none).
Calls/effect boundaries: bool, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[0].value.args[0]::Call

Source: `scripts/roadmap_python.py:115`; AST `fd5b4b44bde615f9fc60e6bd97ae64e8173f8e63fb481e5b52ea35a5d294897a`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, bool. Outputs/bindings: (none).
Calls/effect boundaries: bool.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].orelse[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[1]::Expr

Source: `scripts/roadmap_python.py:116`; AST `58872224455137e98f58ae7c0cbcff009279fb489cbd1a763b8918cd225834d4`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, details, output, qualify. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].body[0].orelse[0].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[1].value::Call

Source: `scripts/roadmap_python.py:116`; AST `371b2425a7112ae402f3fde6b1332781253e534eede3f653afe0a13724b3ec6b`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, details, output, qualify. Outputs/bindings: (none).
Calls/effect boundaries: details.update, qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].body[0].orelse[0].orelse[1].value.args[0]::Call

Source: `scripts/roadmap_python.py:116`; AST `9493480b6d44dbcd3995fce5128ec6af3d336a1d5281e866e5172d6920055f44`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, output, qualify. Outputs/bindings: (none).
Calls/effect boundaries: qualify.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].body[0].orelse[0].orelse[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0]::ExceptHandler

Source: `scripts/roadmap_python.py:117`; AST `be0e352e3eb5a6555cd8a4462cb28790a828f68813c1d94c7e9375175fcc67a2`.

Rust module: `scripts::roadmap_python`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, ROOT, atomic_write_json, details, exc, output, str, type. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[23].body[9].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[0]::Expr

Source: `scripts/roadmap_python.py:118`; AST `abeed5042a73141808d86ad9c758a4deb65df21e35308b4f121f6f848e00979f`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: details, exc, str, type. Outputs/bindings: (none).
Calls/effect boundaries: details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[0].value::Call

Source: `scripts/roadmap_python.py:118`; AST `7aa41abb1d2ef7061383da1ef31927f8ef7b9fe56f8de7461eb92953d27ab474`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details, exc, str, type. Outputs/bindings: (none).
Calls/effect boundaries: details.update, str, type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[0].value.keywords[1].value.values[0].value::Call

Source: `scripts/roadmap_python.py:118`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].handlers[0].body[0].value.keywords[1].value.values[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[0].value.keywords[1].value.values[1]::Call

Source: `scripts/roadmap_python.py:118`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].handlers[0].body[0].value.keywords[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[1]::Expr

Source: `scripts/roadmap_python.py:119`; AST `6827e0538d8a875ec70f86a195629043358a77d80a9ad92988899f3a044623a9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[9].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[1].value::Call

Source: `scripts/roadmap_python.py:119`; AST `60bb52616de20a8c1388546ef8f467481955ceced2d321546afa06ee8106c189`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[9].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[9].handlers[0].body[2]::Raise

Source: `scripts/roadmap_python.py:120`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Raise evaluation at root.body[23].body[9].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[10]::Expr

Source: `scripts/roadmap_python.py:121`; AST `6827e0538d8a875ec70f86a195629043358a77d80a9ad92988899f3a044623a9`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[10].value::Call

Source: `scripts/roadmap_python.py:121`; AST `60bb52616de20a8c1388546ef8f467481955ceced2d321546afa06ee8106c189`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, atomic_write_json, details, output. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[11]::Expr

Source: `scripts/roadmap_python.py:122`; AST `7e5045f4dd975b10c3b4cf83aafd6c94dac43df4c4bea2d3562833171c07f130`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, details, json, print. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps, print.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[23].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[11].value::Call

Source: `scripts/roadmap_python.py:122`; AST `9baa38ad91607bc2d039cb848ddc7837d1bb1d352b50c1e675262f311c081040`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, details, json, print. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps, print.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[11].value.args[0]::Call

Source: `scripts/roadmap_python.py:122`; AST `7954c862fdca8377761218c9b25cae511aa0de78f299f3b3d752f49ae76540cc`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, details, json. Outputs/bindings: (none).
Calls/effect boundaries: details.get, json.dumps.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::main::root.body[23].body[11].value.args[0].args[0].values[1]::Call

Source: `scripts/roadmap_python.py:122`; AST `f63476f469df30469ab052e394bf48bef4cca66f10e12ebb537b6d3ab4725243`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: details. Outputs/bindings: (none).
Calls/effect boundaries: details.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[23].body[11].value.args[0].args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[24]::If

Source: `scripts/roadmap_python.py:125`; AST `3340fd16ba41ba1ddf3989cd136a498b72a97f7796e0f7fad6e815585dbc1c52`.

Rust module: `scripts::roadmap_python`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered If evaluation at root.body[24]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[24].body[0]::Expr

Source: `scripts/roadmap_python.py:126`; AST `26412f54b9dfeb741e0d31e60ab8bd5c087bc77b2e3192f46a2fa84cd9152b86`.

Rust module: `scripts::roadmap_python`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Expr evaluation at root.body[24].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_python.py::module::root.body[24].body[0].value::Call

Source: `scripts/roadmap_python.py:126`; AST `612de6187c097f49a7c6002bfa6b205845dac081e9c3dc6b160fd9a6f584c826`.

Rust module: `scripts::roadmap_python`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: main. Outputs/bindings: (none).
Calls/effect boundaries: main.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, argparse, dataclasses, json, os, pathlib, sys, tarfile, time, venv.

Invariants: Preserve ordered Call evaluation at root.body[24].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
