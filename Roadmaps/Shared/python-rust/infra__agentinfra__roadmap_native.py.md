# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 201. Inventory digest: `c08745c2bda672b7a6ae00907b6f81ed5d78c7cf000bdbbdf94045a202f5b465`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_native.py::module::root::Module

Source: `infra/agentinfra/roadmap_native.py:1`; AST `372cf667af5a14dbd35635989c41af05e86076f9afecd2f4e711d80a6e41a0df`.

Rust module: `infra::agentinfra::roadmap_native`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: CodexReader, INTERFACE_VERSION, Path, _pid_alive, _process_identity, bool, boot, client, context, current, dict, digest, event, event_kind, executable, fields, goal, handle, identity, int, is_process_ancestor, json, kind, len, lifecycle, line, metadata, next, offset, origin, os, owner, owner_executable, parent, path, payload, pid, process_handle, range, raw, read_session_metadata, require, result, root, routing, session, socket, state, str, stream, thread, thread_id, type, usage. Outputs/bindings: INTERFACE_VERSION, _, boot, client, context, current, event, event_kind, executable, fields, goal, identity, kind, lifecycle, line, metadata, offset, origin, owner_executable, parent, path, payload, pid, raw, result, routing, session, state, stream, thread, usage.
Calls/effect boundaries: CodexReader, Path, Path(client.executable).read_bytes, Path(executable['path']).resolve, Path(thread['cwd']).resolve, _pid_alive, _process_identity, boot.exists, boot.read_bytes, client.call, context.get, digest, event.get, goal.get, handle.get, int, is_process_ancestor, json.loads, len, lifecycle.get, line.split, line.split(':', 1)[1].strip, line.startswith, next, os.getpid, owner.get, owner_executable.exists, owner_executable.resolve, path.exists, path.open, path.read_text, path.read_text().splitlines, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, process_handle, range, raw.endswith, read_session_metadata, require, root.resolve, routing.append, socket.gethostname, str, stream.readline, stream.tell, thread.get, type.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_native.py:1`; AST `95f035619612b5206793587b0af2d7dc77a957e13c69f6215eeeefdd8611e3fe`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_native.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_native.py:9`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_native.py:10`; AST `ac3a74d6dd975a8e8fe4b7f85fce794793a9355595b850e3926964913948d386`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_native.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_native.py:12`; AST `9df267ed6eef4f61eaaffaebdf9ac9fe93bcf6d1aab9647b1fd045430624c91e`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[6]::ImportFrom

Source: `infra/agentinfra/roadmap_native.py:14`; AST `010a246c4c56d7b26501d32c14c30f7aff47d5dff742e89b9ad2dd4577f9ba84`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered ImportFrom evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_native.py:15`; AST `f3b29c84ccb33e36661b294cf3be29b70753fdb829915a2e51fca00da4351de1`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_native.py:16`; AST `dcc141a1e9bd471992df89dfef26417080014b0f5967e497f55034dd43ec3a33`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::root.body[9]::Assign

Source: `infra/agentinfra/roadmap_native.py:19`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10]::FunctionDef

Source: `infra/agentinfra/roadmap_native.py:22`; AST `841a0520c4e90d65f6b8487942089874e8289731ac5d2caa08ce27c6696b8c5c`.

Rust module: `infra::agentinfra::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _pid_alive, _process_identity, boot, dict, digest, identity, int, pid, require, socket. Outputs/bindings: boot, identity.
Calls/effect boundaries: Path, _pid_alive, _process_identity, boot.exists, boot.read_bytes, digest, require, socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered FunctionDef evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:23`; AST `9b6e3c38b25dab892c88b918e533ff128ccfd81c25a920f6c7aece97c0524cd0`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_identity, pid. Outputs/bindings: identity.
Calls/effect boundaries: _process_identity.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:23`; AST `97ab2fa3d8871bfad69f9576517a3740e9cb2b5f09b34899b3b395aa0a4b4478`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[1]::Expr

Source: `infra/agentinfra/roadmap_native.py:24`; AST `b7cd66e666dbb7456e0d7fd4b37895c09a8dcd22641a62f8eff425afd8812115`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, identity, pid, require. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[1].value::Call

Source: `infra/agentinfra/roadmap_native.py:24`; AST `8876cbcd4366ac7270f08e54c32a9da34a869068bbc44c062301503cf77887b3`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, identity, pid, require. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[1].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:24`; AST `fa8c9ebf021b18e6716c336d17172d61d67fac049612447c4f03677af0c7ee2b`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[1].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[2]::Assign

Source: `infra/agentinfra/roadmap_native.py:25`; AST `1efa75ed4c3fc2924211913b033089a70b6316a55fe53a26a1586d5618094588`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: boot.
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[10].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[2].value::Call

Source: `infra/agentinfra/roadmap_native.py:25`; AST `12e27f6757b2f3e9d50d87b373e4e6b5aeaded0f4ef59857bb4623f8d2157dc4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[3]::Return

Source: `infra/agentinfra/roadmap_native.py:26`; AST `faaeffd2a53f6812f2008cfab577dd721b81a91e4b86daf569924a2500d0ff65`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: boot, digest, identity, pid, socket. Outputs/bindings: (none).
Calls/effect boundaries: boot.exists, boot.read_bytes, digest, socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[10].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[3].value.values[2]::Call

Source: `infra/agentinfra/roadmap_native.py:26`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[3].value.values[3].test::Call

Source: `infra/agentinfra/roadmap_native.py:27`; AST `2d5817291dacd37361542d08e7e6786af199896a2e1ac1389a03f107d5d0c1d4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot. Outputs/bindings: (none).
Calls/effect boundaries: boot.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.values[3].test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[3].value.values[3].body::Call

Source: `infra/agentinfra/roadmap_native.py:27`; AST `bbf23a9eacff297aa0f0118c34524e708c3cd82753133cd8838c692970ed4da0`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot, digest. Outputs/bindings: (none).
Calls/effect boundaries: boot.read_bytes, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.values[3].body; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::process_handle::root.body[10].body[3].value.values[3].body.args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:27`; AST `21c9fbcbfbdc4eea8fc263b4c47bbfbddca55b3fad3dd448372b04b675062715`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot. Outputs/bindings: (none).
Calls/effect boundaries: boot.read_bytes.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[10].body[3].value.values[3].body.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11]::FunctionDef

Source: `infra/agentinfra/roadmap_native.py:30`; AST `f7b5d99ade04c1922d6fc7c81039f7526bb6c1147405c0f5c23fcffce298c817`.

Rust module: `infra::agentinfra::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, _pid_alive, _process_identity, boot, current, dict, digest, handle, int, pid, socket, str, type. Outputs/bindings: boot, current, pid.
Calls/effect boundaries: Path, _pid_alive, _process_identity, boot.exists, boot.read_bytes, digest, handle.get, socket.gethostname, type.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered FunctionDef evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[0]::If

Source: `infra/agentinfra/roadmap_native.py:31`; AST `aa3abbca16b1dc5bc820a4f1a452b8fc8278259c0be8dc97227876bebbaa1e12`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: handle, socket. Outputs/bindings: (none).
Calls/effect boundaries: handle.get, socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[0]; no call, error or mutation may be omitted. Condition: handle.get('host') != socket.gethostname() or not handle.get('process_identity')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[0].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:31`; AST `959dabe42a6ea817344522fe5cfb3b658f2d188eba532da444feb2c5959e50b5`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handle. Outputs/bindings: (none).
Calls/effect boundaries: handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[0].test.values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_native.py:31`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].test.values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[0].test.values[1].operand::Call

Source: `infra/agentinfra/roadmap_native.py:31`; AST `4507e2cc916dc57e9eadc42e86df7ce1e52eb881519f890c61be8b919e287f73`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handle. Outputs/bindings: (none).
Calls/effect boundaries: handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[0].test.values[1].operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:32`; AST `6eac86cf0d5534dd29d0df0b3c933911ddeb82dd143c7a2106e002fbc6f79544`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:33`; AST `1efa75ed4c3fc2924211913b033089a70b6316a55fe53a26a1586d5618094588`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path. Outputs/bindings: boot.
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[1].value::Call

Source: `infra/agentinfra/roadmap_native.py:33`; AST `12e27f6757b2f3e9d50d87b373e4e6b5aeaded0f4ef59857bb4623f8d2157dc4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2]::If

Source: `infra/agentinfra/roadmap_native.py:34`; AST `cce925efb5f4a3e5f0c0afde0427d7b2e431266d78d0eea74eb15e9d3d4149f7`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: boot, digest, handle. Outputs/bindings: (none).
Calls/effect boundaries: boot.exists, boot.read_bytes, digest, handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[2]; no call, error or mutation may be omitted. Condition: handle.get('boot_identity') is not None
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].test.left::Call

Source: `infra/agentinfra/roadmap_native.py:34`; AST `a9a246f5973d03cea2e62ec8efcd35df882dd49684cf729f41eca426b69cd74a`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handle. Outputs/bindings: (none).
Calls/effect boundaries: handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[0]::If

Source: `infra/agentinfra/roadmap_native.py:35`; AST `07a1fd53ad9aa7b5b2b8fd86155036578b3e153f537c279784fa9dc6d8b73cba`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: boot. Outputs/bindings: (none).
Calls/effect boundaries: boot.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[0]; no call, error or mutation may be omitted. Condition: not boot.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[0].test.operand::Call

Source: `infra/agentinfra/roadmap_native.py:35`; AST `2d5817291dacd37361542d08e7e6786af199896a2e1ac1389a03f107d5d0c1d4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot. Outputs/bindings: (none).
Calls/effect boundaries: boot.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[0].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:36`; AST `6eac86cf0d5534dd29d0df0b3c933911ddeb82dd143c7a2106e002fbc6f79544`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[1]::If

Source: `infra/agentinfra/roadmap_native.py:37`; AST `891a66639701c2cb7a23f8ec245dc98bb9f71112d2842739ddf2457903de15c0`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: boot, digest, handle. Outputs/bindings: (none).
Calls/effect boundaries: boot.read_bytes, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[2].body[1]; no call, error or mutation may be omitted. Condition: digest(boot.read_bytes()) != handle['boot_identity']
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[1].test.left::Call

Source: `infra/agentinfra/roadmap_native.py:37`; AST `bbf23a9eacff297aa0f0118c34524e708c3cd82753133cd8838c692970ed4da0`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot, digest. Outputs/bindings: (none).
Calls/effect boundaries: boot.read_bytes, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].test.left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[1].test.left.args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:37`; AST `21c9fbcbfbdc4eea8fc263b4c47bbfbddca55b3fad3dd448372b04b675062715`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: boot. Outputs/bindings: (none).
Calls/effect boundaries: boot.read_bytes.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[2].body[1].test.left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[2].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:38`; AST `7fb3813cc6e39ec17eb6bc75699d7c11fd4c84b976e803979fefab36d05b6ad3`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[2].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[3]::Assign

Source: `infra/agentinfra/roadmap_native.py:39`; AST `c54c3626672e27b32bc804a5b53d8e1001c11b8a2614dcefad418a2132e9dc04`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: handle. Outputs/bindings: pid.
Calls/effect boundaries: handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[3].value::Call

Source: `infra/agentinfra/roadmap_native.py:39`; AST `2e78890a987d6e187fe2538553d97510b489e8aba25af2d9e52dfdda244cfd6a`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handle. Outputs/bindings: (none).
Calls/effect boundaries: handle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[4]::If

Source: `infra/agentinfra/roadmap_native.py:40`; AST `86293be3e50cf53c090be60658ab63fb13a198e79241f5cb3c69d17fd346def7`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: int, pid, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[4]; no call, error or mutation may be omitted. Condition: type(pid) is not int or pid <= 0
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[4].test.values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:40`; AST `acef30824461625c2df01492671e9b8dbc00efd4a989c4b005bcde314f18533b`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: pid, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[4].test.values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[4].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:41`; AST `6eac86cf0d5534dd29d0df0b3c933911ddeb82dd143c7a2106e002fbc6f79544`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[4].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[5]::Assign

Source: `infra/agentinfra/roadmap_native.py:42`; AST `efbf435e201ea28c516bf77fca5ecaa9ed467a5196ab1bc5aa766b29226a0593`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _process_identity, pid. Outputs/bindings: current.
Calls/effect boundaries: _process_identity.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[11].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[5].value::Call

Source: `infra/agentinfra/roadmap_native.py:42`; AST `97ab2fa3d8871bfad69f9576517a3740e9cb2b5f09b34899b3b395aa0a4b4478`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _process_identity, pid. Outputs/bindings: (none).
Calls/effect boundaries: _process_identity.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[6]::If

Source: `infra/agentinfra/roadmap_native.py:43`; AST `eb176528283bf4f5cf79595b3ffd1cfe0b289eff9a6e94fd82a70d5b3b0ddc2d`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: _pid_alive, current, pid. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[11].body[6]; no call, error or mutation may be omitted. Condition: current is None
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[6].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:44`; AST `95123bd93aeaa9822077c422a5b87ff697f46a1bee53e0ca7899b21ef52beba9`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, pid. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[6].body[0].value.test::Call

Source: `infra/agentinfra/roadmap_native.py:44`; AST `c5afa342dc24bba6838cb6737050642c5b9a72436ed81cef4355c289c6952ecf`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, pid. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[11].body[6].body[0].value.test; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::inspect_process::root.body[11].body[7]::Return

Source: `infra/agentinfra/roadmap_native.py:45`; AST `11c04cd49e4b33b887eff3d9472bb320c4a7c520a692e702e0e14340c877b14b`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: current, handle. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[11].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12]::FunctionDef

Source: `infra/agentinfra/roadmap_native.py:48`; AST `47ee473f1526ba020ecae243f83b123b373de32b42f2e4c66ec147f35a96e2f1`.

Rust module: `infra::agentinfra::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, bool, current, fields, int, line, next, os, parent, path, pid, range. Outputs/bindings: _, current, fields, line, parent, path.
Calls/effect boundaries: Path, int, line.split, line.split(':', 1)[1].strip, line.startswith, next, os.getpid, path.exists, path.read_text, path.read_text().splitlines, range.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:49`; AST `3da110a87f93c33fa66fb6fb5439bfc35da9a6ee418aa4e5b9f5eb8f043cac2d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: os. Outputs/bindings: current.
Calls/effect boundaries: os.getpid.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:49`; AST `ba1923643b161051a18bf7ae7386addd84146f4ab481f99d56712bc1ce97df2c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: os. Outputs/bindings: (none).
Calls/effect boundaries: os.getpid.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1]::For

Source: `infra/agentinfra/roadmap_native.py:50`; AST `8cd1887f6eed5b63dd4c48e15d8d3c22d26e3a886c9eb203a5737ee6997b6f0e`.

Rust module: `infra::agentinfra::roadmap_native`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Path, current, fields, int, line, next, parent, path, pid, range. Outputs/bindings: _, current, fields, line, parent, path.
Calls/effect boundaries: Path, int, line.split, line.split(':', 1)[1].strip, line.startswith, next, path.exists, path.read_text, path.read_text().splitlines, range.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered For evaluation at root.body[12].body[1]; no call, error or mutation may be omitted. Iteration: _ in range(128)
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].iter::Call

Source: `infra/agentinfra/roadmap_native.py:50`; AST `7d6d5d2d7cb0b3af01a22c76c2ed6b0453c04aba0b0ea95defeccdf27d6cd56d`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: range. Outputs/bindings: (none).
Calls/effect boundaries: range.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].iter; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_native.py:51`; AST `41e99a5be506e9ce1c9ecdd9dfac4586f8c099893c0ccdeb6a515491cd3ba251`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, pid. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted. Condition: current == pid
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[0].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:52`; AST `4a8ef490a01d3017cb999fbea58c2adfb60a40ad736e0d23eceb176a236b14c3`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:53`; AST `685adcdc9565fdc7844f1ead1d6b71e975e54078aa3a555db8096ec78f63ce44`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, current. Outputs/bindings: path.
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_native.py:53`; AST `f7f0fd2a4da077872266401ec0e24b95359f18530068d52c73b20e242efeaab6`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, current. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_native.py:54`; AST `0f4d97efb400e6b7575df77a44bae4749db0e5837483033a195315c4eb5b2327`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[12].body[1].body[2]; no call, error or mutation may be omitted. Condition: not path.exists()
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[2].test.operand::Call

Source: `infra/agentinfra/roadmap_native.py:54`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[2].test.operand; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[2].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:55`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[3]::Assign

Source: `infra/agentinfra/roadmap_native.py:56`; AST `0acd0de50578396bb8d9ee03b63a9947df5273b4074deb53c7dec8adaeb8e977`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: fields.
Calls/effect boundaries: path.read_text, path.read_text().splitlines.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_native.py:56`; AST `6ff431918ffde64bb1c1428596401c8ce5e94f2e2e0a999fd96dece2105a2911`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text, path.read_text().splitlines.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[3].value.func.value::Call

Source: `infra/agentinfra/roadmap_native.py:56`; AST `6f5b3f538cc7e19410b08f8be3c28081a9ce52ef26c87cf4f8e875c0bd8b66b4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_text.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[3].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4]::Assign

Source: `infra/agentinfra/roadmap_native.py:57`; AST `4d79bb1d2e03183030c31c82889ea09d4ff13763a6abd27990062ea1080d8f0a`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: fields, int, line, next. Outputs/bindings: line, parent.
Calls/effect boundaries: int, line.split, line.split(':', 1)[1].strip, line.startswith, next.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_native.py:57`; AST `9e9c848274c5e4471642b683c403061e1438292b8ae1d9540b6b4f2495beea7f`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, int, line, next. Outputs/bindings: line.
Calls/effect boundaries: int, line.split, line.split(':', 1)[1].strip, line.startswith, next.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:57`; AST `8675e99bd024d784b5629a49184d1e781c59a474e864600d2225e891b08f898f`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: fields, line, next. Outputs/bindings: line.
Calls/effect boundaries: line.split, line.split(':', 1)[1].strip, line.startswith, next.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_native.py:57`; AST `24243de66d189d53cf488435304a136aa43f727558e6863f4cd0c16a33084f67`.

Rust module: `infra::agentinfra::roadmap_native`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: fields, line. Outputs/bindings: line.
Calls/effect boundaries: line.split, line.split(':', 1)[1].strip, line.startswith.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[12].body[1].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value.args[0].args[0].elt::Call

Source: `infra/agentinfra/roadmap_native.py:57`; AST `818aa9f55fcfbe42df1207bf4802064995c2bd7cee54a5a092ec69f3aab2732e`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.split, line.split(':', 1)[1].strip.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value.args[0].args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value.args[0].args[0].elt.func.value.value::Call

Source: `infra/agentinfra/roadmap_native.py:57`; AST `b81261876cd549895e0b92f47b28eb3ad280f8d93dde630c44ea26420a601511`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.split.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value.args[0].args[0].elt.func.value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[4].value.args[0].args[0].generators[0].ifs[0]::Call

Source: `infra/agentinfra/roadmap_native.py:57`; AST `8434167973a2da8b4550031d8a52daac8f79e6a0180e15adc6c8f3e195bd2136`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: line. Outputs/bindings: (none).
Calls/effect boundaries: line.startswith.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[4].value.args[0].args[0].generators[0].ifs[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[5]::If

Source: `infra/agentinfra/roadmap_native.py:58`; AST `5ca97e4ee32e790255e4773577d6bba26a499a033ea972271512d706917a647e`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: current, parent. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[12].body[1].body[5]; no call, error or mutation may be omitted. Condition: parent <= 0 or parent == current
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[5].body[0]::Return

Source: `infra/agentinfra/roadmap_native.py:59`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[12].body[1].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[1].body[6]::Assign

Source: `infra/agentinfra/roadmap_native.py:60`; AST `da2b7dbc5b683178e62c3ce083fc2e9c83d6d308477dd4a842488b2e3e161b08`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parent. Outputs/bindings: current.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::is_process_ancestor::root.body[12].body[2]::Return

Source: `infra/agentinfra/roadmap_native.py:61`; AST `dd863ea504e8543d2fb185a820aa7e2cf2d0ceddec9c835185a3510fc2ab463d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13]::FunctionDef

Source: `infra/agentinfra/roadmap_native.py:64`; AST `9a1421b22a9f8b4b2ef376b2dbe0736c6a529839bf7b4d806b5724dc4043d8ca`.

Rust module: `infra::agentinfra::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, context, dict, digest, event, event_kind, json, kind, len, lifecycle, offset, origin, path, payload, raw, require, routing, session, str, stream, thread_id, usage. Outputs/bindings: context, event, event_kind, kind, lifecycle, offset, origin, payload, raw, routing, session, stream, usage.
Calls/effect boundaries: context.get, digest, event.get, json.loads, len, lifecycle.get, path.open, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, raw.endswith, require, routing.append, str, stream.readline, stream.tell.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered FunctionDef evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:65`; AST `686d177f7fd8678147ac412f14a966289e3f4fbacfe854bee2122fe610ba31eb`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: session.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:66`; AST `fc9ceb11ca2ed99c84ce918e6c21088987f377bd636df4ca1791e1750dc1cb4f`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: context.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[2]::Assign

Source: `infra/agentinfra/roadmap_native.py:67`; AST `1302dab6e973893e29bbe2f477b053a9a4756794d1b318f20260b4e6c0815144`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: lifecycle.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[3]::Assign

Source: `infra/agentinfra/roadmap_native.py:68`; AST `f698d21e73f9bd5a67b3c01c4135142f7a80a85d20174b0ed5d2d1e22fec3168`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: usage.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_native.py:69`; AST `4eadfd388799e84de0a9044f7e350376a98b06734aa090a9dca801b3afe9255b`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: routing.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5]::With

Source: `infra/agentinfra/roadmap_native.py:70`; AST `cbbd4e8a382fcfcc4d491d89e963dd8fe43e16832a9f230a0e8d727e94912aa9`.

Rust module: `infra::agentinfra::roadmap_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: context, digest, event, event_kind, json, kind, len, offset, origin, path, payload, raw, require, routing, str, stream. Outputs/bindings: context, event, event_kind, kind, lifecycle, offset, origin, payload, raw, routing, session, stream, usage.
Calls/effect boundaries: context.get, digest, event.get, json.loads, len, path.open, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, raw.endswith, require, routing.append, str, stream.readline, stream.tell.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered With evaluation at root.body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_native.py:70`; AST `cf2984cb08c691f2c9c1f8bae5b41cfff4de4e7a17dbea14d92d2e0c1b1b6ab3`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.open.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0]::While

Source: `infra/agentinfra/roadmap_native.py:71`; AST `45c07ffa1fdd95b410b5c2e2255addb28b9248e06b60cbd8c9d865b435b8269d`.

Rust module: `infra::agentinfra::roadmap_native`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: context, digest, event, event_kind, json, kind, len, offset, origin, path, payload, raw, require, routing, str, stream. Outputs/bindings: context, event, event_kind, kind, lifecycle, offset, origin, payload, raw, routing, session, usage.
Calls/effect boundaries: context.get, digest, event.get, json.loads, len, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, raw.endswith, require, routing.append, str, stream.readline, stream.tell.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered While evaluation at root.body[13].body[5].body[0]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:72`; AST `51297d2e3d416c4f43c4350b85a273d7afaaedad21a582a3c8ca850007d0750d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: offset.
Calls/effect boundaries: stream.tell.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:72`; AST `f5cebbed22d978624526f5c640cb4511464e8b8b147280fd71f2fa119a44d9ed`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.tell.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:73`; AST `13716e1e79220852ccdd5b44e78c1d2b607e1dd7481a56532b8e9ccabc2a77fe`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: stream. Outputs/bindings: raw.
Calls/effect boundaries: stream.readline.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_native.py:73`; AST `a0da1a09841eebceb861e3291a50e19cd4a5e87dd4a7423793a2573e11954b21`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: stream. Outputs/bindings: (none).
Calls/effect boundaries: stream.readline.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[2]::If

Source: `infra/agentinfra/roadmap_native.py:74`; AST `d3a453ece86035ce1fef5b7f00b2e14a5ea6c06e6d26a7dbe5f24bf064d801ef`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[2]; no call, error or mutation may be omitted. Condition: not raw
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[2].body[0]::Break

Source: `infra/agentinfra/roadmap_native.py:75`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Break evaluation at root.body[13].body[5].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[3]::Expr

Source: `infra/agentinfra/roadmap_native.py:76`; AST `def58dee6fe6c34d7f5b9e0b76e73d1c29e963332db2459962c95c4b316332e2`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: len, raw.endswith, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[3].value::Call

Source: `infra/agentinfra/roadmap_native.py:76`; AST `1a5c8a29e820c5309729582559abc9aab89e273136d1afe21e1d0f7e361e7e2c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: len, raw.endswith, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:76`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[3].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:76`; AST `5c54d1568ff83f4712e97327ffe52db426ada06b9acd002c4a5611b7ca6c876f`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.endswith.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[3].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[4]::Assign

Source: `infra/agentinfra/roadmap_native.py:77`; AST `e24971587434623fb5f92fd7f6978f4fab7c3e98e13a4f4bb554625aad1e41e2`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: json, raw. Outputs/bindings: event.
Calls/effect boundaries: json.loads.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[4].value::Call

Source: `infra/agentinfra/roadmap_native.py:77`; AST `3d89c902bc01348c144bfca2b00418675b9e8f5d1e5b98c069ae8659d008e758`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: json, raw. Outputs/bindings: (none).
Calls/effect boundaries: json.loads.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[5]::Assign

Source: `infra/agentinfra/roadmap_native.py:78`; AST `48a9969eb3f3aaeafa46c3dbe24d496259488c270d912f1b9e4efd8337975bdf`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event. Outputs/bindings: kind.
Calls/effect boundaries: event.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[5].value::Call

Source: `infra/agentinfra/roadmap_native.py:78`; AST `c623ed8b6bc0af29a322d4a94af5a23bb62b68b7d9ae059606228a8a9603a814`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event. Outputs/bindings: (none).
Calls/effect boundaries: event.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[6]::Assign

Source: `infra/agentinfra/roadmap_native.py:79`; AST `8fc3ecbd5814de83adb129bfa44e004a8b865585bac2828d7c6021b29d8d9bd3`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event. Outputs/bindings: payload.
Calls/effect boundaries: event.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[6].value::Call

Source: `infra/agentinfra/roadmap_native.py:79`; AST `18726e88212cecfcd6ba41f67fcaf1c90faf0e3b437a84cabd6b9842dc47bab6`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event. Outputs/bindings: (none).
Calls/effect boundaries: event.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[7]::Assign

Source: `infra/agentinfra/roadmap_native.py:80`; AST `fbebad9b0f9567c0584faed2b6228552e356fa02878856cf6c790be7c2e6b674`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, event, len, offset, path, raw, str. Outputs/bindings: origin.
Calls/effect boundaries: digest, event.get, len, str.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[7].value.values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:80`; AST `b69621d1d2cfab110acfa6b4ec39b44f2e36ecd25b7402532cc02261af94b6bf`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[7].value.values[2]::Call

Source: `infra/agentinfra/roadmap_native.py:80`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[7].value.values[3]::Call

Source: `infra/agentinfra/roadmap_native.py:80`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[7].value.values[4]::Call

Source: `infra/agentinfra/roadmap_native.py:81`; AST `a90b576983e0afef821099568037e48f09dc40bcfaa95fea13ac3b81b1e6da73`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: event. Outputs/bindings: (none).
Calls/effect boundaries: event.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[7].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8]::If

Source: `infra/agentinfra/roadmap_native.py:82`; AST `c52371d39711cfe40af3737004b5ba80e3b321d4aa72b1b2357e6b4d1345cd7d`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, event_kind, kind, origin, payload, routing. Outputs/bindings: context, event_kind, lifecycle, routing, session, usage.
Calls/effect boundaries: context.get, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8]; no call, error or mutation may be omitted. Condition: kind == 'session_meta'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:83`; AST `73905a5b0005361152ad10c3910d52ec07f853ce6c96cad5caf1d1bf43d8098a`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: origin, payload. Outputs/bindings: session.
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].body[0].value.values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:83`; AST `fd6966b5a495a224c3d2485b841a1d4bb3122af2764bb40b1b91b1df51887a1f`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0]::If

Source: `infra/agentinfra/roadmap_native.py:84`; AST `e03667afb106456fd7d81875b9f50cc102051f0476a62b271c05d0f69d2c93eb`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, event_kind, kind, origin, payload, routing. Outputs/bindings: context, event_kind, lifecycle, routing, usage.
Calls/effect boundaries: context.get, payload.get, payload.get('collaboration_mode', {}).get, payload['info'].get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0]; no call, error or mutation may be omitted. Condition: kind == 'turn_context'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[0]::If

Source: `infra/agentinfra/roadmap_native.py:85`; AST `cb42f7553c00a7d90acbf5809dcaec766062de1343c5e06e79f5736fa3782aec`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: context, payload. Outputs/bindings: routing.
Calls/effect boundaries: context.get, payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[0]; no call, error or mutation may be omitted. Condition: context is None or context.get('turn_id') != payload.get('turn_id')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[0].test.values[1].left::Call

Source: `infra/agentinfra/roadmap_native.py:85`; AST `f094fe87951f84d5b815288e3b7f21b9f91bf4aefdd73ab22d0698e976cf79ad`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[0].test.values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[0].test.values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_native.py:85`; AST `33d00eb96d728714e5bdb60e5a46a401f1c155167e8ca92feaecd0228408b932`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[0].test.values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:86`; AST `4eadfd388799e84de0a9044f7e350376a98b06734aa090a9dca801b3afe9255b`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: routing.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:87`; AST `9246b5013f9d6dbf80677fd56c938bce2cad2bab4bbd4fa6aa6332102cb0cc05`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: origin, payload. Outputs/bindings: context.
Calls/effect boundaries: payload.get, payload.get('collaboration_mode', {}).get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:87`; AST `1f4009a0eca0b8944ef383af2a755ca7c8dbec63d41c4c2a7777f8450a778172`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:87`; AST `a5bc877a58337d7d42dff5a07f32180ee32468f80c80bf22d6c46bad548db8ae`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[2]::Call

Source: `infra/agentinfra/roadmap_native.py:88`; AST `33d00eb96d728714e5bdb60e5a46a401f1c155167e8ca92feaecd0228408b932`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[3]::Call

Source: `infra/agentinfra/roadmap_native.py:89`; AST `f5225035d4588890eadd0943ee8355ebb2cb99df0afea27c0b90ce2b39e3abb2`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get, payload.get('collaboration_mode', {}).get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[3].func.value::Call

Source: `infra/agentinfra/roadmap_native.py:89`; AST `48ad114b1d18bd6ab5acea9b91096edc1102f1b9e5b2f61d0f02bea607b3b10d`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[3].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[4]::Call

Source: `infra/agentinfra/roadmap_native.py:90`; AST `cb30716d64b7afb4be21c742f1e9f4fbd4f4226c692e23f8c3e8ca370dd431c6`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].body[1].value.values[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_native.py:91`; AST `e70d88048e563dd32f6afb7adff07dafa28afacbd45b915b8e67404736ab1788`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: event_kind, kind, origin, payload, routing. Outputs/bindings: event_kind, lifecycle, usage.
Calls/effect boundaries: payload.get, payload['info'].get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: kind == 'event_msg'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:92`; AST `8d14ba08f1549c8c37a1959c62b357025831417cf317a6be0971b9242484b955`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: payload. Outputs/bindings: event_kind.
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:92`; AST `3ba966235cb872f8f831cc23823164168d672c7d4d9cbaf035f99fb2e236a1a9`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1]::If

Source: `infra/agentinfra/roadmap_native.py:93`; AST `15db15f31e6f92d0c0026d6a0b163b13332577c511077ad1a575241110def237`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: event_kind, origin, payload, routing. Outputs/bindings: lifecycle, usage.
Calls/effect boundaries: payload.get, payload['info'].get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1]; no call, error or mutation may be omitted. Condition: event_kind in {'task_started', 'task_complete', 'turn_aborted'}
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:94`; AST `bdfe32542c41a654f97778050b0a99624a65e055dc8919a95fdbc9f500dc2340`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: event_kind, origin, payload. Outputs/bindings: lifecycle.
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].body[0].value.values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:94`; AST `33d00eb96d728714e5bdb60e5a46a401f1c155167e8ca92feaecd0228408b932`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].body[0].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0]::If

Source: `infra/agentinfra/roadmap_native.py:95`; AST `0427e8e9e1dcf443e523308869f3199256bceb7b6b489127d4d4db06d47c6e32`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: event_kind, origin, payload, routing. Outputs/bindings: usage.
Calls/effect boundaries: payload.get, payload['info'].get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0]; no call, error or mutation may be omitted. Condition: event_kind == 'token_count' and payload.get('info')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].test.values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:95`; AST `14a4027c87f1979e98951b855635b5c28ca3b8da127547761d9b1d8cae3c9deb`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:96`; AST `f69c8dede194e4c96e60edc7e825abd9fbcab8009a4aaab069f80f9c7fbc9a36`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: origin, payload. Outputs/bindings: usage.
Calls/effect boundaries: payload['info'].get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].body[0].value.values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:96`; AST `17d3b50795c683dafe65f43a66ed4d0b2918640546e191e7b08b4519965b77d3`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload['info'].get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].body[0].value.values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0]::If

Source: `infra/agentinfra/roadmap_native.py:97`; AST `e184e0f38531359032fb6ff1a92dff2bb3ee13412bbdea0269fdf92abd9ec253`.

Rust module: `infra::agentinfra::roadmap_native`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: event_kind, origin, payload, routing. Outputs/bindings: (none).
Calls/effect boundaries: payload.get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered If evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0]; no call, error or mutation may be omitted. Condition: event_kind == 'model_rerouted'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_native.py:98`; AST `e5e0f2409647ed7840546b852a0babd6d007f145894c596786430fe85edf3f0d`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: origin, payload, routing. Outputs/bindings: (none).
Calls/effect boundaries: payload.get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:98`; AST `d9ced78f74761de471082f3b880e57b3bceefb09e11f3e8205771bb1b5d8b827`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: origin, payload, routing. Outputs/bindings: (none).
Calls/effect boundaries: payload.get, routing.append.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:98`; AST `33d00eb96d728714e5bdb60e5a46a401f1c155167e8ca92feaecd0228408b932`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:98`; AST `6b64d6434cc48a20976d59884e2766066e882298d5a87211f090d28684e67282`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_native.py:99`; AST `e13231f463ff51c6180727d53739cd55b5eb490d2f3967a04b82c17ceed03001`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: payload. Outputs/bindings: (none).
Calls/effect boundaries: payload.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[5].body[0].body[8].orelse[0].orelse[0].body[1].orelse[0].orelse[0].body[0].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[6]::Expr

Source: `infra/agentinfra/roadmap_native.py:100`; AST `a4a9433bbab51ccb5d68978a30984e7149123a96905beeccc8f44f31308175d8`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, session, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[6].value::Call

Source: `infra/agentinfra/roadmap_native.py:100`; AST `c675a39867b595b9af6de03cbfeb0a7b8fd434330cc144a8eabd6da970aab48c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, session, thread_id. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[7]::Expr

Source: `infra/agentinfra/roadmap_native.py:101`; AST `0fb1ab55a3b5626e21b006a3361ed151e87c60c1caa15171eaafc9c45d538339`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, lifecycle, require. Outputs/bindings: (none).
Calls/effect boundaries: lifecycle.get, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[7].value::Call

Source: `infra/agentinfra/roadmap_native.py:101`; AST `29545609e1c683b68c9dac355b9b7b35840c68a46a2e298a3bc03676fcb66a9c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, lifecycle, require. Outputs/bindings: (none).
Calls/effect boundaries: lifecycle.get, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[7].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_native.py:101`; AST `e87474e01c26685faf39b453a42fbd00de06ffd933d846fed25c0bb41253d350`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: lifecycle. Outputs/bindings: (none).
Calls/effect boundaries: lifecycle.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[13].body[7].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::read_session_metadata::root.body[13].body[8]::Return

Source: `infra/agentinfra/roadmap_native.py:102`; AST `a688e6412f76ff50fe76eda37da00e300216f266c7d1e615e149595985c51ff2`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, lifecycle, routing, session, usage. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[13].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_native.py:105`; AST `23ebf2973f06a0281fdaddc13acaaf93474dbf599b0cee5b5ca23edd6c28b8cf`.

Rust module: `infra::agentinfra::roadmap_native`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: CodexReader, INTERFACE_VERSION, Path, _pid_alive, client, context, dict, digest, executable, goal, is_process_ancestor, metadata, owner, owner_executable, process_handle, read_session_metadata, require, result, root, socket, state, thread. Outputs/bindings: client, context, executable, goal, metadata, owner_executable, result, state, thread.
Calls/effect boundaries: CodexReader, Path, Path(client.executable).read_bytes, Path(executable['path']).resolve, Path(thread['cwd']).resolve, _pid_alive, client.call, context.get, digest, goal.get, is_process_ancestor, owner.get, owner_executable.exists, owner_executable.resolve, process_handle, read_session_metadata, require, root.resolve, socket.gethostname, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0]::Expr

Source: `infra/agentinfra/roadmap_native.py:106`; AST `873c275cee08bccd6c703352f04f4ff615a0c5d7a4f3422febb887a570ee85b2`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, owner.get, require, socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_native.py:106`; AST `3181d0a5f60c1029cba5722bc8c2f7ddd5f069e414d68fd4f7b5e5edd5ad324f`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner, require, socket. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, owner.get, require, socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:106`; AST `03d3b11aaf79145d39ddbb53c87a20f8a9f5a15bdf14a916336be876eb9986f4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_native.py:106`; AST `4263cfe4ff762fbfb73db5540d6d421a621a7fb22318759bc79d367d143d5895`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.gethostname.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:107`; AST `4e53f12a86d5ea50b43f6acbb353586c142c688a83131bde24ee6ddc6578e448`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _pid_alive, owner. Outputs/bindings: (none).
Calls/effect boundaries: _pid_alive, owner.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value.args[0].values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:107`; AST `74dd8c31d58328cd9ed8e12172bf1f92e764a09f60e2e061f0a57d8b89827474`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[0].value.args[0].values[1].args[1]::Call

Source: `infra/agentinfra/roadmap_native.py:107`; AST `6df7346f8a9e90dfc4b9a5b830dada1a2d7f1a03e5cfe93e9e57f7a6c6f04db3`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner. Outputs/bindings: (none).
Calls/effect boundaries: owner.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0].values[1].args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1]::With

Source: `infra/agentinfra/roadmap_native.py:108`; AST `eab2db31751ba7f5efc6b7724c2d0e5cb9b3c959c87134d0a6226eb66cacb19b`.

Rust module: `infra::agentinfra::roadmap_native`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: CodexReader, Path, client, digest, owner. Outputs/bindings: client, executable, goal, thread.
Calls/effect boundaries: CodexReader, Path, Path(client.executable).read_bytes, client.call, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered With evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_native.py:108`; AST `5474868276eac54ee388fbec780e85b338d421cad5310223341f527dadf813f2`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: CodexReader. Outputs/bindings: (none).
Calls/effect boundaries: CodexReader.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_native.py:109`; AST `9ece6b9aae2c5746e5ac7e4c58760415b399899345f8a0ec0630e24e1c0a75eb`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, owner. Outputs/bindings: goal.
Calls/effect boundaries: client.call.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[0].value.value::Call

Source: `infra/agentinfra/roadmap_native.py:109`; AST `216bf4de7120209a57095a0fc31f954f012cf3bfceaa71e52590e165be899827`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, owner. Outputs/bindings: (none).
Calls/effect boundaries: client.call.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[0].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_native.py:110`; AST `07937052d36aa37ec7a7f08ad6f8a5fe6d0dbdad215c47b1581a84f37be39357`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: client, owner. Outputs/bindings: thread.
Calls/effect boundaries: client.call.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[1].value.value::Call

Source: `infra/agentinfra/roadmap_native.py:110`; AST `17695ffab7e80338d581d33326e20e47c38d5e46716a9739bcb48916b89025e4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: client, owner. Outputs/bindings: (none).
Calls/effect boundaries: client.call.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_native.py:111`; AST `e85d929cb957a908facbcf818f86347221ac785134a443d3ab64dfb911dc63eb`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, client, digest. Outputs/bindings: executable.
Calls/effect boundaries: Path, Path(client.executable).read_bytes, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[2].value.values[1]::Call

Source: `infra/agentinfra/roadmap_native.py:111`; AST `0ad8a3ab6a13f1648ff746560ab6ace8cc1701de0d607511e0cf0cf4f96d77b0`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client, digest. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(client.executable).read_bytes, digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.values[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[2].value.values[1].args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:111`; AST `a5716cbca75c2e8d15ba9b23f04415592adaad3e27233003c711aaeb0963164e`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(client.executable).read_bytes.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[1].body[2].value.values[1].args[0].func.value::Call

Source: `infra/agentinfra/roadmap_native.py:111`; AST `8e918ec44e1a14e1691757c17663cddf52724a8e2388abc0fcc63a1b6a46b287`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, client. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].body[2].value.values[1].args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[2]::Expr

Source: `infra/agentinfra/roadmap_native.py:112`; AST `61b1f7e7cd9d50bb31342ce340be3cd903a229f82f4d2cda88b56aa7d1472504`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: goal, owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[2].value::Call

Source: `infra/agentinfra/roadmap_native.py:112`; AST `5da050342d6b3c5ce98eb5b224ebe8f5161b1453828ded782d10eff5d20459b0`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal, owner, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: goal.get, require, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[2].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:112`; AST `1e72ea6afac0e7afab17f95dcb152eb935fc9a728ae1ad9f13a9e064e2ae22c5`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[2].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_native.py:112`; AST `8f55e512c3a2f19fb9f66b774909d8420ccfacefd0b26022a3494cdd5841f2a4`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: goal. Outputs/bindings: (none).
Calls/effect boundaries: goal.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[3]::Expr

Source: `infra/agentinfra/roadmap_native.py:114`; AST `ec6cbd2df428c90ea74c358c5dbde40f63ebce4ea03787a47d2fb3bf8441e0bf`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, require, root, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(thread['cwd']).resolve, require, root.resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[3].value::Call

Source: `infra/agentinfra/roadmap_native.py:114`; AST `3ddd02e87886805de02cba9781ea1acee3e6487ccc715f8762446071d8cb486c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, require, root, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(thread['cwd']).resolve, require, root.resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:114`; AST `6e0daa542d88a148d93a8ed36369095d7f591b23614e759e5e1205d61f4fd527`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(thread['cwd']).resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[3].value.args[0].left.func.value::Call

Source: `infra/agentinfra/roadmap_native.py:114`; AST `6eebed5972569d20078fcb2a772f0189edec0552c206372144f3010ff1cff2cd`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[3].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_native.py:114`; AST `b97f3f463d4724206af2869ad4674d5eb373167f052507971a722ecc8f771a87`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: root.resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[4]::Assign

Source: `infra/agentinfra/roadmap_native.py:115`; AST `9d45937e75dfbb29838adf561febd79713c0f24d84126e437c8a6e40dfcf7337`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, owner. Outputs/bindings: owner_executable.
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[4].value::Call

Source: `infra/agentinfra/roadmap_native.py:115`; AST `0755a0e236949a57c6872697dcb4a491e89e6b5e4f173e9110fa63122ca70ba5`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, owner. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5]::Expr

Source: `infra/agentinfra/roadmap_native.py:116`; AST `d3c730e663a1823035e0150b8c5569c14bcc219f0e9137f8e1d1b389525c9239`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, executable, owner_executable, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(executable['path']).resolve, owner_executable.exists, owner_executable.resolve, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5].value::Call

Source: `infra/agentinfra/roadmap_native.py:116`; AST `1221f14a2f9b61f719758777b9b26fcee012f7d67093506ac319311690405ee5`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, executable, owner_executable, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(executable['path']).resolve, owner_executable.exists, owner_executable.resolve, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_native.py:116`; AST `aad9cce7f35914511b4526f065127282da64125274c95bab7f658b46baa7adba`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner_executable. Outputs/bindings: (none).
Calls/effect boundaries: owner_executable.exists.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_native.py:116`; AST `9356029e94c48a7dc63ba435f175ad4db75aa9c532077eab0aad0be224fa0308`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner_executable. Outputs/bindings: (none).
Calls/effect boundaries: owner_executable.resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_native.py:116`; AST `a4e2a17d85da9d1fe700baedba581c04a44cb3e537d1a0b15618c9bec8938721`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, executable. Outputs/bindings: (none).
Calls/effect boundaries: Path, Path(executable['path']).resolve.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[5].value.args[0].values[1].comparators[0].func.value::Call

Source: `infra/agentinfra/roadmap_native.py:116`; AST `efe8ddc0b415f50350aa689c886891611287f90c50b12f26c062947d53eab5e9`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, executable. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].values[1].comparators[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[6]::Assign

Source: `infra/agentinfra/roadmap_native.py:118`; AST `9f7235fac221f787b0e58c7198e62e1daa6270a50f21dcea89bbb7fe71f83927`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, owner, read_session_metadata, thread. Outputs/bindings: metadata.
Calls/effect boundaries: Path, read_session_metadata.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[6].value::Call

Source: `infra/agentinfra/roadmap_native.py:118`; AST `c25349de0439a45649c72c867e2caebad60fbfcf03c4a8ff2eb4f3dd6d4ce410`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, owner, read_session_metadata, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path, read_session_metadata.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[6].value.args[0]::Call

Source: `infra/agentinfra/roadmap_native.py:118`; AST `12268a32766cddcb1dcf7aa1eae1de6e8b66aab09c4ba6043c985c4363bbede9`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, thread. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[7]::Assign

Source: `infra/agentinfra/roadmap_native.py:119`; AST `a87cbeee31103a54f4a3dd823da85a89374368a3dbc8d9bb1d3aa727619a540f`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: metadata. Outputs/bindings: context.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[8]::Expr

Source: `infra/agentinfra/roadmap_native.py:120`; AST `a4b9ff2072ab3021d694454efeb67e798dd06dc8468f536665148b58c0695052`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: metadata, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[8].value::Call

Source: `infra/agentinfra/roadmap_native.py:120`; AST `56a51d0de99e0e4a13552c13a9cf98f41f9c708f7e2bb24be6c3976529cc7e1d`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: metadata, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[9]::Expr

Source: `infra/agentinfra/roadmap_native.py:121`; AST `1e9e0c983b29adadd711b664df9c11c3edbee89f0ffc1e0d8e84b036f9afa446`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, metadata, require. Outputs/bindings: (none).
Calls/effect boundaries: context.get, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[9].value::Call

Source: `infra/agentinfra/roadmap_native.py:121`; AST `258d1d9eaac7e45387766cb88f3265fe2f229d770c56ea6d860677bc0f3f99d6`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, metadata, require. Outputs/bindings: (none).
Calls/effect boundaries: context.get, require.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[9].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:121`; AST `f094fe87951f84d5b815288e3b7f21b9f91bf4aefdd73ab22d0698e976cf79ad`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context. Outputs/bindings: (none).
Calls/effect boundaries: context.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[9].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[10]::Expr

Source: `infra/agentinfra/roadmap_native.py:123`; AST `84d67fbe2655a6a214f6c10d2bf149baa35ec309ecd811919a3befae432fab04`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: require, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[10].value::Call

Source: `infra/agentinfra/roadmap_native.py:123`; AST `5d7f3a6ba4589eb2ab1b5bdd86e9d7da0da730f4c52025e9ab2c77b1fe99eb54`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, require, thread. Outputs/bindings: (none).
Calls/effect boundaries: require, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[10].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_native.py:123`; AST `fea912d461c5a45f12afa922ae7a70c7d8c284ae558ca6e8fe15c1c04b584861`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[10].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_native.py:123`; AST `d174e2c4a6fde548b6ae15749ff7fe27580af0a8eef961ee8a05290f2ecfa76c`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[10].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[11]::Assign

Source: `infra/agentinfra/roadmap_native.py:125`; AST `8b5909a31269d1106195cc34ba4dffe321e65fba972ea48c63c771c5f61ad1b9`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: metadata. Outputs/bindings: state.
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[12]::Assign

Source: `infra/agentinfra/roadmap_native.py:126`; AST `164f2802b8a64b12b19ecd66ed033239df9d1e6d622d024820bfc6a65cd012d9`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: INTERFACE_VERSION, context, executable, goal, is_process_ancestor, metadata, owner, process_handle, state, thread. Outputs/bindings: result.
Calls/effect boundaries: is_process_ancestor, process_handle, thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[12].value.values[10]::Call

Source: `infra/agentinfra/roadmap_native.py:130`; AST `cbc32985190de7c599a46bf438be757bb705188da58a8e6ec43ac269d291c758`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: owner, process_handle. Outputs/bindings: (none).
Calls/effect boundaries: process_handle.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].value.values[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[12].value.values[11]::Call

Source: `infra/agentinfra/roadmap_native.py:130`; AST `f9938fa034fd33d47ce7237308c114b4541a6bc6c65bc30f47e24f6c3db0dad3`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: is_process_ancestor, owner. Outputs/bindings: (none).
Calls/effect boundaries: is_process_ancestor.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].value.values[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[12].value.values[12]::Call

Source: `infra/agentinfra/roadmap_native.py:131`; AST `5b3dca0c4679dd3485adf0e32d5c8560f68e473c2ecc097320452b17d6ad1017`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: thread. Outputs/bindings: (none).
Calls/effect boundaries: thread.get.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[12].value.values[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[13]::Assign

Source: `infra/agentinfra/roadmap_native.py:135`; AST `ea550629d25e1f9e71896bf31374af5bfddb3e00134f1ff852e05146c14aecd2`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[13]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[13].value::Call

Source: `infra/agentinfra/roadmap_native.py:135`; AST `9ddec37ebb871d950d3273f3c19aaf26231ea1c560172aa64604b6f8dc8f2faf`.

Rust module: `infra::agentinfra::roadmap_native`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, result. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Call evaluation at root.body[14].body[13].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_native.py::module::observe_native_owner::root.body[14].body[14]::Return

Source: `infra/agentinfra/roadmap_native.py:136`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_native`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, json, locks, os, pathlib, roadmap_codex, roadmap_records, socket.

Invariants: Preserve ordered Return evaluation at root.body[14].body[14]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
