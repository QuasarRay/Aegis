# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 141. Inventory digest: `63d9b4ce678f83477859a5a2a6594f2f075d7513ff6c173c52897d613717dab1`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/check_formal.py::module::root::Module

Source: `scripts/check_formal.py:1`; AST `0aaed7da6b1dd3ab8053286b6cf7dd4f618c3902c158b2707bb248764f9ecc19`.

Rust module: `scripts::check_formal`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ArgumentParser, FileLock, KeyError, OSError, Path, ROOT, RuntimeError, SystemExit, TypeError, ValueError, __doc__, __file__, __name__, all, args, argv, asdict, atomic_write_json, before, checked_output, confined_path, digest, env, exc, found, identity, json, k, key, load_json, load_profile, lock, matches_version, min, os, outputs, p, passed, pin, pin_path, print, receipt, record, remaining, require, reserve_attempt, result, run_process, sha256_file, shutil, sorted, source, started, str, sys, time, tools, verify, version, verus. Outputs/bindings: ROOT, args, argv, before, env, found, k, key, lock, outputs, p, passed, pin, pin_path, receipt, record, remaining, result, source, started, tools, version, verus.
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, ArgumentParser, FileLock, Path, Path(__file__).resolve, Path(found).resolve, SystemExit, all, asdict, atomic_write_json, checked_output, confined_path, digest, env.update, identity, json.dumps, load_json, load_profile, lock.acquire, lock.release, matches_version, min, outputs.append, p.add_argument, p.is_file, p.parse_args, pin_path.read_text, print, require, reserve_attempt, run_process, sha256_file, shutil.which, sorted, str, sys.path.insert, time.monotonic, tools.extend, verify, verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[0]::Expr

Source: `scripts/check_formal.py:1`; AST `433130000ff54bc58fe0d13d7cb1e33c590234a3f3cd815e155303b045667c7e`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[1]::ImportFrom

Source: `scripts/check_formal.py:2`; AST `d227b402e85018c648ff579fbce5a77882972f044ab3b7b9e923ba9580f3194d`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[2]::ImportFrom

Source: `scripts/check_formal.py:3`; AST `400d7764c2a2b8cabf9a4dc4cd172f3f6e19abcbe53e771b676ad31a327775fa`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[3]::ImportFrom

Source: `scripts/check_formal.py:4`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[4]::Import

Source: `scripts/check_formal.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[5]::Import

Source: `scripts/check_formal.py:6`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[6]::Import

Source: `scripts/check_formal.py:7`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[7]::Import

Source: `scripts/check_formal.py:8`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[8]::Import

Source: `scripts/check_formal.py:9`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[9]::Assign

Source: `scripts/check_formal.py:11`; AST `7efba0850e8eeaef93e5c3de6b7d47927a3e4bde0e8161dfb3d03fc10717d3c2`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, __file__. Outputs/bindings: ROOT.
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[9].value.value.value::Call

Source: `scripts/check_formal.py:11`; AST `d44e7d02687cdbf8fc79685a0d804e563813f4a84f2eb0ac60318cd0b1739a48`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(__file__).resolve.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[9].value.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[9].value.value.value.func.value::Call

Source: `scripts/check_formal.py:11`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[9].value.value.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[10]::Expr

Source: `scripts/check_formal.py:12`; AST `7c52d21c478e96a76000665e41a3690a48a529a401dfef50034ba26b4b4ab7b9`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[10].value::Call

Source: `scripts/check_formal.py:12`; AST `6c37d3755a0c3539e837482dba47597de98fd50aa6057e6df2fdc189353ef33e`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str, sys. Outputs/bindings: (none).
Calls/effect boundaries: str, sys.path.insert.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[10].value.args[1]::Call

Source: `scripts/check_formal.py:12`; AST `c1d796c6a1c077f98792dc2423ba6f7cc673f43b503388376d2d5522f04a67f3`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[10].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[11]::ImportFrom

Source: `scripts/check_formal.py:13`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[12]::ImportFrom

Source: `scripts/check_formal.py:14`; AST `c6d45c71cc6d729985b9e992a37af3b80b02553007dfb7f115c76e72d64711b7`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[13]::ImportFrom

Source: `scripts/check_formal.py:15`; AST `663d3b0bb00a8e13b98181e80fb8049d42c972c9c0890632f0fdc7a1d9473ac0`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[14]::ImportFrom

Source: `scripts/check_formal.py:16`; AST `20b875c04a5bc467b4634a4ab8c796f858cc4737c0f733bcb0cd515d85ffcf6a`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[15]::ImportFrom

Source: `scripts/check_formal.py:17`; AST `a19e166d00b3c1a61d7380c876517d3c1ed89a4f59fc21e765e78f1c68e4e8e9`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[16]::ImportFrom

Source: `scripts/check_formal.py:18`; AST `255dfec4d6ff7dfa92dc78e143e11e331797115bca3317171a233bfe87c5edad`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[17]::ImportFrom

Source: `scripts/check_formal.py:19`; AST `860451982277a7f5c435b7fc36a0eb328ab43d13fe8858ce9091906ca6dcc079`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ImportFrom evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18]::FunctionDef

Source: `scripts/check_formal.py:22`; AST `0f0fec79b043335278e4d4fffd71f98fe20a8c8408d5ab43a0d177ae0bf6d375`.

Rust module: `scripts::check_formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileLock, Path, ROOT, __file__, all, args, argv, asdict, atomic_write_json, before, checked_output, confined_path, digest, env, found, identity, k, key, load_json, load_profile, lock, matches_version, min, os, outputs, p, passed, pin, pin_path, receipt, record, remaining, require, reserve_attempt, result, run_process, sha256_file, shutil, sorted, source, started, str, time, tools, version, verus. Outputs/bindings: argv, before, env, found, k, key, lock, outputs, p, passed, pin, pin_path, receipt, record, remaining, result, source, started, tools, version, verus.
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, FileLock, Path, Path(found).resolve, all, asdict, atomic_write_json, checked_output, confined_path, digest, env.update, identity, load_json, load_profile, lock.acquire, lock.release, matches_version, min, outputs.append, p.is_file, pin_path.read_text, require, reserve_attempt, run_process, sha256_file, shutil.which, sorted, str, time.monotonic, tools.extend, verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[0]::Assign

Source: `scripts/check_formal.py:23`; AST `17e01661a5a4993bd1f4630a656942b010d4d759061b7d6ae8ceab129d550f6a`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT. Outputs/bindings: pin_path.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[1]::Assign

Source: `scripts/check_formal.py:24`; AST `dc2e029a3603db4fc34a82e2b0cc7088b1ee16e23eb51d12b9dfe9033ba4a160`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: load_json, pin_path. Outputs/bindings: pin.
Calls/effect boundaries: load_json, pin_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[1].value::Call

Source: `scripts/check_formal.py:24`; AST `829461ba2d62959d6bbf8a7dfe73a7961362d05e09ad5a1fdedfe3f30f55ff68`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_json, pin_path. Outputs/bindings: (none).
Calls/effect boundaries: load_json, pin_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[1].value.args[0]::Call

Source: `scripts/check_formal.py:24`; AST `8a3df5713c5def215243ffecf4766096076a159b28d7882b43005715afc3378a`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pin_path. Outputs/bindings: (none).
Calls/effect boundaries: pin_path.read_text.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[2]::Assign

Source: `scripts/check_formal.py:25`; AST `07ce84b1989573ed8bf9173795ac19f57b85934c03805d13c45891421fb7e358`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, shutil. Outputs/bindings: found.
Calls/effect boundaries: shutil.which.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[2].value::Call

Source: `scripts/check_formal.py:25`; AST `83c51b5a4118b7605e44cbc0c1b8a04e866f6bc1d5ff1a05757840202d1014f7`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, shutil. Outputs/bindings: (none).
Calls/effect boundaries: shutil.which.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[3]::Expr

Source: `scripts/check_formal.py:26`; AST `948c3738d7992c77067564df1c3563e364dc3f83ae3312ed1d7e793483969555`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: found, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[3].value::Call

Source: `scripts/check_formal.py:26`; AST `95be05dd63ec1038bbb5c109deb7b752d1231901fc49691a2f8595a8b0e95097`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: found, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[4]::Assign

Source: `scripts/check_formal.py:27`; AST `2a382ed98d7477555ff359ac5f5456c9424c56609ba4cdc9398f18cd99478e83`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, found. Outputs/bindings: verus.
Calls/effect boundaries: Path, Path(found).resolve.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[4].value::Call

Source: `scripts/check_formal.py:27`; AST `ca017b298addcf7e50a3512ca83bdf579121890296f154a487a592efbd1e6a1c`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, found. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(found).resolve.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[4].value.func.value::Call

Source: `scripts/check_formal.py:27`; AST `f03cc7b199beed0541fac9f98a29da24930ed83bae0fb78795c889227f84cb4d`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, found. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[5]::Assign

Source: `scripts/check_formal.py:28`; AST `068bdc70ba4be2ec795bd9236fbd1a90ad6007ee9aff867f4700b95c13b57948`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, confined_path, pin. Outputs/bindings: source.
Calls/effect boundaries: confined_path.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[5].value::Call

Source: `scripts/check_formal.py:28`; AST `86dd3e015b78a0c8236eb20a63e92bcdcee4be07987b6727b9c2c34849e71a97`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, confined_path, pin. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[6]::Assign

Source: `scripts/check_formal.py:29`; AST `aa168caf0fc30d166067095b90b9e980cf052fa20fc249d5b6f2f1a33138d0f5`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: verus. Outputs/bindings: tools.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[7]::Expr

Source: `scripts/check_formal.py:32`; AST `ceb3940a701dceac109f76b561363f0c5741fd6c4ea06890b7e3b48b57ed1b0d`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: sorted, tools, verus. Outputs/bindings: (none).
Calls/effect boundaries: sorted, tools.extend, verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[7].value::Call

Source: `scripts/check_formal.py:32`; AST `c87faeebd9746580bc8683ab9ee0125080042a41341c2d2b514e40ffaf1255e2`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sorted, tools, verus. Outputs/bindings: (none).
Calls/effect boundaries: sorted, tools.extend, verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[7].value.args[0]::Call

Source: `scripts/check_formal.py:32`; AST `f50a1195953e76df444b98d0b1973a6a7b9faea2786477d10c9ed96baf4f2fcb`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sorted, verus. Outputs/bindings: (none).
Calls/effect boundaries: sorted, verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[7].value.args[0].args[0]::Call

Source: `scripts/check_formal.py:32`; AST `68240fd2ce66c44fb4eef4bd04ac45807c2bf5d5954eacc3cd954296ec6742e7`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: verus. Outputs/bindings: (none).
Calls/effect boundaries: verus.parent.glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[8]::Expr

Source: `scripts/check_formal.py:33`; AST `7799201abaec83b2e479e7003e2045992fc52cffd3bd88df1a900f09196209a5`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, p, require, tools. Outputs/bindings: p.
Calls/effect boundaries: all, p.is_file, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[8].value::Call

Source: `scripts/check_formal.py:33`; AST `9697b1214a0e3f70c5eb1b3917d4ce8cfd1188b5bd8bf1db42ebfee3fa78ea96`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, p, require, tools. Outputs/bindings: p.
Calls/effect boundaries: all, p.is_file, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[8].value.args[0]::Call

Source: `scripts/check_formal.py:33`; AST `d36a94a8007850351a6b4b54dd0c156c91c10b246bc6fb312fef938441d7cf03`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, p, tools. Outputs/bindings: p.
Calls/effect boundaries: all, p.is_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[8].value.args[0].args[0]::GeneratorExp

Source: `scripts/check_formal.py:33`; AST `314cadae0b17b36adf464e910e983e77a970a4e6af72903eb96189cb0350112a`.

Rust module: `scripts::check_formal`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: p, tools. Outputs/bindings: p.
Calls/effect boundaries: p.is_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[18].body[8].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[8].value.args[0].args[0].elt::Call

Source: `scripts/check_formal.py:33`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[8].value.args[0].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9]::FunctionDef

Source: `scripts/check_formal.py:35`; AST `281be51a328bda6c4d81687ebad66cf14bb3112d647fef60c45711cdb7a67834`.

Rust module: `scripts::check_formal`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, ROOT, __file__, p, pin_path, sha256_file, sorted, source, str, tools. Outputs/bindings: p.
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, Path, sha256_file, sorted, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0]::Return

Source: `scripts/check_formal.py:36`; AST `ff73b0d1172401f01b6af8c6d8c2afdcf46af62ceadd835eadadc0c2ecbcce43`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, ROOT, __file__, p, pin_path, sha256_file, sorted, source, str, tools. Outputs/bindings: p.
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, Path, sha256_file, sorted, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[18].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[0]::Call

Source: `scripts/check_formal.py:36`; AST `7c3bc417991c21c12653dd6c537b5116c5c21119aee629946070ba38aa54e260`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sha256_file, source. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[1]::Call

Source: `scripts/check_formal.py:36`; AST `d0cb4f53ca17c451a9257576856d43be37a00e4d6238cdae024325c80c16482f`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pin_path, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[2]::Call

Source: `scripts/check_formal.py:37`; AST `e7f7b3b81070b387fca78f0205671d8a7d0bcfdd0845653e1f8cbcd5ee48a828`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: Path, sha256_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[2].args[0]::Call

Source: `scripts/check_formal.py:37`; AST `9f5e243206e67f121178ef2a1c915d192fa009a9d045e76d252ae2843b3aa69c`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, __file__. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[2].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[3]::DictComp

Source: `scripts/check_formal.py:38`; AST `3322fa579c9a8314b33f4b7e47eff53f7d1a7660d5a46c2f82af3bf7124841e4`.

Rust module: `scripts::check_formal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: p, sha256_file, str, tools. Outputs/bindings: p.
Calls/effect boundaries: sha256_file, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[9].body[0].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[3].key::Call

Source: `scripts/check_formal.py:38`; AST `8d6f3ff4500eed900ba221924fbd81d7b5a940c4b4541d30d4dc12d4da789c5e`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[3].key; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[3].value::Call

Source: `scripts/check_formal.py:38`; AST `10ff965a98abd23dad94b70fab85cccd23b07ff31fab5f20e7d34b872a90d58a`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[4]::DictComp

Source: `scripts/check_formal.py:39`; AST `809d88057f4ddcc066945566cc49f49465b7185b1348cd50c1ef1b8febec4d0b`.

Rust module: `scripts::check_formal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: ROOT, p, sha256_file, sorted. Outputs/bindings: p.
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, sha256_file, sorted.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[9].body[0].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[4].value::Call

Source: `scripts/check_formal.py:39`; AST `10ff965a98abd23dad94b70fab85cccd23b07ff31fab5f20e7d34b872a90d58a`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, sha256_file. Outputs/bindings: (none).
Calls/effect boundaries: sha256_file.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[4].generators[0].iter::Call

Source: `scripts/check_formal.py:39`; AST `31ada70a93abfab09ea79b182805110c7d85819f14d1943f0b0a27f62d6e03a0`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, sorted. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob, sorted.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[4].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::identity::root.body[18].body[9].body[0].value.values[4].generators[0].iter.args[0]::Call

Source: `scripts/check_formal.py:39`; AST `3faba11b113745b2929e0ff819a60f6c8ee03c0cfd0ed3676292a4a44d5d2937`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT. Outputs/bindings: (none).
Calls/effect boundaries: (ROOT / 'infra/agentinfra').glob.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].body[0].value.values[4].generators[0].iter.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[10]::Assign

Source: `scripts/check_formal.py:41`; AST `1cc82008c69bbaae6ce1bf4ddbf988068a99864ef2aa92e3bc8b7b9e98f96bc7`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: k, os. Outputs/bindings: env, k.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[10].value::DictComp

Source: `scripts/check_formal.py:41`; AST `7bfb0f8c030731f9fab0172263699ef095ff8dc73b8cd73f65c5117359903965`.

Rust module: `scripts::check_formal`. ordered evaluation into an insertion-ordered map; preserve duplicate-key replacement

Inputs: k, os. Outputs/bindings: k.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered DictComp evaluation at root.body[18].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[11]::Expr

Source: `scripts/check_formal.py:42`; AST `3f427aeee5e1141fc7fe6cdf257437f4770da539e2b520253a195e0ed4686e72`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: env, str, verus. Outputs/bindings: (none).
Calls/effect boundaries: env.update, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[11].value::Call

Source: `scripts/check_formal.py:42`; AST `a81fe5d1691990a5e0592bbc37208151ddfcc7452dc9b88e9f91503b545b5d9e`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: env, str, verus. Outputs/bindings: (none).
Calls/effect boundaries: env.update, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[11].value.args[0].values[3]::Call

Source: `scripts/check_formal.py:43`; AST `c32051f392cc416cd7d5e30f2e10b8b914b6815e0a4712825361ef8a5a2c1914`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, verus. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[12]::Assign

Source: `scripts/check_formal.py:44`; AST `ce7eb78526fa75a3f6564d4a7a4c68cd4ce11e82b633b292bae2afde46f4dc42`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: FileLock, ROOT. Outputs/bindings: lock.
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[12].value::Call

Source: `scripts/check_formal.py:44`; AST `592c809cf898f631967a8ed0e23e7cb2836be2516e21ab2cd430b44bc92aee33`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileLock, ROOT. Outputs/bindings: (none).
Calls/effect boundaries: FileLock.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[13]::Expr

Source: `scripts/check_formal.py:45`; AST `428763d06f915001746cebdf7dd12cafef877a86e9b481dec8ac0e4b0c995c09`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[13].value::Call

Source: `scripts/check_formal.py:45`; AST `7b464e5c1137f26af8593e9de31970baaae7cd7f638e99176de038b1af8b46a2`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.acquire.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14]::Try

Source: `scripts/check_formal.py:46`; AST `63e79a2372ececf07e048fcdc3d27f2f4de907280721ee93d662f2216caeb133`.

Rust module: `scripts::check_formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: ROOT, args, argv, asdict, atomic_write_json, before, checked_output, digest, env, identity, key, load_profile, lock, matches_version, min, outputs, passed, pin, receipt, record, remaining, require, reserve_attempt, result, run_process, source, started, str, time, version, verus. Outputs/bindings: argv, before, key, outputs, passed, receipt, record, remaining, result, started, version.
Calls/effect boundaries: asdict, atomic_write_json, checked_output, digest, identity, load_profile, lock.release, matches_version, min, outputs.append, require, reserve_attempt, run_process, str, time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[18].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[0]::Assign

Source: `scripts/check_formal.py:47`; AST `a060092cf5b9b4c4e58aa60ba3d93a8aba5477f4ac2f8f9a56a632e33aa2f616`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: identity. Outputs/bindings: before.
Calls/effect boundaries: identity.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[0].value::Call

Source: `scripts/check_formal.py:47`; AST `6a00dd638daec40aa23c52f7515902cf1ea6b256ddef77bb268aec48a4bad550`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[1]::Assign

Source: `scripts/check_formal.py:48`; AST `204841eb7b755bf7abf280a2e5e1f03fdaab91faf3f8b3280f191364794c7f20`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, digest, env. Outputs/bindings: key.
Calls/effect boundaries: digest.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[1].value::Call

Source: `scripts/check_formal.py:48`; AST `1484f550904066fd0efb3c820d96c4b598136c0195bb600c14df2d3915267ea4`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, digest, env. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[2]::Expr

Source: `scripts/check_formal.py:49`; AST `78b2455628705e6eec6dea336cc621d0abc098b90dc46b2d2b736148572fef7d`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, args, key, load_profile, pin, require, reserve_attempt. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, require, reserve_attempt.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[2].value::Call

Source: `scripts/check_formal.py:49`; AST `1e56db6d3b42846774e16b25c240570a2b81e69f7700bf6de022e6f5ed03224a`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, key, load_profile, pin, require, reserve_attempt. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, require, reserve_attempt.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[2].value.args[0]::Call

Source: `scripts/check_formal.py:49`; AST `c79e8c7ccf809da029a3560dd154113d6cd487d6a04c8151fbd3d275ef3d36f7`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, args, key, load_profile, pin, reserve_attempt. Outputs/bindings: (none).
Calls/effect boundaries: load_profile, reserve_attempt.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[2].value.args[0].args[1]::Call

Source: `scripts/check_formal.py:49`; AST `fa1700caf9097f7f914b030615a19ed9a49e5e3378161e05148649b8f8521a73`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: load_profile. Outputs/bindings: (none).
Calls/effect boundaries: load_profile.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[2].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[3]::Assign

Source: `scripts/check_formal.py:50`; AST `ffb01939a1744166f8e8b1b6999b1f72c7d696dab355b4b68f83c3a867bfd6b0`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: time. Outputs/bindings: started.
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[3].value::Call

Source: `scripts/check_formal.py:50`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[4]::Assign

Source: `scripts/check_formal.py:51`; AST `29abd739e0f9510fbc369a0d7b4c2b001357a1b0e671e50ea16ce77a98965462`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: outputs.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5]::For

Source: `scripts/check_formal.py:52`; AST `37a742060b32141e032442752858fa29c0dc92c8ac7802998274b564ce1e39ca`.

Rust module: `scripts::check_formal`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ROOT, argv, asdict, env, matches_version, min, outputs, pin, remaining, require, result, run_process, started, str, time, version, verus. Outputs/bindings: argv, remaining, result, version.
Calls/effect boundaries: asdict, matches_version, min, outputs.append, require, run_process, str, time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered For evaluation at root.body[18].body[14].body[5]; no call, error or mutation may be omitted. Iteration: (argv, version) in (([str(verus), '--version'], pin['verus']), ([str(verus.parent / 'z3'), '--version'], pin['z3']))
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].iter.elts[0].elts[0].elts[0]::Call

Source: `scripts/check_formal.py:52`; AST `3569eaa6fd8a0be436e77fdaa6e2676e30953d465698119b1d75b7e22fe465d4`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, verus. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].iter.elts[0].elts[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].iter.elts[1].elts[0].elts[0]::Call

Source: `scripts/check_formal.py:53`; AST `c32051f392cc416cd7d5e30f2e10b8b914b6815e0a4712825361ef8a5a2c1914`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, verus. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].iter.elts[1].elts[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[0]::Assign

Source: `scripts/check_formal.py:54`; AST `6566cb221aa1eb2c1646124473d3be5ce31e0af7774980929ac2abdce3caf2c0`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pin, started, time. Outputs/bindings: remaining.
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[0].value.right.left::Call

Source: `scripts/check_formal.py:54`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[0].value.right.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[1]::Expr

Source: `scripts/check_formal.py:55`; AST `fa17ad17d5622e95f7d3da8c0acc585e5fc99d73fdf3c8f6aff15d092721a3d1`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[1].value::Call

Source: `scripts/check_formal.py:55`; AST `670b58bdcf3108777b412f50a4f71ec2868d2e934197591245942bbfd2fe45e4`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[2]::Assign

Source: `scripts/check_formal.py:56`; AST `3a03a17cf5ab2f33b53e77f6edea2224913d02760d03183a021c157a3042b02c`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, argv, env, min, remaining, run_process. Outputs/bindings: result.
Calls/effect boundaries: min, run_process.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[2].value::Call

Source: `scripts/check_formal.py:56`; AST `bd679cd403e8fac5c9673413d8bff1d4a4e1b52821181d896984f454a68898bf`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, argv, env, min, remaining, run_process. Outputs/bindings: (none).
Calls/effect boundaries: min, run_process.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[2].value.keywords[2].value::Call

Source: `scripts/check_formal.py:56`; AST `07a2d85a289aa27e5b56c6580d07e01ddd539f65007409d7e2a3131fac2e488f`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: min, remaining. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[2].value.keywords[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[3]::Expr

Source: `scripts/check_formal.py:57`; AST `03e3824df9dc0643d15cfcaa46fd69fdb6554d503068985418c3e1845c20d636`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, outputs, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict, outputs.append.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[3].value::Call

Source: `scripts/check_formal.py:57`; AST `c5ed654a60276d6481fb4f1e3735508980999ba8aebef7ac135be664ae4f2299`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, outputs, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict, outputs.append.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[3].value.args[0]::Call

Source: `scripts/check_formal.py:57`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[4]::Expr

Source: `scripts/check_formal.py:58`; AST `afbbecc3925c8fefef81c7a1eea6d3c50cabf333838480c978e38c6505f98e14`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: matches_version, require, result, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[4].value::Call

Source: `scripts/check_formal.py:58`; AST `58f1d8ca05e6a699b81cfd54a2f93aa07d925f8913069040bfc59b42c3ecb4c0`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version, require, result, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[5].body[4].value.args[0].values[4]::Call

Source: `scripts/check_formal.py:59`; AST `89a311d40f95de235cc00ccaacef67469b85ae5c0c33d2c9b87cd648acd05948`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: matches_version, result, version. Outputs/bindings: (none).
Calls/effect boundaries: matches_version.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[5].body[4].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[6]::Assign

Source: `scripts/check_formal.py:61`; AST `6566cb221aa1eb2c1646124473d3be5ce31e0af7774980929ac2abdce3caf2c0`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pin, started, time. Outputs/bindings: remaining.
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[6].value.right.left::Call

Source: `scripts/check_formal.py:61`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[6].value.right.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[7]::Expr

Source: `scripts/check_formal.py:62`; AST `c519cd58e74ee19812f3ea272d34a3b958ff8682ae66f6a57475bba59f70e3eb`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[7].value::Call

Source: `scripts/check_formal.py:62`; AST `41364bee300d52837d7f0a10defd5c61c54d2970335ddc56a4bbd4715ede358c`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[8]::Assign

Source: `scripts/check_formal.py:63`; AST `46814ac9f44981bda9ee4088e2952d0ce7bc2fa27216cc261d50e62857968139`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, env, remaining, run_process, source, str, verus. Outputs/bindings: result.
Calls/effect boundaries: run_process, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[8].value::Call

Source: `scripts/check_formal.py:63`; AST `0c7415f499fa631632e7c05d466af420eb3eff6951ec32b37150855f1ae7e356`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ROOT, env, remaining, run_process, source, str, verus. Outputs/bindings: (none).
Calls/effect boundaries: run_process, str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[8].value.args[0].elts[0]::Call

Source: `scripts/check_formal.py:63`; AST `3569eaa6fd8a0be436e77fdaa6e2676e30953d465698119b1d75b7e22fe465d4`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: str, verus. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[8].value.args[0].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[8].value.args[0].elts[5]::Call

Source: `scripts/check_formal.py:63`; AST `e84c9c7864af0fee24e28123120dae12990caa3a9145d280b7a0f55e8d6cb247`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[8].value.args[0].elts[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[9]::Expr

Source: `scripts/check_formal.py:65`; AST `cc7d5af108090e646b0848975bffcd2c22db853d919e9683133b0feb122d4a90`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: before, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: identity, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[9].value::Call

Source: `scripts/check_formal.py:65`; AST `c13d152e717ed30fef2ba30e7e2ab5beb32c0cabd4c7b2e9c3fd468efd0d1153`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: before, identity, require. Outputs/bindings: (none).
Calls/effect boundaries: identity, require.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[9].value.args[0].left::Call

Source: `scripts/check_formal.py:65`; AST `6a00dd638daec40aa23c52f7515902cf1ea6b256ddef77bb268aec48a4bad550`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: identity. Outputs/bindings: (none).
Calls/effect boundaries: identity.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[9].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[10]::Assign

Source: `scripts/check_formal.py:66`; AST `f1b734dc0094bfbe1810a96dfb4381decce9cde3f05c0bab56f3ae5c76e144c2`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: checked_output, pin, result. Outputs/bindings: passed.
Calls/effect boundaries: checked_output.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[10].value::Call

Source: `scripts/check_formal.py:66`; AST `0b7cc5c429ebacdc16dc460611c299571e601801d171e2edce0e657a9dca59bd`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: checked_output, pin, result. Outputs/bindings: (none).
Calls/effect boundaries: checked_output.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[11]::Assign

Source: `scripts/check_formal.py:67`; AST `b6b6913c7cbc0d0bf31a7389b41eb1a0cb3e66d90f75ce577befe744ea882c05`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, before, env, outputs, passed, pin, result. Outputs/bindings: record.
Calls/effect boundaries: asdict.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[11].value.values[5]::Call

Source: `scripts/check_formal.py:68`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[11].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[12]::Assign

Source: `scripts/check_formal.py:70`; AST `e0714adfba58fde834ea61a86fd40108eaeaf2603a5dce2b47bffcad14c2ab8b`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[12].value::Call

Source: `scripts/check_formal.py:70`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[13]::Assign

Source: `scripts/check_formal.py:71`; AST `d74a319548f23e9d47978099cec61b0695b72cd0bbfbf871a74adce03545d3fa`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ROOT, record. Outputs/bindings: receipt.
Calls/effect boundaries: (none).
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[14]::Expr

Source: `scripts/check_formal.py:72`; AST `4857b0ea1157c6762a9be342fc49bc7d27d14b6c04aa3f7acd5291b70a4241c9`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, receipt, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[14].value::Call

Source: `scripts/check_formal.py:72`; AST `ddacbbffd23316bf767d3682d783a3e078a421000ad7a7ed2639956bffbb8bd1`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, receipt, record. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[15]::Return

Source: `scripts/check_formal.py:73`; AST `e70887a88783040c34af957dc65d61a28b89663111ec386960abe1cd44e48206`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: pin, receipt, record, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Return evaluation at root.body[18].body[14].body[15]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].body[15].value.values[1]::Call

Source: `scripts/check_formal.py:73`; AST `294615daf0e87fb66923e7bb46155e37932b9bddff262913d7e0398bfbb228b0`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: receipt, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].body[15].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].finalbody[0]::Expr

Source: `scripts/check_formal.py:75`; AST `9aa6f04fc26ee6b3f6fe1a19158adb3cfde13709dcae4a7cc38bccbb2655afb2`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[14].finalbody[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::verify::root.body[18].body[14].finalbody[0].value::Call

Source: `scripts/check_formal.py:75`; AST `107c5710331db61e695f7d71256d48862412d15c223e204da5c71c497352b634`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.release.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[18].body[14].finalbody[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19]::If

Source: `scripts/check_formal.py:78`; AST `c855bc81926c44deb177a7bb198bd81a13207c7dd94d08a0a62237c7579e7b32`.

Rust module: `scripts::check_formal`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: ArgumentParser, KeyError, OSError, RuntimeError, SystemExit, TypeError, ValueError, __doc__, __name__, args, exc, json, p, print, result, str, verify. Outputs/bindings: args, p, result.
Calls/effect boundaries: ArgumentParser, SystemExit, json.dumps, p.add_argument, p.parse_args, print, str, verify.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered If evaluation at root.body[19]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[0]::Assign

Source: `scripts/check_formal.py:79`; AST `b9cbe578e877a2eaf69fa3e73216df4fd90d8af363953f3a5b6176e34c3b21da`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ArgumentParser, __doc__. Outputs/bindings: p.
Calls/effect boundaries: ArgumentParser.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[0].value::Call

Source: `scripts/check_formal.py:79`; AST `61dd938be7740b4c0c13120a92c24d23f639874a56ec8271ae0059a6354c7075`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ArgumentParser, __doc__. Outputs/bindings: (none).
Calls/effect boundaries: ArgumentParser.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[1]::Expr

Source: `scripts/check_formal.py:80`; AST `e08a1bc74151d5aa2f2c05949ebb79b5c41864b640c10a66a0c94d7849e4f57d`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_argument.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[1].value::Call

Source: `scripts/check_formal.py:80`; AST `48650b6c40c59af465e4bc57659786ba53a7b5cb52a3dd6d08d2ba14fa3204ee`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_argument.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[2]::Expr

Source: `scripts/check_formal.py:81`; AST `7493f95d24ac431f46d8be6a1a39426ce85cb37e1bf243401470828defb2fbe2`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_argument.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[2].value::Call

Source: `scripts/check_formal.py:81`; AST `f7133c1b784aa557947c18d2e58e7d1c20bab2595ed33b886cbae16625c3835d`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.add_argument.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[3]::Assign

Source: `scripts/check_formal.py:82`; AST `4140262007419c1c529f90a9a4264780735da1ff8af31c0f42b9dcc60a1dd3bd`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: p. Outputs/bindings: args.
Calls/effect boundaries: p.parse_args.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[3].value::Call

Source: `scripts/check_formal.py:82`; AST `4b3bad6ca7a4d4119f304649f8c717ae32c8553857f3d229eec66db830fe40ca`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.parse_args.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4]::Try

Source: `scripts/check_formal.py:83`; AST `ade4b96154fd74bbe5ba2833ffb5f8b460a2b4ba53ca0dd8ea8536d3f415d4ba`.

Rust module: `scripts::check_formal`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: KeyError, OSError, RuntimeError, TypeError, ValueError, args, exc, str, verify. Outputs/bindings: result.
Calls/effect boundaries: str, verify.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Try evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4].body[0]::Assign

Source: `scripts/check_formal.py:84`; AST `1e6589f240a71087c693db9fb65dedc5d9203c09792bbc16779000fd59885dfe`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: args, verify. Outputs/bindings: result.
Calls/effect boundaries: verify.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4].body[0].value::Call

Source: `scripts/check_formal.py:84`; AST `e1dd7f2e6ebf00d69a783aad38c9c973f6adf657e27a3fa8cfa5228b33a29fb2`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: args, verify. Outputs/bindings: (none).
Calls/effect boundaries: verify.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4].handlers[0]::ExceptHandler

Source: `scripts/check_formal.py:85`; AST `979ae80f92f4081212a3346ceda5d66fec7f7d59cab1a10bcfd7ed7b75d73aec`.

Rust module: `scripts::check_formal`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: KeyError, OSError, RuntimeError, TypeError, ValueError, exc, str. Outputs/bindings: result.
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[4].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4].handlers[0].body[0]::Assign

Source: `scripts/check_formal.py:86`; AST `125654dc26af6059c6a658397900f18214205c6f2769891c74e518f11dc41e4f`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, str. Outputs/bindings: result.
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[4].handlers[0].body[0].value.values[1]::Call

Source: `scripts/check_formal.py:86`; AST `ed91e0e2c4feb43ad37ba7941b4ee3c7dcc36d3eb80d4a170990c028aa16f027`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].handlers[0].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[5]::Expr

Source: `scripts/check_formal.py:87`; AST `d816772e8e023db121760f52dbccf861ae7ce233a2beaf6016e184433a47ad02`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[5].value::Call

Source: `scripts/check_formal.py:87`; AST `ee3717087b237ccd743239af61bbe8734d121db150340a4d5a8674d4958ade09`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, print, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, print.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[5].value.args[0]::Call

Source: `scripts/check_formal.py:87`; AST `00d46c6b8a01b70b1f1d7d9c3b8e42d3c1fb1af83238e95a34624e9451c0d595`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, result. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[6]::Raise

Source: `scripts/check_formal.py:88`; AST `d1a0cc87198e3ef4dd0bc668d5c5f641815dc419f8da2d3b4c32c5b3d9409fab`.

Rust module: `scripts::check_formal`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: SystemExit, result. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/check_formal.py::module::root.body[19].body[6].exc::Call

Source: `scripts/check_formal.py:88`; AST `0fc84825f7ce80c2ca0ac634e0742c59418caaa6d8fe2640a33de2e1c246d275`.

Rust module: `scripts::check_formal`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: SystemExit, result. Outputs/bindings: (none).
Calls/effect boundaries: SystemExit.
Dependencies: agentinfra.atomic, agentinfra.context_cache, agentinfra.destiny, agentinfra.destiny_reuse, agentinfra.locks, agentinfra.process, agentinfra.security, argparse, dataclasses, json, os, pathlib, shutil, sys, time.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].exc; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf; std::time::Instant / SystemTime; clap
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
