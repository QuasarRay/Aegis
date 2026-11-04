# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 299. Inventory digest: `0f08a5044c6d333cecf5eb1e255e37ac8f12f3c2d7e76626b96f37c380fe1885`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## scripts/roadmap_esbmc.py::module::root::Module

Source: `scripts/roadmap_esbmc.py:1`; AST `885da6586f85572a52c7a9ff221471b32d58085cd3df00e7bc159e7a33dd69f2`.

Rust module: `scripts::roadmap_esbmc`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: Path, PurePosixPath, TRANSPORT, all, archive, archive_binding, argv, artifacts, asdict, atomic_write_json, b, binding, bindings_current, bundle, claims, claims_binding, claims_path, classification, classify_esbmc, confined_path, deadline, destination, dict, digest, directory, download_with_mirrors, entries, entry, environment, esbmc_arguments, esbmc_link_state, executables, extract_release, file_binding, files, fixture, identity, len, link, links, lock, map, marker, minimal_subprocess_env, mode, name, names, os, output, p, path, profile, python, read_download_policy, read_json, release, require, resolved, result, result_binding, root, run_recipe_stage, runs, saved, set, shutil, sorted, source, source_closure, staging, stat, state, str, sum, symlinks, sys, target, time, toolchain, toolchain_path, venv, virtual, wheels, x, zipfile. Outputs/bindings: _, archive, archive_binding, argv, artifacts, binding, bundle, claims, claims_binding, claims_path, classification, deadline, destination, directory, entries, entry, environment, executables, files, fixture, identity, link, links, lock, marker, mode, name, names, output, p, path, profile, python, release, resolved, result, result_binding, runs, saved, source, staging, state, symlinks, target, toolchain, virtual, wheels, x.
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, (destination / p.relative_to(staging)).relative_to(root).as_posix, (target.parent / link).resolve, (virtual / 'bin/python').exists, Path, Path(link).is_absolute, PurePosixPath, all, archive.relative_to, archive.relative_to(root).as_posix, artifacts.append, artifacts.extend, asdict, atomic_write_json, bindings_current, bundle.infolist, bundle.open, bundle.read, bundle.read(entry).decode, claims_path.relative_to, claims_path.relative_to(root).as_posix, classify_esbmc, confined_path, destination.exists, destination.relative_to, destination.relative_to(root).as_posix, destination.rglob, destination.with_name, dict, digest, directory.mkdir, directory.rglob, download_with_mirrors, entry.filename.rstrip, entry.is_dir, esbmc_arguments, esbmc_link_state, extract_release, file_binding, len, links.append, lock.get, map, marker.is_file, minimal_subprocess_env, os.access, os.uname, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, path.is_absolute, path.relative_to, path.relative_to(root).as_posix, read_download_policy, read_json, release.relative_to, release.relative_to(root).as_posix, release.rglob, require, resolved.is_relative_to, run_recipe_stage, runs.append, saved.get, set, shutil.copyfileobj, sorted, source_closure, staging.exists, staging.mkdir, staging.rename, staging.resolve, stat.S_IFMT, stat.S_ISLNK, str, sum, target.chmod, target.exists, target.is_symlink, target.mkdir, target.open, target.parent.mkdir, target.resolve, target.resolve().is_relative_to, target.symlink_to, time.monotonic, toolchain.get, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create, x.filename.rstrip, zipfile.ZipFile.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[0]::Expr

Source: `scripts/roadmap_esbmc.py:1`; AST `5e63d18a96fcd659acc98a1520a710de0265c0da1314b6fd2adaca6aeee736cf`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[1]::ImportFrom

Source: `scripts/roadmap_esbmc.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[2]::ImportFrom

Source: `scripts/roadmap_esbmc.py:4`; AST `400d7764c2a2b8cabf9a4dc4cd172f3f6e19abcbe53e771b676ad31a327775fa`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[3]::Import

Source: `scripts/roadmap_esbmc.py:5`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[4]::ImportFrom

Source: `scripts/roadmap_esbmc.py:6`; AST `40c6b803ee13cbcec633052def0cd7814baf9bfd67818b3dd46dd82625d3e333`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[5]::Import

Source: `scripts/roadmap_esbmc.py:7`; AST `b461ae95c16c1e73a466fdd306ad6da693ead3a324e5d33627958cc4a2f47e36`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[6]::Import

Source: `scripts/roadmap_esbmc.py:8`; AST `c22b5a111acc3bea9e5136e41e207f1f95083e90d861516ce34d682526721c86`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[7]::Import

Source: `scripts/roadmap_esbmc.py:9`; AST `f7252e3c1dbe1d5edf1f34c020a58a05b55f706b2c1d9479eae91f9a9d4be275`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[8]::Import

Source: `scripts/roadmap_esbmc.py:10`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[9]::Import

Source: `scripts/roadmap_esbmc.py:11`; AST `ed2cb5c0bad66165f89629cf1ddc37e5077e2360bde054e7e311c6e64bed20c6`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[10]::Import

Source: `scripts/roadmap_esbmc.py:12`; AST `4123c8e546e07497699149dda363dc8539207c3974a8a7d70400f73212c30178`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Import evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[11]::ImportFrom

Source: `scripts/roadmap_esbmc.py:14`; AST `e706389dc4535d08f9bd29369c244a847d9b553c6dcf2248be7dd6d082410af1`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[12]::ImportFrom

Source: `scripts/roadmap_esbmc.py:15`; AST `53de7f6c4c3d9d3208c4dde7e7ab94a698ffba0be3741058ffc6fca32b8ec724`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[13]::ImportFrom

Source: `scripts/roadmap_esbmc.py:16`; AST `db5c8677a4f676e011786557ebf779dfd621dafd3f5394ec9f88c9673bebca4e`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[14]::ImportFrom

Source: `scripts/roadmap_esbmc.py:17`; AST `e951ad861c4446d722893978996adccc021d19add69685ab9ecd5b5e945b89e7`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[15]::ImportFrom

Source: `scripts/roadmap_esbmc.py:18`; AST `e70166107f04b82e695c59137d27151ca7893d8e4f198d93b95af9cef6ce0ef0`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::root.body[16]::ImportFrom

Source: `scripts/roadmap_esbmc.py:19`; AST `e0ffff08081556b53bbf2f6e7c9f8aea08955e05b121baaa0cd5b75e05c5cd1b`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ImportFrom evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17]::FunctionDef

Source: `scripts/roadmap_esbmc.py:22`; AST `7f228bd2f938522719af0b99ec9fc948c021889efaf8f4f3ef25678322bd11bb`.

Rust module: `scripts::roadmap_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, PurePosixPath, all, archive, archive_binding, atomic_write_json, b, bindings_current, bundle, confined_path, destination, entries, entry, esbmc_link_state, file_binding, files, len, link, links, marker, mode, name, names, output, p, path, read_json, require, resolved, root, saved, set, shutil, sorted, source, staging, stat, state, str, sum, symlinks, target, x, zipfile. Outputs/bindings: _, archive_binding, bundle, destination, entries, entry, files, link, links, marker, mode, name, names, output, p, path, resolved, saved, source, staging, state, symlinks, target, x.
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, (destination / p.relative_to(staging)).relative_to(root).as_posix, (target.parent / link).resolve, Path, Path(link).is_absolute, PurePosixPath, all, archive.relative_to, archive.relative_to(root).as_posix, atomic_write_json, bindings_current, bundle.infolist, bundle.open, bundle.read, bundle.read(entry).decode, confined_path, destination.exists, destination.relative_to, destination.relative_to(root).as_posix, destination.rglob, destination.with_name, entry.filename.rstrip, entry.is_dir, esbmc_link_state, file_binding, len, links.append, marker.is_file, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, path.is_absolute, read_json, require, resolved.is_relative_to, saved.get, set, shutil.copyfileobj, sorted, staging.exists, staging.mkdir, staging.rename, staging.resolve, stat.S_IFMT, stat.S_ISLNK, str, sum, target.chmod, target.exists, target.is_symlink, target.mkdir, target.open, target.parent.mkdir, target.resolve, target.resolve().is_relative_to, target.symlink_to, x.filename.rstrip, zipfile.ZipFile.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:23`; AST `2807497b5df1e91d56c360e6c60dc10df436180d6f67587b9d3e467bd721f1d9`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:24`; AST `b5b4bcb29da7020f3289b51eae269232641c5ff66375199f52fe9daf5147d919`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, destination, root. Outputs/bindings: destination.
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:24`; AST `e957657579bb3eb016e5841d8485c54f2fc5b5371eb1752b9c8ea45f82f025a1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, destination, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[2]::Assign

Source: `scripts/roadmap_esbmc.py:25`; AST `5e8bc7b15c070e9f905b780f16973a0541c63e5bd3f84cb0280a4f08047e1c35`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination. Outputs/bindings: marker.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:26`; AST `8bb34c091b04a79f4d27159abaf72439191c7b71d3858e6534538424e674b9b3`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, file_binding, root. Outputs/bindings: archive_binding.
Calls/effect boundaries: archive.relative_to, archive.relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:26`; AST `1ac6e2cf371709d849127b81d2ee0f806e8fa0e28e1c078f0220ad8a15ecca6c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: archive.relative_to, archive.relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[3].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:26`; AST `4438117fb4a59e329c298c00d98c0ba530e9dafc399bc679ed0470bb05c6d54b`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, root. Outputs/bindings: (none).
Calls/effect boundaries: archive.relative_to, archive.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[3].value.args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:26`; AST `5dfea53d7a27be33972af0a570f276353067b38366b1660f55bd0b2bd487d27a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, root. Outputs/bindings: (none).
Calls/effect boundaries: archive.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4]::If

Source: `scripts/roadmap_esbmc.py:27`; AST `779b3fa19492a9c34e2a1a07f687300e02f8a2048cf3178965711799ae4573d8`.

Rust module: `scripts::roadmap_esbmc`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: all, archive_binding, bindings_current, destination, esbmc_link_state, marker, read_json, require, root, saved, state, x. Outputs/bindings: saved, state, x.
Calls/effect boundaries: all, bindings_current, destination.exists, destination.relative_to, destination.relative_to(root).as_posix, esbmc_link_state, marker.is_file, read_json, require, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered If evaluation at root.body[17].body[4]; no call, error or mutation may be omitted. Condition: destination.exists()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].test::Call

Source: `scripts/roadmap_esbmc.py:27`; AST `63204dbdfb8c413cedd2da584060b63f287edaac6b32432ac94605d193b3ea53`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:28`; AST `6c55c694c8f65e183d5d200a8a35b8afacdc0ae0c27704e592e103588e4fdbe2`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: marker, require. Outputs/bindings: (none).
Calls/effect boundaries: marker.is_file, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:28`; AST `73df04640e01c64a86948d7623c770c25239720488d6c80bccf4bc3f4cf70063`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker, require. Outputs/bindings: (none).
Calls/effect boundaries: marker.is_file, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[0].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:28`; AST `439e89f4f672c1a633448173a236b6641e37bed926c98c69cef381e73f18a9e1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker. Outputs/bindings: (none).
Calls/effect boundaries: marker.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:29`; AST `2065000a3628ae75251860da99a86038c32401914017faf1e4714c267917fa6c`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: marker, read_json. Outputs/bindings: saved.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:29`; AST `0e73675e907278cb3438ce9af7d1bdb009fcdb332eba5755104565b65d80ea20`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: marker, read_json. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:30`; AST `d1008d05608b93a1668ccc8c789981c7804a39463615d8fb457d23add903b99a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive_binding, bindings_current, require, root, saved. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:30`; AST `d05535073c63de37b4c26d921e5a55a473ce8bb75d08f93547ef7f4dd9769a5a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive_binding, bindings_current, require, root, saved. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[2].value.args[0].values[0].left::Call

Source: `scripts/roadmap_esbmc.py:30`; AST `3e8f539082d9444de36a405fa7a76a6cdbdbba2785682a99710119a2808b97e5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: saved. Outputs/bindings: (none).
Calls/effect boundaries: saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[2].value.args[0].values[1]::Call

Source: `scripts/roadmap_esbmc.py:30`; AST `c15371c8bb6af34982130bbe3aae7b2191d2e446812505cbad1c0b518ff52327`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, saved. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[2].value.args[0].values[1].args[1]::Call

Source: `scripts/roadmap_esbmc.py:30`; AST `0b536ea0c6a0ad2f371ce7cf8db0d2453f1c08a47653f1f5b9dbf863ac141a34`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: saved. Outputs/bindings: (none).
Calls/effect boundaries: saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[2].value.args[0].values[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:31`; AST `a2c4c7f0bc6931dbe8099344b3d67de0708a9fbe7efbdfe5d59afb606c026bfc`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, esbmc_link_state, root, saved. Outputs/bindings: state.
Calls/effect boundaries: destination.relative_to, destination.relative_to(root).as_posix, esbmc_link_state, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:31`; AST `342428eabdefe1e1a79eba741de4e69907aeb1d63c8d4286ec22107b8d605578`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, esbmc_link_state, root, saved. Outputs/bindings: (none).
Calls/effect boundaries: destination.relative_to, destination.relative_to(root).as_posix, esbmc_link_state, saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[3].value.args[1].values[0]::Call

Source: `scripts/roadmap_esbmc.py:31`; AST `0e624fbf7d989661408eef0d46e624e52982cc4e0e15fb0ea0bc943a6c245dc7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, root. Outputs/bindings: (none).
Calls/effect boundaries: destination.relative_to, destination.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[1].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[3].value.args[1].values[0].func.value::Call

Source: `scripts/roadmap_esbmc.py:31`; AST `88b166e64f8d8d44a59866f759bbf2b233094c2ee19617f94fbdace9ae507ed1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, root. Outputs/bindings: (none).
Calls/effect boundaries: destination.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[1].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[3].value.args[1].values[1]::Call

Source: `scripts/roadmap_esbmc.py:31`; AST `cec76056d70af87cd3f901770dceebdba9f7f52f4b9730cc11c6333601c669ad`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: saved. Outputs/bindings: (none).
Calls/effect boundaries: saved.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[3].value.args[1].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:32`; AST `8697a51a33622e8c9dd7d4b647630b67b3c2d1b9735d26c9cb015deee3d320cf`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, require, state, x. Outputs/bindings: x.
Calls/effect boundaries: all, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:32`; AST `d9a6697e0af5dc321080762b15ef5cfe151fba3a8350692bbf63eca98cede01e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, require, state, x. Outputs/bindings: x.
Calls/effect boundaries: all, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[4].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:32`; AST `41860388425e7317182cfe23e657d373c08ff66a846197756d3487c19ffe8fb2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, state, x. Outputs/bindings: x.
Calls/effect boundaries: all.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[4].value.args[0].args[0]::GeneratorExp

Source: `scripts/roadmap_esbmc.py:32`; AST `7473cc5c0075e12d37dd7c63391c46fee6e984be26bbe37071d5d9364a84eaa4`.

Rust module: `scripts::roadmap_esbmc`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: state, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[4].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[4].body[5]::Return

Source: `scripts/roadmap_esbmc.py:33`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[17].body[4].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[5]::Assign

Source: `scripts/roadmap_esbmc.py:34`; AST `54118ebbd734f40b6b7cb0b2c81472351b30042dedf73e83bcdf3d6d9002955d`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination. Outputs/bindings: staging.
Calls/effect boundaries: destination.with_name.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[5].value::Call

Source: `scripts/roadmap_esbmc.py:34`; AST `1ea574c9aa7074e48e6156608e048635dcd585ac28a6b8955697b86986299bf7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.with_name.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[6]::Expr

Source: `scripts/roadmap_esbmc.py:35`; AST `24db91c91f49af0ef6d79f96b589dca9be3378f23c04349436d05cd08cad97c0`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, staging. Outputs/bindings: (none).
Calls/effect boundaries: require, staging.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[6].value::Call

Source: `scripts/roadmap_esbmc.py:35`; AST `d0b405c1d03142aadd20fc30302de3766d6bb771749cb3e39629116fa649e1f8`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, staging. Outputs/bindings: (none).
Calls/effect boundaries: require, staging.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[6].value.args[0].operand::Call

Source: `scripts/roadmap_esbmc.py:35`; AST `bf4918c45c09ab2bf1b0e8a93cf45775711d14ececb6734056a5b5261fd31584`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[7]::Assign

Source: `scripts/roadmap_esbmc.py:36`; AST `3394cbc20ecbd77f539283ee6219b0b320d6f4a2f40d9b86337c3b68570b575c`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: links.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8]::With

Source: `scripts/roadmap_esbmc.py:37`; AST `aa05d1dba94dd9d25d1c9b8851611dd97f25a7b02fcb6e8daaa12f54c95d968c`.

Rust module: `scripts::roadmap_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: Path, PurePosixPath, archive, bundle, confined_path, entries, entry, len, link, links, mode, name, names, output, path, require, resolved, root, set, shutil, source, staging, stat, str, sum, target, x, zipfile. Outputs/bindings: bundle, entries, entry, link, mode, name, names, output, path, resolved, source, target, x.
Calls/effect boundaries: (target.parent / link).resolve, Path, Path(link).is_absolute, PurePosixPath, bundle.infolist, bundle.open, bundle.read, bundle.read(entry).decode, confined_path, entry.filename.rstrip, entry.is_dir, len, links.append, path.is_absolute, require, resolved.is_relative_to, set, shutil.copyfileobj, staging.mkdir, staging.resolve, stat.S_IFMT, stat.S_ISLNK, str, sum, target.chmod, target.exists, target.mkdir, target.open, target.parent.mkdir, x.filename.rstrip, zipfile.ZipFile.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered With evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].items[0].context_expr::Call

Source: `scripts/roadmap_esbmc.py:37`; AST `6d90a041d09b786c520fdd0cb9a546e563379e61a9f7b2bd5363383831bd108b`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, zipfile. Outputs/bindings: (none).
Calls/effect boundaries: zipfile.ZipFile.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:38`; AST `fa2a6e931bdcfa18a1a0286588eb60b1694d3fbfbff534269d2213a57309e9e6`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bundle. Outputs/bindings: entries.
Calls/effect boundaries: bundle.infolist.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:38`; AST `92069593eab8d0b2bc010f9b4b1a6f91ca0ec724c093704da8cf096cae827786`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bundle. Outputs/bindings: (none).
Calls/effect boundaries: bundle.infolist.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[1]::Expr

Source: `scripts/roadmap_esbmc.py:39`; AST `027af9bc284d11e8d67c73e651a99c51b631e633c3b4d326e1381fd929ac22b3`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, len, require, sum, x. Outputs/bindings: x.
Calls/effect boundaries: len, require, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:39`; AST `86eee70bb8d4fd2dc54dd986ec12990f4d16090664712567e8381cd62979421f`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, len, require, sum, x. Outputs/bindings: x.
Calls/effect boundaries: len, require, sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[1].value.args[0].values[0].comparators[0]::Call

Source: `scripts/roadmap_esbmc.py:39`; AST `22260685a0fdc6a14217dce23ad22bc48643fd54da96058a4d41c4370cfbcdf8`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[1].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[1].value.args[0].values[1].left::Call

Source: `scripts/roadmap_esbmc.py:39`; AST `c76cb0c7da22e44a91761d3ba650c68cd8613f0eb9e62276c18e86cb6d35fcff`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entries, sum, x. Outputs/bindings: x.
Calls/effect boundaries: sum.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[1].value.args[0].values[1].left.args[0]::GeneratorExp

Source: `scripts/roadmap_esbmc.py:39`; AST `db59b254ce9472089da5d7406bc36f9efade25d3e0770c9d176fedab315dd3d2`.

Rust module: `scripts::roadmap_esbmc`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: entries, x. Outputs/bindings: x.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[8].body[1].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[2]::Assign

Source: `scripts/roadmap_esbmc.py:40`; AST `dc44663918d46eb90147b3f61c1e62a623d32bc0de4bfe844aa3642c9e057246`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entries, x. Outputs/bindings: names, x.
Calls/effect boundaries: x.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[2].value::ListComp

Source: `scripts/roadmap_esbmc.py:40`; AST `c7396c5b3c7131e27c7427b510edae907ef39ea0f72bec64f23fa58926beae66`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: entries, x. Outputs/bindings: x.
Calls/effect boundaries: x.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[8].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[2].value.elt::Call

Source: `scripts/roadmap_esbmc.py:40`; AST `b2795e373a54f8bfee67d52107ca5eef6641e60c040a86861d7e3f875cb1b122`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: x. Outputs/bindings: (none).
Calls/effect boundaries: x.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[2].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[3]::Expr

Source: `scripts/roadmap_esbmc.py:41`; AST `fee9a6a368d952c1bd7e20928de33415246eec902e36998ac10b22c40a0c9c01`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, names, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:41`; AST `eba1477b2a33cec40ffdd5501d608da7697b3321e07a88fafae0dc11bee32fc0`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, names, require, set. Outputs/bindings: (none).
Calls/effect boundaries: len, require, set.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[3].value.args[0].values[0].left::Call

Source: `scripts/roadmap_esbmc.py:41`; AST `ce9fca83fd900bbca95e221c4430f53047c3367df4d8c6e4d6bab8047d93db4c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, names. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[3].value.args[0].values[0].comparators[0]::Call

Source: `scripts/roadmap_esbmc.py:41`; AST `9eda32bdda72d44b7edb2789a627b3413b206903609fed31e70f978691fc74a6`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, names, set. Outputs/bindings: (none).
Calls/effect boundaries: len, set.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[3].value.args[0].values[0].comparators[0].args[0]::Call

Source: `scripts/roadmap_esbmc.py:41`; AST `862a7b0f4436264fe85b17b02bd7de07da4560fba9f6772ccbe2128fc3588829`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: names, set. Outputs/bindings: (none).
Calls/effect boundaries: set.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[3].value.args[0].values[0].comparators[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4]::For

Source: `scripts/roadmap_esbmc.py:42`; AST `c78f0ea1c67ad03be9da1711ca73c73c10119fee0237ddc7981a6981f2e51cb5`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: PurePosixPath, entries, entry, mode, name, path, require, stat, str. Outputs/bindings: entry, mode, name, path.
Calls/effect boundaries: PurePosixPath, entry.filename.rstrip, path.is_absolute, require, stat.S_IFMT, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[17].body[8].body[4]; no call, error or mutation may be omitted. Iteration: entry in entries
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:43`; AST `59c7f7beef54b31112f804acdb6ba34fbc7653de0641ce0fc4f63782fa0af8c0`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: name.
Calls/effect boundaries: entry.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:43`; AST `84f639e63ecc1e000e85f68a145cbc718e587722ff3a6c7c860c5e9ebe7f0a2a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:44`; AST `83077c68c8b276e1d8a694f60d13d940e0bdeb91b3d4b875b75ff9f5015c902c`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: PurePosixPath, name. Outputs/bindings: path.
Calls/effect boundaries: PurePosixPath.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[4].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:44`; AST `cc48c4c9f96747100b7a924d79efd2ae9d5fdec8080b87f89008f71c72cf773e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: PurePosixPath, name. Outputs/bindings: (none).
Calls/effect boundaries: PurePosixPath.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:45`; AST `195854551672f4edd1dd9b2770bc3725840cbdf9c7aa40a3a4be7dd8f1e7b279`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, path, require, str. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute, require, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[4].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:45`; AST `1b7c94145ba1eb55f1107fdf373b283c6a737927008d7a0fcb89c8ad5b883ed0`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: name, path, require, str. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute, require, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[2].value.args[0].values[1].operand::Call

Source: `scripts/roadmap_esbmc.py:45`; AST `b6c359348f99100e1e49132bf117e1cf4485da0246e8b496522239d8400f0c44`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.is_absolute.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[2].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[2].value.args[0].values[4].left::Call

Source: `scripts/roadmap_esbmc.py:45`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[2].value.args[0].values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:47`; AST `e33d93045a27b310c04c752ec0ca8dcd0754f285df750fd77b508752a7d201b8`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: mode.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[4].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:48`; AST `97663ca1c105f4c022a735724dc33e4040f08cde1e1491c987de99d5a734735b`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mode, require, stat. Outputs/bindings: (none).
Calls/effect boundaries: require, stat.S_IFMT.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[4].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:48`; AST `f0a77774a01fe4324781b39e81cd3e667af0d189b7c6482e58c507d50eaa0df8`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mode, require, stat. Outputs/bindings: (none).
Calls/effect boundaries: require, stat.S_IFMT.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[4].body[4].value.args[0].left::Call

Source: `scripts/roadmap_esbmc.py:48`; AST `574c47f8b2078616e9a926e4fb2bbaef6f656ec1bdd30268eb75b59177d0ce68`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mode, stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.S_IFMT.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[4].body[4].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[5]::Expr

Source: `scripts/roadmap_esbmc.py:49`; AST `21be1d8a3629cae92d89bc79e57d5f0615d23170e85ec68328ee2d5dc8dd16be`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[5].value::Call

Source: `scripts/roadmap_esbmc.py:49`; AST `ce430d05fc0e6b89d8762bda8641157a4da69a0198fd0b8ffd3e8601bcceca6c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6]::For

Source: `scripts/roadmap_esbmc.py:50`; AST `d9d1f9b5ba83dd26feba82541d8c86131bbbeaa95d92b10ca307a9a6766173d8`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, bundle, confined_path, entries, entry, link, links, mode, output, require, resolved, root, shutil, source, staging, stat, target. Outputs/bindings: entry, link, mode, output, resolved, source, target.
Calls/effect boundaries: (target.parent / link).resolve, Path, Path(link).is_absolute, bundle.open, bundle.read, bundle.read(entry).decode, confined_path, entry.filename.rstrip, entry.is_dir, links.append, require, resolved.is_relative_to, shutil.copyfileobj, staging.resolve, stat.S_ISLNK, target.chmod, target.exists, target.mkdir, target.open, target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[17].body[8].body[6]; no call, error or mutation may be omitted. Iteration: entry in entries
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:51`; AST `6da00933b992a5747167fc201426cfb24c1d6739215567bd4e22b2f96f3a8e67`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, entry, root, staging. Outputs/bindings: target.
Calls/effect boundaries: confined_path, entry.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:51`; AST `e31e73d217faf2e3486e3dd9bfda422a498d0846239c22fe399822a4e1ad5e93`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, entry, root, staging. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, entry.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[0].value.args[1].right::Call

Source: `scripts/roadmap_esbmc.py:51`; AST `84f639e63ecc1e000e85f68a145cbc718e587722ff3a6c7c860c5e9ebe7f0a2a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.filename.rstrip.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[0].value.args[1].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:52`; AST `e33d93045a27b310c04c752ec0ca8dcd0754f285df750fd77b508752a7d201b8`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: mode.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[6].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2]::If

Source: `scripts/roadmap_esbmc.py:53`; AST `b670035111fa7405203c9072a2af19a4a4e6f5d900fd5b1b0cb7b8dd24c99ca6`.

Rust module: `scripts::roadmap_esbmc`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: Path, bundle, entry, link, links, mode, output, require, resolved, shutil, source, staging, stat, target. Outputs/bindings: link, output, resolved, source.
Calls/effect boundaries: (target.parent / link).resolve, Path, Path(link).is_absolute, bundle.open, bundle.read, bundle.read(entry).decode, entry.is_dir, links.append, require, resolved.is_relative_to, shutil.copyfileobj, staging.resolve, stat.S_ISLNK, target.chmod, target.exists, target.mkdir, target.open, target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered If evaluation at root.body[17].body[8].body[6].body[2]; no call, error or mutation may be omitted. Condition: stat.S_ISLNK(mode)
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].test::Call

Source: `scripts/roadmap_esbmc.py:53`; AST `c974c1009351e37b4435517e766640d341ef2b1468bf11c4b828eed33fd40bf2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mode, stat. Outputs/bindings: (none).
Calls/effect boundaries: stat.S_ISLNK.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:54`; AST `c6cf5a25a6b96ef718e53b149e80be4922fcbfd3a61edea7fb92a64b722985eb`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bundle, entry. Outputs/bindings: link.
Calls/effect boundaries: bundle.read, bundle.read(entry).decode.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[6].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:54`; AST `1f3669fcb4eb6a0795d4f4004b7ad2de862f82e72076978966e0e3e6611f6002`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bundle, entry. Outputs/bindings: (none).
Calls/effect boundaries: bundle.read, bundle.read(entry).decode.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[0].value.func.value::Call

Source: `scripts/roadmap_esbmc.py:54`; AST `ce15f36b02851c3c4b3931b8fe50a2b384466e335317457af52e2d92bd001d61`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bundle, entry. Outputs/bindings: (none).
Calls/effect boundaries: bundle.read.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[1]::Expr

Source: `scripts/roadmap_esbmc.py:55`; AST `af6692f93f77655c7453b1739f3c30fa78bb58ad99aaf03b452c4f13a700d023`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, link, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(link).is_absolute, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:55`; AST `66646666973c7a86139a9e014beac918081890bce0719d51910d88066deb2716`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, link, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(link).is_absolute, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[1].value.args[0].values[1].operand::Call

Source: `scripts/roadmap_esbmc.py:55`; AST `f6184665ef642de13f2e5eaf20de91dfdfd26bc3f48c9c1e0d57db8ce7f39a10`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, link. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(link).is_absolute.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[1].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[1].value.args[0].values[1].operand.func.value::Call

Source: `scripts/roadmap_esbmc.py:55`; AST `4d649ba52f690e71c9914dd1be7034b5a70c8167b8ec699c75aa4d3a486db6ca`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, link. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[1].value.args[0].values[1].operand.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[2]::Assign

Source: `scripts/roadmap_esbmc.py:57`; AST `402687923d9a54599a8c474c7dd6090d6c9eda41f3074b506fdef303d98f7f7a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, target. Outputs/bindings: resolved.
Calls/effect boundaries: (target.parent / link).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[8].body[6].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:57`; AST `3a8b6bc3b939a76f7687e32008602062d5e93b10373a5fc1bd47a41108d358b3`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, target. Outputs/bindings: (none).
Calls/effect boundaries: (target.parent / link).resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[3]::Expr

Source: `scripts/roadmap_esbmc.py:58`; AST `b5582696e809c7c83730ad6c37b0f554b950c9d70ccc1c8a6cd4b7c82569608b`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, resolved, staging. Outputs/bindings: (none).
Calls/effect boundaries: require, resolved.is_relative_to, staging.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:58`; AST `edbab9048425c95a3e6f72023b8b54f556f7bdcd7741715b2cffd433ea8cead5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, resolved, staging. Outputs/bindings: (none).
Calls/effect boundaries: require, resolved.is_relative_to, staging.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[3].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:58`; AST `968f6f99d6000eb15d3c0d42e9db95b872f038fcaec11589b93a0f8902bce5e8`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: resolved, staging. Outputs/bindings: (none).
Calls/effect boundaries: resolved.is_relative_to, staging.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[3].value.args[0].args[0]::Call

Source: `scripts/roadmap_esbmc.py:58`; AST `f22c8dbf16f99e2227e852344816a1a4fa6336fc98361f98b639f0d9c6fa6141`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[3].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:59`; AST `03d0c97731d58b890f7b7b37cfadd09eafd750c43ac5c2cb235d31e552c48da7`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, links, target. Outputs/bindings: (none).
Calls/effect boundaries: links.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:59`; AST `df0a664334000a2cd9978f0618b5196000ba4ae801d99f245040859b8d9ff75a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, links, target. Outputs/bindings: (none).
Calls/effect boundaries: links.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0]::If

Source: `scripts/roadmap_esbmc.py:60`; AST `57080ce42e3b6743478fa89e9311aa668d09231a04562f1fca558f343f5d9081`.

Rust module: `scripts::roadmap_esbmc`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: bundle, entry, mode, output, require, shutil, source, target. Outputs/bindings: output, source.
Calls/effect boundaries: bundle.open, entry.is_dir, require, shutil.copyfileobj, target.chmod, target.exists, target.mkdir, target.open, target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered If evaluation at root.body[17].body[8].body[6].body[2].orelse[0]; no call, error or mutation may be omitted. Condition: entry.is_dir()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].test::Call

Source: `scripts/roadmap_esbmc.py:60`; AST `e1244ebd1e4aa3eb201413f9dfd27b72e00d838cdfcafff0bab5bff124e1dd8c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.is_dir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:61`; AST `d34c6606ece44ad913b4d9c5164fe1079105a1a417b61dbf9e377bde614033a3`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:61`; AST `15ec769ff3f6e9332492e8188860c7f62a832048191c440ba425d52a93395714`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[0]::Expr

Source: `scripts/roadmap_esbmc.py:63`; AST `e28cb5b2a9367313ba3b6470f9081a2b8186dd82dbfeec416a8d5f23d955b886`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[0].value::Call

Source: `scripts/roadmap_esbmc.py:63`; AST `58c379428a4dcb05097164e1e9cd0aa827bbb5a613fe07fceba4b6c0e390d1c9`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[1]::Expr

Source: `scripts/roadmap_esbmc.py:64`; AST `dc467eba18627f711cf37e45273a85980d5c3e5af99b1a58df0778a3e1008792`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[1].value::Call

Source: `scripts/roadmap_esbmc.py:64`; AST `135cc8abe7b8031e089890e22b0b974d10166e848ddffae423aa704a4d365b22`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[1].value.args[0].operand::Call

Source: `scripts/roadmap_esbmc.py:64`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[1].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[2]::With

Source: `scripts/roadmap_esbmc.py:65`; AST `a1b686e279deb0d1fbc6d1cd248e266c87f4a4c230d938604a3b5ab9320d11cb`.

Rust module: `scripts::roadmap_esbmc`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: bundle, entry, output, shutil, source, target. Outputs/bindings: output, source.
Calls/effect boundaries: bundle.open, shutil.copyfileobj, target.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered With evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].items[0].context_expr::Call

Source: `scripts/roadmap_esbmc.py:65`; AST `66828300b90494173ba6b74df16b85294f3dee9aa3bbf23b6e1249ae0e42c7a6`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bundle, entry. Outputs/bindings: (none).
Calls/effect boundaries: bundle.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].items[1].context_expr::Call

Source: `scripts/roadmap_esbmc.py:65`; AST `b45f72198138ac049f17d7ed9f3b48a02f547eaaef84e9a6f0bb6f0cfcccb732`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.open.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:66`; AST `e86f79a3ed3175b25182523bdde944080b620026f83e2a67875fdee03259381d`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: output, shutil, source. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfileobj.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:66`; AST `900c47f8d854ffc2af45e399572f58780da437b7a7e4c4361fa20d38a86d279c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: output, shutil, source. Outputs/bindings: (none).
Calls/effect boundaries: shutil.copyfileobj.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[3]::Expr

Source: `scripts/roadmap_esbmc.py:67`; AST `a81510f4573445e6f8d3013314d1171ede91a9d0fb60a1b0a79ade1fe5cc73d5`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: mode, target. Outputs/bindings: (none).
Calls/effect boundaries: target.chmod.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[8].body[6].body[2].orelse[0].orelse[3].value::Call

Source: `scripts/roadmap_esbmc.py:67`; AST `0346ba384d6f7c110f13c00e4637f3e2cae32dc0d1725bccab45a90fe14b538c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: mode, target. Outputs/bindings: (none).
Calls/effect boundaries: target.chmod.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].body[6].body[2].orelse[0].orelse[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9]::For

Source: `scripts/roadmap_esbmc.py:68`; AST `3f2559c15bdc82e3359c32ef588ad5d458dffb43c02e892a13872fb1c2d936c6`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: link, links, require, target. Outputs/bindings: link, target.
Calls/effect boundaries: require, target.exists, target.is_symlink, target.parent.mkdir, target.symlink_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[17].body[9]; no call, error or mutation may be omitted. Iteration: (target, link) in links
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:69`; AST `26a3a499b9e9f25d91e0145f2201956c9b18e7cd102537185b77146a703d584c`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists, target.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:69`; AST `0a375206843e3858ed0e84012cfaa894bc394632387fafaae1c6d166ff910142`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists, target.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[0].value.args[0].values[0].operand::Call

Source: `scripts/roadmap_esbmc.py:69`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[0].value.args[0].values[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[0].value.args[0].values[1].operand::Call

Source: `scripts/roadmap_esbmc.py:69`; AST `01c0e3a8d7aebaddf3e9b2d9e17ff265070a833cdc5a5af1ae3c979a7a4eb2f3`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[0].value.args[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[1]::Expr

Source: `scripts/roadmap_esbmc.py:70`; AST `e28cb5b2a9367313ba3b6470f9081a2b8186dd82dbfeec416a8d5f23d955b886`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:70`; AST `58c379428a4dcb05097164e1e9cd0aa827bbb5a613fe07fceba4b6c0e390d1c9`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.parent.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:71`; AST `e68b356cda68ca434f538499f31426760de049322d5731a51006469b8564168a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: link, target. Outputs/bindings: (none).
Calls/effect boundaries: target.symlink_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[9].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:71`; AST `97ed6bd6dcaf619dcc461a1d0b5b9799b1e1d4211b521f8378b92bc90e5c9a8a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: link, target. Outputs/bindings: (none).
Calls/effect boundaries: target.symlink_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10]::For

Source: `scripts/roadmap_esbmc.py:72`; AST `c46b4b0a1785594202ee8a79c3a17ddc1aea6d3551218793607317dac5655d29`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: links, require, staging, target. Outputs/bindings: _, target.
Calls/effect boundaries: require, staging.resolve, target.exists, target.resolve, target.resolve().is_relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[17].body[10]; no call, error or mutation may be omitted. Iteration: (target, _) in links
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:73`; AST `0dab9291a8ef337d152e82beb285a18eb127e576d5bcf13ab3fa610389e373ce`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, staging, target. Outputs/bindings: (none).
Calls/effect boundaries: require, staging.resolve, target.exists, target.resolve, target.resolve().is_relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:73`; AST `90b7068e874d4994aa72d7420034f0499abbbdf602e7790d214c39273ce5da1d`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, staging, target. Outputs/bindings: (none).
Calls/effect boundaries: require, staging.resolve, target.exists, target.resolve, target.resolve().is_relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0].value.args[0].values[0]::Call

Source: `scripts/roadmap_esbmc.py:73`; AST `2d9d947e8231dafd0d65eff5fce75bf28ef3894086cc42495b973ec196f241da`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: staging, target. Outputs/bindings: (none).
Calls/effect boundaries: staging.resolve, target.resolve, target.resolve().is_relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0].value.args[0].values[0].func.value::Call

Source: `scripts/roadmap_esbmc.py:73`; AST `5e1a6e165527bbdae5b20232e40a8e9fe4ed322b004cf30b48c6934c7fd84da5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value.args[0].values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0].value.args[0].values[0].args[0]::Call

Source: `scripts/roadmap_esbmc.py:73`; AST `f22c8dbf16f99e2227e852344816a1a4fa6336fc98361f98b639f0d9c6fa6141`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.resolve.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value.args[0].values[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[10].body[0].value.args[0].values[1]::Call

Source: `scripts/roadmap_esbmc.py:73`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[10].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[11]::Expr

Source: `scripts/roadmap_esbmc.py:74`; AST `9e22833a45af81e7656d6193a9d1ba1f56b1800b13200ebf3ca6700ca1b606d0`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.rename.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[11].value::Call

Source: `scripts/roadmap_esbmc.py:74`; AST `ddcb3682da75f8df2aa28e3e330805cf0573f51abd0762bb38e45595281fe4a6`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, staging. Outputs/bindings: (none).
Calls/effect boundaries: staging.rename.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12]::Assign

Source: `scripts/roadmap_esbmc.py:75`; AST `4d5f0a4227770a7da26e9bef750f7caf42574f3be9df2364d05d7747a7027e03`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, file_binding, p, root. Outputs/bindings: files, p.
Calls/effect boundaries: destination.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value::ListComp

Source: `scripts/roadmap_esbmc.py:75`; AST `48c8f77a14f311a8974796332aec817354ce08e38ca60e0b2aa07b71b94dfe88`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: destination, file_binding, p, root. Outputs/bindings: p.
Calls/effect boundaries: destination.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[12].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.elt::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `eb79f32bd6462ca7c8c36dc6e41d01e5b8e63c36372e4a980ce6e1c1502388a6`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, p, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.elt.args[1]::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.elt.args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.generators[0].iter::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `eb71d9ae83a6efb14d33dd0c3033af2a13e9f6dca44142c9411aa94220df40a7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination. Outputs/bindings: (none).
Calls/effect boundaries: destination.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[12].value.generators[0].ifs[0].values[1].operand::Call

Source: `scripts/roadmap_esbmc.py:75`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[12].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[13]::Assign

Source: `scripts/roadmap_esbmc.py:76`; AST `69c1f55a9d141544da09ec535c961c6474066b61a23e877df47e403177b19666`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: destination, link, links, p, root, staging. Outputs/bindings: link, p, symlinks.
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, (destination / p.relative_to(staging)).relative_to(root).as_posix, p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[13].value::ListComp

Source: `scripts/roadmap_esbmc.py:76`; AST `d43e8e62a0aee58595719ac616897a645d3db9e4a50a33ae701248d984a8fc1e`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: destination, link, links, p, root, staging. Outputs/bindings: link, p.
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, (destination / p.relative_to(staging)).relative_to(root).as_posix, p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[17].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[13].value.elt.values[0]::Call

Source: `scripts/roadmap_esbmc.py:76`; AST `9d1928f32d0534246344e512ceaea7fe963a32c115230b859d29dd6fa31fb7b4`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, p, root, staging. Outputs/bindings: (none).
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, (destination / p.relative_to(staging)).relative_to(root).as_posix, p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.elt.values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[13].value.elt.values[0].func.value::Call

Source: `scripts/roadmap_esbmc.py:76`; AST `c3098fab8f637b4f33652d9961bda7927011f9169cba16a230f253b4cfad9540`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: destination, p, root, staging. Outputs/bindings: (none).
Calls/effect boundaries: (destination / p.relative_to(staging)).relative_to, p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.elt.values[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[13].value.elt.values[0].func.value.func.value.right::Call

Source: `scripts/roadmap_esbmc.py:76`; AST `ba369c8faf6942e376387393dbd7905bec564ad7215689250919f92e122d8ed5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, staging. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[13].value.elt.values[0].func.value.func.value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[14]::Expr

Source: `scripts/roadmap_esbmc.py:77`; AST `547a11b949a8185c89315dc62423c756b663e23a0eb3cd2dc627f1900b091bd0`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive_binding, atomic_write_json, b, files, marker, root, sorted, symlinks. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[14].value::Call

Source: `scripts/roadmap_esbmc.py:77`; AST `2533606ab0d1e6868cfe7b9f5957b2644610b5f4bdd67fadf13b1822423599ff`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive_binding, atomic_write_json, b, files, marker, root, sorted, symlinks. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[14].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[14].value.args[1].values[2]::Call

Source: `scripts/roadmap_esbmc.py:77`; AST `a5616fd6a71280cc0021ec98e0e0aa0aaf2df557f2242b1ce25a206fc8069837`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[17].body[14].value.args[1].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::extract_release::root.body[17].body[14].value.args[1].values[2].keywords[0].value::Lambda

Source: `scripts/roadmap_esbmc.py:77`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `scripts::roadmap_esbmc`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Lambda evaluation at root.body[17].body[14].value.args[1].values[2].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18]::FunctionDef

Source: `scripts/roadmap_esbmc.py:81`; AST `09bb33ffc3c26b0b4ef0f0fe92990d18800c44933fc1d39eae118c2b9e3f6012`.

Rust module: `scripts::roadmap_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, TRANSPORT, archive, argv, artifacts, asdict, atomic_write_json, b, confined_path, deadline, dict, digest, directory, download_with_mirrors, environment, executables, extract_release, file_binding, files, identity, len, lock, map, minimal_subprocess_env, name, os, output, p, path, profile, python, read_download_policy, read_json, release, require, result, root, run_recipe_stage, sorted, str, sys, time, venv, virtual, wheels. Outputs/bindings: archive, argv, artifacts, deadline, directory, environment, executables, files, identity, lock, name, p, path, profile, python, release, result, virtual, wheels.
Calls/effect boundaries: (virtual / 'bin/python').exists, artifacts.append, asdict, atomic_write_json, confined_path, dict, digest, directory.mkdir, directory.rglob, download_with_mirrors, extract_release, file_binding, len, lock.get, map, minimal_subprocess_env, os.access, os.uname, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix, path.relative_to, path.relative_to(root).as_posix, read_download_policy, read_json, release.relative_to, release.relative_to(root).as_posix, release.rglob, require, run_recipe_stage, sorted, str, time.monotonic, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:82`; AST `7c3b275630ec4c1b2d9ee05b84db582b3a33fe6f1df21fe14bedc193a521242a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: profile.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:83`; AST `7aecf23f5d65b5be9f380a1a662abcf9abfce99ab389cd2ea6066f6663437a44`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: profile, read_json, root. Outputs/bindings: lock.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:83`; AST `6fd2eb6d22afaa8b938ef1733d08c0a4e3d0f1703f57a7ba8d12fd1d75c03749`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: profile, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:84`; AST `777bfc4db4195430621ea52786294916efca1ae981647542954e9ce04605b10e`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TRANSPORT, lock, os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:84`; AST `b077d8fd3d406cea6e52e0452174da871380e2e734ee6fa93b624efb500af030`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: TRANSPORT, lock, os, require, sys. Outputs/bindings: (none).
Calls/effect boundaries: lock.get, os.uname, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[2].value.args[0].values[0].left::Call

Source: `scripts/roadmap_esbmc.py:84`; AST `391afc41ac06cfbbb7183fbada92250cec99cb0f89877d6370006cc407c99917`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[2].value.args[0].values[1].left::Call

Source: `scripts/roadmap_esbmc.py:84`; AST `0f5caa8d721fa57ccd111022f4dd4a6cb35818790520adfc04f1aa7246c5f0d0`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lock. Outputs/bindings: (none).
Calls/effect boundaries: lock.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[2].value.args[0].values[3].left.value::Call

Source: `scripts/roadmap_esbmc.py:85`; AST `3870b6eca1eb32f0495f3ce63519015697c5abaab1b7c0cd315823eb5f223d84`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.uname.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[2].value.args[0].values[3].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:86`; AST `b003f2657cfef918d715f10cb5c6b64e9afaee684cdebfb7a2105c8418a3713e`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, digest, lock, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:86`; AST `16a57f49f7d32860b2f2139e1b0ff6a79ac9b49e68e3a1e6eb13e59c224d0d3c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, digest, lock, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[3].value.args[1].right::Call

Source: `scripts/roadmap_esbmc.py:86`; AST `5bc6a77705554ea369323608f0973231236c18cf659990724b2fdbdbb8e7067e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, lock. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[3].value.args[1].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:87`; AST `3a400253aadde423a42d9e21da0e9ba55a3fe64614ae692874cebc9a5aa91183`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:87`; AST `7f8492ad27b11def9f8bffa8aea0180c657a9152ccc4f6a4269a7601584575c2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[5]::Assign

Source: `scripts/roadmap_esbmc.py:88`; AST `4bf1f8e6c36f98f38e92ec4bca5e754fb5c2256335263ba3ca08b43b415056ba`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_download_policy, root, time. Outputs/bindings: deadline.
Calls/effect boundaries: read_download_policy, time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[5].value.left::Call

Source: `scripts/roadmap_esbmc.py:88`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[5].value.right.value::Call

Source: `scripts/roadmap_esbmc.py:88`; AST `d98a9d8f02719fd4afc66431e19bae5e085c1a1947d40c1d0c9c099b5cc2ace2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_download_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_download_policy.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[5].value.right.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[6]::Assign

Source: `scripts/roadmap_esbmc.py:89`; AST `8794258d17ac7024e6cf93a636f8891f9bfc9ccc2f56ad422a0b02ece9aa331a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, directory, download_with_mirrors, lock, p, root. Outputs/bindings: p, wheels.
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[6].value::ListComp

Source: `scripts/roadmap_esbmc.py:89`; AST `24316a0c9272154a3a75f9eb57ead1c329c8de944bfb67c2e6bd1899eb13d7b5`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: deadline, directory, download_with_mirrors, lock, p, root. Outputs/bindings: p.
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[6].value.elt::Call

Source: `scripts/roadmap_esbmc.py:89`; AST `db1bfa8bc8cafbbb207e39e122992c92a389799a9a498924c0d9d2d923eae03d`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, directory, download_with_mirrors, p, root. Outputs/bindings: (none).
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[6].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[7]::Assign

Source: `scripts/roadmap_esbmc.py:90`; AST `3a20ff5b6a1419dd00022fcf08f5fe2370942c1205f409c1c1fcccd2c5d1e159`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, directory, download_with_mirrors, lock, root. Outputs/bindings: archive.
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[7].value::Call

Source: `scripts/roadmap_esbmc.py:90`; AST `48f7e64c869d62107dbabee85f2ca8d650da29a1d45689859259435821691157`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, directory, download_with_mirrors, lock, root. Outputs/bindings: (none).
Calls/effect boundaries: download_with_mirrors.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[8]::Assign

Source: `scripts/roadmap_esbmc.py:91`; AST `b624d95071fe46fe036d209bccf9ea7d500c717c5347c4a50034ceae72473c37`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: release.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[9]::Expr

Source: `scripts/roadmap_esbmc.py:92`; AST `109f8260ad3194db00e36226d16a54fed8fa44fecf30a196a0200835d5939b4a`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: archive, extract_release, release, root. Outputs/bindings: (none).
Calls/effect boundaries: extract_release.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[9].value::Call

Source: `scripts/roadmap_esbmc.py:92`; AST `b24ec9c0c78e63ce83ab1c910b5d897af56061e2a214d3708ee018b797e5d4d8`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: archive, extract_release, release, root. Outputs/bindings: (none).
Calls/effect boundaries: extract_release.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[10]::Assign

Source: `scripts/roadmap_esbmc.py:93`; AST `42b53fc874e5e306cc01e4f06ea1418315f20e84930e89276b915eebd35f0a95`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os, p, release. Outputs/bindings: executables, p.
Calls/effect boundaries: os.access, p.is_file, release.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[10].value::ListComp

Source: `scripts/roadmap_esbmc.py:93`; AST `067a5757a933747c86cc36577a87865e15972dd9c66ae7cc06d44eb8c2f29ad1`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: os, p, release. Outputs/bindings: p.
Calls/effect boundaries: os.access, p.is_file, release.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[10].value.generators[0].iter::Call

Source: `scripts/roadmap_esbmc.py:93`; AST `518e914634ebf4d72a81ac36851310fc41f3d8285396506c05d8d81623d65508`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: release. Outputs/bindings: (none).
Calls/effect boundaries: release.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[10].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_esbmc.py:93`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[10].value.generators[0].ifs[0].values[1]::Call

Source: `scripts/roadmap_esbmc.py:93`; AST `51815cc075102faba3a795cf855f9a74ba80f9618a13b718817deb5398c0bf5a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os, p. Outputs/bindings: (none).
Calls/effect boundaries: os.access.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[10].value.generators[0].ifs[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[11]::Expr

Source: `scripts/roadmap_esbmc.py:94`; AST `a90838fec63643501d29928e39d15ee0a78cc6dbc5d9704dec3f864d2433a59c`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: executables, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[11].value::Call

Source: `scripts/roadmap_esbmc.py:94`; AST `7d162e866383b189a8e6e5b3f175d15ec3e93916a3f975865be368d045cbb5a7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executables, len, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[11].value.args[0].left::Call

Source: `scripts/roadmap_esbmc.py:94`; AST `3822129743b1057217850a6ea2eef06c7ecf5989e8d318190910316a6e9efef1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executables, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[11].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[12]::Assign

Source: `scripts/roadmap_esbmc.py:95`; AST `b2b20845ca3c33880841af77a8dbd450bfed5a844c0692cd30cff6f52380a646`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: virtual.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[13]::If

Source: `scripts/roadmap_esbmc.py:96`; AST `ef8a109a479ce8ff2656c8acccd7cfbf5d59f4dbf4a3026268220be20bb98214`.

Rust module: `scripts::roadmap_esbmc`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists, venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered If evaluation at root.body[18].body[13]; no call, error or mutation may be omitted. Condition: not (virtual / 'bin/python').exists()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[13].test.operand::Call

Source: `scripts/roadmap_esbmc.py:96`; AST `11bd605d4b8042dcd6fa6abc11a7f8cb4cad169d97c1b84a16d2d67a7e3620cc`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: virtual. Outputs/bindings: (none).
Calls/effect boundaries: (virtual / 'bin/python').exists.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].test.operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[13].body[0]::Expr

Source: `scripts/roadmap_esbmc.py:97`; AST `92c90ec98733d58f9e12e19512aca7cdb916986d543f7f7a77af60aa471b6937`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[13].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:97`; AST `9d8c6758a1dc49b67a4c2545e4ab0a411f7954299c88c80381698e340636c690`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv, virtual. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder, venv.EnvBuilder(with_pip=True).create.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[13].body[0].value.func.value::Call

Source: `scripts/roadmap_esbmc.py:97`; AST `c8c152ecb6c87d3d058f6bff59b9baee7727e29c264936c80874fedc8e1ce948`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: venv. Outputs/bindings: (none).
Calls/effect boundaries: venv.EnvBuilder.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[13].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[14]::Assign

Source: `scripts/roadmap_esbmc.py:98`; AST `43559ae3e722df57ae62c2fc9cf97a4fe964a0d51d8e984447c1c6f5697edad4`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: virtual. Outputs/bindings: python.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[15]::Assign

Source: `scripts/roadmap_esbmc.py:99`; AST `90741055731cbeff50b1bfc7ce711dd5785e69026a59df14f5d64d15e9ae2357`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, minimal_subprocess_env. Outputs/bindings: environment.
Calls/effect boundaries: dict, minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[15].value::Call

Source: `scripts/roadmap_esbmc.py:99`; AST `c5a0a6503fc8a5d3eacd42fdb4d780b2e8a2999d1aa5a4c4f797810639f816e5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: dict, minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[15].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[15].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:99`; AST `9e9061036bd9e328e720270b436538e3d5500df22e91a0d49a0d1cd8cd8d5695`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: minimal_subprocess_env. Outputs/bindings: (none).
Calls/effect boundaries: minimal_subprocess_env.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[15].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[16]::Assign

Source: `scripts/roadmap_esbmc.py:100`; AST `e73c528694ffe6c1c84fbb9c5ff044ae0c34a914494eadac59b06b6361649f86`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: artifacts.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17]::For

Source: `scripts/roadmap_esbmc.py:101`; AST `7f23e5e7af598115917e88da9772c3f57f83de1d33815d5d9c26553aab75d1c2`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: argv, artifacts, asdict, atomic_write_json, environment, executables, file_binding, map, name, output, path, python, require, result, root, run_recipe_stage, str, wheels. Outputs/bindings: argv, name, path, result.
Calls/effect boundaries: artifacts.append, asdict, atomic_write_json, file_binding, map, path.relative_to, path.relative_to(root).as_posix, require, run_recipe_stage, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[18].body[17]; no call, error or mutation may be omitted. Iteration: (name, argv) in (('pip-result.json', [str(python), '-B', '-m', 'pip', 'install', '--no-index', '--no-deps', *map(str, wheels)]), ('pip-check.json', [str(python), '-B', '-m', 'pip', 'check']), ('esbmc-version.json', [str(executables[0]), '--version']))
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].iter.elts[0].elts[1].elts[0]::Call

Source: `scripts/roadmap_esbmc.py:101`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].iter.elts[0].elts[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].iter.elts[0].elts[1].elts[7].value::Call

Source: `scripts/roadmap_esbmc.py:101`; AST `a89a4d10f15fcf45dcb987d9b119d10ddbaa50d5511754be6250fd2c6014f9a5`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: map, str, wheels. Outputs/bindings: (none).
Calls/effect boundaries: map.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].iter.elts[0].elts[1].elts[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].iter.elts[1].elts[1].elts[0]::Call

Source: `scripts/roadmap_esbmc.py:102`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].iter.elts[1].elts[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].iter.elts[2].elts[1].elts[0]::Call

Source: `scripts/roadmap_esbmc.py:103`; AST `1f856c531b3aa8b9f735ec74128bccf190a5a3942aac63682f462c4661aba0e4`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executables, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].iter.elts[2].elts[1].elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:104`; AST `f802c75c13444cf33fce4ad0ed80bf5ebea0a9cbda411ba7a80ff595533d76b8`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: argv, environment, root, run_recipe_stage. Outputs/bindings: result.
Calls/effect boundaries: run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:104`; AST `bac19288464b2af15e29ca4705aaea6181d029c19012982d97b42b281688e44d`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: argv, environment, root, run_recipe_stage. Outputs/bindings: (none).
Calls/effect boundaries: run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:105`; AST `ac0bc25cee3c3769a8aa769d7aba83147b4f929c077f08642b3fd8ead84b76a2`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:106`; AST `bdf64811b95b939af6ea7eee41b9e91eea1f56f98d54e9f689f3d30d19491963`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:106`; AST `4298a9f4fcb2b3067e14867dbddab90daed2957656839048e079cfe3c3b3ef03`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[2].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:106`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[3]::Expr

Source: `scripts/roadmap_esbmc.py:107`; AST `2fc28c9d3bb8691ddc6e6a5a99873506f698d9fc5ca9b29c6b631fd7fb891e85`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append, file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:107`; AST `efeb05caed238acf36201da7b921c24980b7cc5422c0ec64affe731fbca1892e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append, file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[3].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:107`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[3].value.args[0].args[1]::Call

Source: `scripts/roadmap_esbmc.py:107`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[3].value.args[0].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[3].value.args[0].args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:107`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[3].value.args[0].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:108`; AST `ec9f351622a5699665c86e691a79fe2066281b210e420ae8dd132505415ee862`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[17].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:108`; AST `0b1571d7399c21bfdf41f203921a8ded91da31f564337ffac1cf37ab55fab70a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, result. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[17].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18]::Assign

Source: `scripts/roadmap_esbmc.py:110`; AST `1cbbac69aff269a10d9ffd430fa4d7d8d712dfe64169e614609a90f04d918b5d`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory, file_binding, p, root. Outputs/bindings: files, p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value::ListComp

Source: `scripts/roadmap_esbmc.py:110`; AST `24b9656771e727034dde025d62ba4150c889c9fca7fc388c6617099dac654b23`.

Rust module: `scripts::roadmap_esbmc`. iterator pipeline collected into Vec; preserve evaluation order and comprehension-local scope

Inputs: directory, file_binding, p, root. Outputs/bindings: p.
Calls/effect boundaries: directory.rglob, file_binding, p.is_file, p.is_symlink, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered ListComp evaluation at root.body[18].body[18].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.elt::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `eb79f32bd6462ca7c8c36dc6e41d01e5b8e63c36372e4a980ce6e1c1502388a6`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, p, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.elt.args[1]::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `e5edcd6b200205e2fc0e53b73f283275768b68b00541e7340a68a6790ede5a16`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to, p.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.elt.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.elt.args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `104da8a083f29e3a4bb917346795d093732c1321160619fe967702ce846a3e35`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p, root. Outputs/bindings: (none).
Calls/effect boundaries: p.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.elt.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.generators[0].iter::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `41d06ab308b2a9f6afc10dd35a5e6c7ba671d5befff73c0a5a1caa71363e86d7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.rglob.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.generators[0].ifs[0].values[0]::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `e0594c8f8595272c6b5ea9423cbfc33970f76cb3832fbbde2b4a35e386807838`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_file.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.generators[0].ifs[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[18].value.generators[0].ifs[0].values[1].operand::Call

Source: `scripts/roadmap_esbmc.py:110`; AST `e9cab480c97fe5effaf0b2cd191d671f332cea8d0957cd0f4ecd6d4870d0f0db`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: p. Outputs/bindings: (none).
Calls/effect boundaries: p.is_symlink.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[18].value.generators[0].ifs[0].values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[19]::Assign

Source: `scripts/roadmap_esbmc.py:111`; AST `8ee217fba87c89a169340aa63e1aa3752023eba88d8c89bb1a603527c3bdaffe`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_json, release. Outputs/bindings: identity.
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[19].value::Call

Source: `scripts/roadmap_esbmc.py:111`; AST `59f40861c9e0cb2f534aba1b09778d05b3d71a14bacd3bd1d7a3c7fbeaf1760c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_json, release. Outputs/bindings: (none).
Calls/effect boundaries: read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[19].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20]::Return

Source: `scripts/roadmap_esbmc.py:112`; AST `409bac9a0ea1fc845eaa0cbcfcb45618b65a7e74850f74ccd488eb3be45d640d`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, b, environment, executables, file_binding, files, identity, profile, python, release, root, sorted, str. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, release.relative_to, release.relative_to(root).as_posix, sorted, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[18].body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[2]::Call

Source: `scripts/roadmap_esbmc.py:112`; AST `bbac3d3e2068529355b1ab743fb0e27184efd487afe79aa051c725805e327339`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, profile, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[3]::Call

Source: `scripts/roadmap_esbmc.py:113`; AST `b6922cde8c2e7104d6243299f4ef4e3b049733ba31ce3fdcc0b5be147a02c002`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: python, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[4]::Call

Source: `scripts/roadmap_esbmc.py:113`; AST `1f856c531b3aa8b9f735ec74128bccf190a5a3942aac63682f462c4661aba0e4`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: executables, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[6]::Call

Source: `scripts/roadmap_esbmc.py:114`; AST `a5616fd6a71280cc0021ec98e0e0aa0aaf2df557f2242b1ce25a206fc8069837`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: b, files, sorted. Outputs/bindings: (none).
Calls/effect boundaries: sorted.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[6].keywords[0].value::Lambda

Source: `scripts/roadmap_esbmc.py:114`; AST `10552bb4b453c48baad30da0d42657f44c1f0b25d33ce1f7c87527d13f5dd537`.

Rust module: `scripts::roadmap_esbmc`. closure with explicit captures; preserve Python late binding and argument defaults

Inputs: b. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Lambda evaluation at root.body[18].body[20].value.values[6].keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[8]::Call

Source: `scripts/roadmap_esbmc.py:115`; AST `50f5267faa043c01780d9591b514e32b0bba7e00ff126dc8353526f8888938f7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: release, root. Outputs/bindings: (none).
Calls/effect boundaries: release.relative_to, release.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::provision_esbmc::root.body[18].body[20].value.values[8].func.value::Call

Source: `scripts/roadmap_esbmc.py:115`; AST `ca964476f0bd72daee80f6d71c2e54700ccad7e7a046a889d82422a997a65d19`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: release, root. Outputs/bindings: (none).
Calls/effect boundaries: release.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[18].body[20].value.values[8].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19]::FunctionDef

Source: `scripts/roadmap_esbmc.py:118`; AST `372c66e36c584e5b2ed252d9c0fe1dac8277ae9919f8ecca2f1f8b3811368db2`.

Rust module: `scripts::roadmap_esbmc`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, all, artifacts, asdict, atomic_write_json, binding, bindings_current, claims, claims_binding, claims_path, classification, classify_esbmc, confined_path, dict, environment, esbmc_arguments, esbmc_link_state, file_binding, fixture, name, output, path, read_json, require, result, result_binding, root, run_recipe_stage, runs, source_closure, str, toolchain, toolchain_path, x. Outputs/bindings: artifacts, binding, claims, claims_binding, claims_path, classification, environment, fixture, name, path, result, result_binding, runs, toolchain, x.
Calls/effect boundaries: all, artifacts.append, artifacts.extend, asdict, atomic_write_json, bindings_current, claims_path.relative_to, claims_path.relative_to(root).as_posix, classify_esbmc, confined_path, dict, esbmc_arguments, esbmc_link_state, file_binding, path.relative_to, path.relative_to(root).as_posix, read_json, require, run_recipe_stage, runs.append, source_closure, str, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:119`; AST `9c4ed075341df239cefc71fc85e737c489c52b1edf0734eae30e1f6ed63824be`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, root, toolchain_path. Outputs/bindings: binding.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:119`; AST `d1ab105f67a191a692ccfa7349ad4ff83b44f59a053df2c13003cd86b60ff40f`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:120`; AST `306834594d91496c2087b429d7388547edeb1770e5e25cd42ecffc9433459f0e`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: toolchain.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:120`; AST `cef1490a0865a886283dc1abfdd972486c9964aa9e05ad3933980f4f22e59e83`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, read_json, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[1].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:120`; AST `224b2b021d2f344194abcb6afa9f4b3ede25cf388cb616010c2eade7e5ad9cbc`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, root, toolchain_path. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:121`; AST `11e95250aff7705ca6594a9007157098c26d2b231d6f2274969c62d22e9026b4`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:121`; AST `3a2aa44ee415db52838d8c5938b6c844a304b0bd072e9bb26f4a824e328bbf75`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, require, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current, require, toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[2].value.args[0].values[0].left::Call

Source: `scripts/roadmap_esbmc.py:121`; AST `a1570292a8fc75ba5ee5d3c375d6190adbc55c1d07ea99d6aa2674ae094cc85b`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[2].value.args[0].values[1].left::Call

Source: `scripts/roadmap_esbmc.py:121`; AST `d80367ddfb01184b29a244b9798c54812da40b621eb6b5ee31d30a9dcc39ffde`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: toolchain. Outputs/bindings: (none).
Calls/effect boundaries: toolchain.get.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[2].value.args[0].values[2]::Call

Source: `scripts/roadmap_esbmc.py:122`; AST `eaa22374d32a9f53d86375fd8b957817f509b6715f81bf2b7cf491a514306a1c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: bindings_current, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: bindings_current.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[3]::Expr

Source: `scripts/roadmap_esbmc.py:123`; AST `f9374eca3ef00e6465c1d1b94a33d368f433d9c123178c6386e98c78fa399067`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, esbmc_link_state, require, root, toolchain, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:123`; AST `01cbb31dfd595a08e946a862b24046060a53c55534a61eb9a0e6560a2db16331`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, esbmc_link_state, require, root, toolchain, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state, require.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[3].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:123`; AST `b3d433f315ed26cf05a3280d7731bb42ce31b50d054c6c784d6d93a168a0aa34`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, esbmc_link_state, root, toolchain, x. Outputs/bindings: x.
Calls/effect boundaries: all, esbmc_link_state.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[3].value.args[0].args[0]::GeneratorExp

Source: `scripts/roadmap_esbmc.py:123`; AST `7519af78edb4821230d9d546fd11c46ba4708fd8b09b20a8c0b38c3a5a3a757b`.

Rust module: `scripts::roadmap_esbmc`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: esbmc_link_state, root, toolchain, x. Outputs/bindings: x.
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[19].body[3].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[3].value.args[0].args[0].generators[0].iter::Call

Source: `scripts/roadmap_esbmc.py:123`; AST `6caf4c0f92348aaea382c6864abe507af9c6c282c9bd22dca6778235e5997fd7`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_link_state, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_link_state.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value.args[0].args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[4]::Assign

Source: `scripts/roadmap_esbmc.py:124`; AST `17b32c4c49775e968c12298fd4b6e8bd96e47be5f177cdce50ea94c7faa0c167`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: artifacts, runs.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5]::For

Source: `scripts/roadmap_esbmc.py:125`; AST `41525a465a3bd42f33ebd381550c517b0dfc64d788d3aab0298863b5c041aeff`.

Rust module: `scripts::roadmap_esbmc`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: artifacts, asdict, atomic_write_json, claims, claims_binding, claims_path, classification, classify_esbmc, dict, environment, esbmc_arguments, file_binding, fixture, name, output, path, result, result_binding, root, run_recipe_stage, runs, str, toolchain. Outputs/bindings: claims, claims_binding, claims_path, classification, environment, fixture, name, path, result, result_binding.
Calls/effect boundaries: artifacts.append, artifacts.extend, asdict, atomic_write_json, claims_path.relative_to, claims_path.relative_to(root).as_posix, classify_esbmc, dict, esbmc_arguments, file_binding, path.relative_to, path.relative_to(root).as_posix, run_recipe_stage, runs.append, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered For evaluation at root.body[19].body[5]; no call, error or mutation may be omitted. Iteration: name in ('policy_deal_positive.py', 'policy_deal_negative.py')
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:126`; AST `7077b03c695e271045a9bb384fbd97125542515450b2a10511862a77efb2b403`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, name, root. Outputs/bindings: fixture.
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:126`; AST `b0a7348dff571b978183e11d8fd0eca126d3a255189c19f890c1933cf16fc626`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, name, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:127`; AST `9347fa70e47d26b03dbcee0c7d1745424cd50b1bf09c8caddaa0eead93f4d9ee`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: dict, root, str, toolchain. Outputs/bindings: environment.
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[1].value::Call

Source: `scripts/roadmap_esbmc.py:127`; AST `16088de01e02bae46fa5180a27baf07590f959a32d214ff60c7ad8a91f216506`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, root, str, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: dict, str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[1].value.keywords[0].value::Call

Source: `scripts/roadmap_esbmc.py:127`; AST `5e78564dad6f72b4fffe70a2682a87198ad49cb6d6eea55e10061b531d18c330`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[1].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[2]::Assign

Source: `scripts/roadmap_esbmc.py:128`; AST `6144affb80332bf78e80950fa04e24e840acd268e2a11569630f6fbf56c7ffb6`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, esbmc_arguments, fixture, root, run_recipe_stage, toolchain. Outputs/bindings: result.
Calls/effect boundaries: esbmc_arguments, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:128`; AST `3f804339ac2c71b5b0c1977c633d81f6d1ac3fd286856de43049dda77ad275ce`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, esbmc_arguments, fixture, root, run_recipe_stage, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[2].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:128`; AST `44d0bf8e0e4eebdd7de6f0bafd3d8fa55d9abeb4397b9fd0845f1e23e6ea77f9`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_arguments, fixture, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[2].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:130`; AST `7d6b3db36765b8decb82be54bc601c54ceac2d8db3d18be6872fac671a2fcd6d`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:131`; AST `bdf64811b95b939af6ea7eee41b9e91eea1f56f98d54e9f689f3d30d19491963`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:131`; AST `4298a9f4fcb2b3067e14867dbddab90daed2957656839048e079cfe3c3b3ef03`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, path, result, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[4].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:131`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[4].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[5]::Assign

Source: `scripts/roadmap_esbmc.py:132`; AST `8dae720bb64e7fa4c3505e5f110602aecc84a3a625305353b85ccdab266aafc6`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, path, root. Outputs/bindings: result_binding.
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[5].value::Call

Source: `scripts/roadmap_esbmc.py:132`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[5].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:132`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[5].value.args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:132`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[5].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[6]::Expr

Source: `scripts/roadmap_esbmc.py:133`; AST `dfa305053b321c11df57efae8ad1ebf0c7e6c45daa1adb4c9f55da326f6a6a10`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, fixture, result_binding. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.extend.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[6].value::Call

Source: `scripts/roadmap_esbmc.py:133`; AST `00d84d7f5a8c43f808a5e99b6034aa77a4f127d6b57954aa3b2d469c5a64d16e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, fixture, result_binding. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.extend.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[7]::Assign

Source: `scripts/roadmap_esbmc.py:134`; AST `d4167a724c17c64db47b1fb8f8405a261740144281694ee6cb6564c6373e1fbf`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, classify_esbmc, result. Outputs/bindings: classification.
Calls/effect boundaries: asdict, classify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[7].value::Call

Source: `scripts/roadmap_esbmc.py:134`; AST `3fc7ddf025338d866f23debf3c78eacd88e64e90ff35fea0c7631b5d10b16e06`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, classify_esbmc, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict, classify_esbmc.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[7].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:134`; AST `ce20447b66f9f8d0c58e031411bbd30f4f01d60f0597d2892d8b7e49cf622fd1`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, result. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[8]::Assign

Source: `scripts/roadmap_esbmc.py:135`; AST `4f0b520aa3e7c78ea0ef7a9c163760601f810d6b5dbb9924c013d8ccf7fc2f96`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: claims_binding.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9]::If

Source: `scripts/roadmap_esbmc.py:136`; AST `a752eaab9a9e4d1acc4272327427bc80e98f397088c6cedfb986ba119d2f31e4`.

Rust module: `scripts::roadmap_esbmc`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: artifacts, asdict, atomic_write_json, claims, claims_binding, claims_path, classification, environment, esbmc_arguments, file_binding, fixture, name, output, root, run_recipe_stage, toolchain. Outputs/bindings: claims, claims_binding, claims_path.
Calls/effect boundaries: artifacts.append, asdict, atomic_write_json, claims_path.relative_to, claims_path.relative_to(root).as_posix, esbmc_arguments, file_binding, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered If evaluation at root.body[19].body[5].body[9]; no call, error or mutation may be omitted. Condition: classification['outcome'] in {'TOOL_VERDICT_PROPERTIES_UNQUALIFIED', 'FAILURE_PROPERTY_UNREVIEWED'}
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[0]::Assign

Source: `scripts/roadmap_esbmc.py:137`; AST `9ec0150ba07d03343e70cb12c042392adc8fdad9692eea33f73e134ab9e9d8ed`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: environment, esbmc_arguments, fixture, root, run_recipe_stage, toolchain. Outputs/bindings: claims.
Calls/effect boundaries: esbmc_arguments, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[9].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[0].value::Call

Source: `scripts/roadmap_esbmc.py:137`; AST `3037825531e2f219d13687932b9df8848b48c75889bc795622f253b20201b37d`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: environment, esbmc_arguments, fixture, root, run_recipe_stage, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments, run_recipe_stage.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[0].value.args[0]::Call

Source: `scripts/roadmap_esbmc.py:137`; AST `6775c46403e41326a7707961a72f78f70abef9c3ab0ee8b0fb65cc54ae5138f9`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: esbmc_arguments, fixture, root, toolchain. Outputs/bindings: (none).
Calls/effect boundaries: esbmc_arguments.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[1]::Assign

Source: `scripts/roadmap_esbmc.py:139`; AST `4d5024a22b435619d67742a6b1d8847c50b9b6cf123a4619914573fd1a9993a7`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: name, output. Outputs/bindings: claims_path.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[9].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[2]::Expr

Source: `scripts/roadmap_esbmc.py:140`; AST `0775fde3f401bb6cc4254a274dc43fbc801523ac65572695830bc5dfe85ea404`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: asdict, atomic_write_json, claims, claims_path, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[9].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[2].value::Call

Source: `scripts/roadmap_esbmc.py:140`; AST `60d3cf1fab60024644927e6f8c76a9264e38e2283e3c7317aaf1bdd800c5623a`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, atomic_write_json, claims, claims_path, root. Outputs/bindings: (none).
Calls/effect boundaries: asdict, atomic_write_json.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[2].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:140`; AST `a3688a83a36e69c9bf3e08ea63c34331377a22fa9b2aa68f671d4005a8016c56`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: asdict, claims. Outputs/bindings: (none).
Calls/effect boundaries: asdict.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[2].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[3]::Assign

Source: `scripts/roadmap_esbmc.py:141`; AST `f46b84e7f2ec0009b526e6698800b755e39ac39bf25c0f9b0e4042effc70a423`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: claims_path, file_binding, root. Outputs/bindings: claims_binding.
Calls/effect boundaries: claims_path.relative_to, claims_path.relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5].body[9].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[3].value::Call

Source: `scripts/roadmap_esbmc.py:141`; AST `5f2c3c9fefdd7472e6d9ebcc54d2ee9e74cce5a1d449d48524b3aae224c7d058`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: claims_path, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: claims_path.relative_to, claims_path.relative_to(root).as_posix, file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[3].value.args[1]::Call

Source: `scripts/roadmap_esbmc.py:141`; AST `e40b8d0a65007be6c7385f90d927a445b108eaed8a19cb73665d93d47f87eccf`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: claims_path, root. Outputs/bindings: (none).
Calls/effect boundaries: claims_path.relative_to, claims_path.relative_to(root).as_posix.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[3].value.args[1].func.value::Call

Source: `scripts/roadmap_esbmc.py:141`; AST `c63fd54ed2b1fb0cd5704f41047565d8dfd2874ad316d44279559dab47965cd3`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: claims_path, root. Outputs/bindings: (none).
Calls/effect boundaries: claims_path.relative_to.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[3].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[4]::Expr

Source: `scripts/roadmap_esbmc.py:142`; AST `2fa600f144f8249d18f38972fba738b8782f28deba95980016de63f21e9badc1`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, claims_binding. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[9].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[9].body[4].value::Call

Source: `scripts/roadmap_esbmc.py:142`; AST `11234c004da09c513cf0c68aeea013be3e7248288c18f823774717405a0018fd`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: artifacts, claims_binding. Outputs/bindings: (none).
Calls/effect boundaries: artifacts.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[9].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[10]::Expr

Source: `scripts/roadmap_esbmc.py:143`; AST `18c5897e427b7553eca1761fdc0137b9644f4637a35d98245cc10cdc0c4ac6c7`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: claims_binding, classification, fixture, name, result_binding, runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[5].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[5].body[10].value::Call

Source: `scripts/roadmap_esbmc.py:143`; AST `4c24ece9c826f128118bec45c1b0f649f088c3f29b99a1f050d61d5a1f1b984e`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: claims_binding, classification, fixture, name, result_binding, runs. Outputs/bindings: (none).
Calls/effect boundaries: runs.append.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[6]::Return

Source: `scripts/roadmap_esbmc.py:146`; AST `a50c9330b3cfea15bad7be04ee2106cbe65b449cdf8d3f9eec0a463a9be31631`.

Rust module: `scripts::roadmap_esbmc`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: artifacts, binding, file_binding, root, runs, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Return evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[6].value.values[4]::Call

Source: `scripts/roadmap_esbmc.py:147`; AST `9541f4c9d8dff7d7ff3112bf1ab4deb4b2305a0241438b75b655ce54f3816385`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, source_closure. Outputs/bindings: (none).
Calls/effect boundaries: source_closure.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## scripts/roadmap_esbmc.py::module::qualify_esbmc::root.body[19].body[6].value.values[5]::Call

Source: `scripts/roadmap_esbmc.py:148`; AST `5490821019984d7c4f8f46ec5cf3fa43c46111d139cff228c93af8e6fae119fb`.

Rust module: `scripts::roadmap_esbmc`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, agentinfra.atomic, agentinfra.process, agentinfra.roadmap_mirrors, agentinfra.roadmap_python, agentinfra.roadmap_records, agentinfra.security, dataclasses, os, pathlib, shutil, stat, sys, time, venv, zipfile.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
