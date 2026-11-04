# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 265. Inventory digest: `02dbb6e7d30c447095f4124a54a8f4d794e19d6879c1b575f4c954c6c7f8fbba`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_mirrors.py::module::root::Module

Source: `infra/agentinfra/roadmap_mirrors.py:1`; AST `0582ce56537b76f46a62758d8b41db66cdaaddfb264a75e270110b3c2652b40c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, DNS_ENDPOINT, Exception, POLICY_PATH, Path, TRANSPORT, _MirrorHTTPS, _MirrorRedirect, _ResolvedConnection, _host, _save, _sources, all, any, atomic_write_json, c, chunk, code, confined_path, connection, count, created, deadline, dict, digest, directory, entry, enumerate, events, exc, field, file_binding, float, fp, getattr, hashed, hashlib, headers, host, hosts, int, isinstance, kwargs, len, list, maximum, message, min, name, newurl, opener, ordinal, output, partial, path, policy, provider, providers, quarantine, raw, read_download_policy, read_json, record, request, require, response, result, results, root, self, source, source_deadline, sources, ssl, str, super, target, time, type, urllib. Outputs/bindings: INTERFACE_VERSION, POLICY_PATH, TRANSPORT, c, chunk, count, created, directory, events, field, hashed, host, maximum, name, opener, ordinal, output, partial, path, policy, provider, providers, quarantine, raw, record, request, response, result, results, source, source_deadline, sources, target.
Calls/effect boundaries: ContractError, Path, _MirrorHTTPS, _MirrorRedirect, _ResolvedConnection, _host, _save, _sources, all, any, atomic_write_json, confined_path, digest, directory.mkdir, entry.get, enumerate, file_binding, getattr, hashed.hexdigest, hashed.update, hashlib.sha256, isinstance, len, min, opener.open, output.write, partial.exists, partial.open, partial.read_bytes, partial.replace, partial.unlink, policy.get, policy['providers'].get, provider.get, providers.items, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, read_download_policy, read_json, record.update, require, response.read1, results.append, self.do_open, source.get, ssl.create_default_context, str, super, super().__init__, super().redirect_request, target.exists, target.read_bytes, target.relative_to, target.relative_to(root).as_posix, target.stat, time.monotonic, type, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:1`; AST `601d73c88dd3eee00b25a1594f2d2dd8de2f4621dc09dc1f2265967dfd038879`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:6`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_mirrors.py:8`; AST `092cb77ae0770f1627b29bf41b2732722fbcc3a0e1d77a79674801800a2721d1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[3]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:9`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[4]::Import

Source: `infra/agentinfra/roadmap_mirrors.py:10`; AST `d58f4a781306aa988c2a48663bae1b9c9f8057e04c8f1f102adaea8473a930a5`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_mirrors.py:11`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[6]::Import

Source: `infra/agentinfra/roadmap_mirrors.py:12`; AST `6e0f76526c6d4c47fb54fd80b1a9075af18e040d8abcba786757ca55a9676c61`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[7]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:14`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[8]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:15`; AST `7d8935a43987e539073e796205400bb2723a491293e80c8ac449da85e20243ae`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[9]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:16`; AST `04c2b493d7617e4c4e7e694d6510665d9f63c32b1e1eab9ee5876ed334aa1b81`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_mirrors.py:17`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[11]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:20`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[12]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:21`; AST `f01623263eac515867d0ac7f4369d9a37df2382fb00ad7cabc7a8491fcba663e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: POLICY_PATH.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::root.body[13]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:22`; AST `caccd79fe09319bb16c13440dad7c9dff799452da22b2febb59cb0618b4e4113`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: TRANSPORT.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:25`; AST `42caac480b292ca34acd4dbb8f8b8c9f875a437d293d3f2c5177ec7634340b27`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: DNS_ENDPOINT, POLICY_PATH, Path, TRANSPORT, _host, confined_path, dict, field, host, int, len, maximum, name, policy, provider, providers, read_json, require, root, type. Outputs/bindings: field, host, maximum, name, policy, provider, providers.
Calls/effect boundaries: _host, confined_path, len, policy.get, provider.get, providers.items, read_json, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:26`; AST `8b9ca89c1deb4e89c1679c54b926784c69baf9e5ad496adac358050094599296`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, confined_path, read_json, root. Outputs/bindings: policy.
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:26`; AST `d081ebf732a5076ea80080077ee05eed0cc3e1dbe0afdab57a3ff72456cae974`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, confined_path, read_json, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, read_json.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:26`; AST `5bdd9b5c01bd125a424c1f9d0d39aae66e9ab63f6ce4889586c0ed8d993ed01e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, confined_path, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:27`; AST `051161b702adf1d74a55026833480f64b7c531bde3491aaea3ebbe24520f9b0b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: DNS_ENDPOINT, TRANSPORT, policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:27`; AST `e631e999294662fd47b4cbe43020b7925b86663df88091db6ccca0b44d362502`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: DNS_ENDPOINT, TRANSPORT, policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:27`; AST `4f4917a694d078dcde9a0b2b3f36334ce31176634b9e12cecc4a86db64cf7e07`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:27`; AST `4e74def8138f11b5dc1fc000ec795c3ecddb8a0f14fabb4232b5be09581e3abf`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:28`; AST `9e911179584dd5be2928514005977070ee1fb7c5879b9995fe6c5421f0f1b8b2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:29`; AST `031ffc3989b28d9f2446e7ffa55c0f27e294a5e8cadaa7062fd5011aac71e298`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[1].value.args[0].values[4].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:29`; AST `ed6c8035efc0eca1f4f68401f071e5314b56cc7c8c2c235b2aaaa46961e8f3d9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[1].value.args[0].values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[2]::For

Source: `infra/agentinfra/roadmap_mirrors.py:31`; AST `0ac4e67ca0a1426a07144785688f4087962c13962db9bb3dcb068466bd4a5428`.

Rust module: `infra::agentinfra::roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: field, int, maximum, policy, require, type. Outputs/bindings: field, maximum.
Calls/effect boundaries: policy.get, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[14].body[2]; no call, error or mutation may be omitted. Iteration: (field, maximum) in (('max_sources_per_artifact', 4), ('max_addresses_per_source', 4), ('socket_timeout_seconds', 20), ('source_timeout_seconds', 120), ('stage_timeout_seconds', 600), ('max_redirects', 8))
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[2].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:34`; AST `2cbd5d495743211535174ff1c86468f09b421fee3ccf32f3db0cfb3bcc949151`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: field, int, maximum, policy, require, type. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:34`; AST `7843080b95480e1fb162bcd8dede632caa2a8263ebc528cd730e772591802ce3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, int, maximum, policy, require, type. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[2].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:34`; AST `e17749fec9bd23b3c33c6c52dd93070ea53925a680d60e8aa7caafebcaa42eaf`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, policy, type. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[2].body[0].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:34`; AST `ef682d59f41199d9dba07191f563b3a4dd92424e2f4bdb4ea0bc016d7beec1d1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: field, policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[2].body[0].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:35`; AST `29ba64346807c64079997687d36de139e88d5d3cf479305a48aab23bd48bc402`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:35`; AST `677622799886d71587b58edf4a8383617f13958d2912de7cb4616c6cff5c477f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, require. Outputs/bindings: (none).
Calls/effect boundaries: policy.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:35`; AST `623960b07c83362ef8197e73e63b4e5a582dee2e113fe67042915f7fc82bdfe9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:35`; AST `e80a1ee8f8985d1c266f8b9c1a31167c265ef33418e65c11284048b519d729e6`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:36`; AST `b61810a3f60ded338723209ab9f8687b54c6fa7b961cb777c0537a5c5334dfe8`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[3].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:36`; AST `8fcc6c7dc66d4669e5c89b816db0eaff999f8df6ef06a1b6b01530764d209467`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[3].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[4]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:38`; AST `752829bfcfa26067e4523eac5ac56419fac9e8614f2527d9fe52009855192fa9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy. Outputs/bindings: providers.
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[14].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:38`; AST `c69b267dde35186dd3645cdeefb2b84dbd5a20dd389b113e0392cb5225f9adf3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: policy.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[5]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:39`; AST `a842e9f75d1bf988ecf0960bc89758aefbbbf5ffc7ea15708d957301a52c5133`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[5].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:39`; AST `647b031fc50b93f4d8fe5aeafb017172bbe83f010dc0d930d82ba66e8db5fa31`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, providers, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:39`; AST `9966409d264e50cc7c5d01400c9e72d834ef13356ac5d5d86eb4274bcddc249f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, providers. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6]::For

Source: `infra/agentinfra/roadmap_mirrors.py:40`; AST `f4bd241601e6fa3def512e7436704c1a5e88c5662ae766b3727592ee2f61c967`.

Rust module: `infra::agentinfra::roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _host, host, len, name, provider, providers, require. Outputs/bindings: host, name, provider.
Calls/effect boundaries: _host, len, provider.get, providers.items, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[14].body[6]; no call, error or mutation may be omitted. Iteration: (name, provider) in providers.items()
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].iter::Call

Source: `infra/agentinfra/roadmap_mirrors.py:40`; AST `70dd79814a7278caacf407d442888151bc4f8108fcabd5d37be54eeddf7bcdb1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: providers. Outputs/bindings: (none).
Calls/effect boundaries: providers.items.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:41`; AST `68a837acbf37b406487644d2ec742cb8fd5e8a2990e176768954e2057325cf17`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, name, provider, require. Outputs/bindings: (none).
Calls/effect boundaries: len, provider.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:41`; AST `3d53ce073c398b598ef92799ba3a90659369ce354d56c18032012439d2bc22d3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, name, provider, require. Outputs/bindings: (none).
Calls/effect boundaries: len, provider.get, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[0].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:41`; AST `60e7d3cf749f6a7e96c317bd644384783893c2316eb5bba6c643f4dc177577b2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: provider. Outputs/bindings: (none).
Calls/effect boundaries: provider.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[0].value.args[0].values[2]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:41`; AST `28db0b85d3726575881dac7556e6acd6f1b920bcaf1e2f677ee78c241f0999ca`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: provider. Outputs/bindings: (none).
Calls/effect boundaries: provider.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.args[0].values[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[0].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:41`; AST `25e403c90501d86a516f881b730c643d5b73db212ffbd149a9ed5357796acb2f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, provider. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[0].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[1]::For

Source: `infra/agentinfra/roadmap_mirrors.py:43`; AST `b427b1345ef510eaf4b50a5b8dd285f336c70c21150e1179a19a8a92fce7773e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _host, host, provider, require. Outputs/bindings: host.
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[14].body[6].body[1]; no call, error or mutation may be omitted. Iteration: host in provider['hosts']
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:44`; AST `5b11e9e08a4d9bde9282c752e99fa4cc4216b7e32a446c87c02b729c2ccd794b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, host, require. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[14].body[6].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:44`; AST `669b26ef24e04d663c3a7cfd398991fc13ea61fc72a110e1b8f75a069e618f89`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, host, require. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[6].body[1].body[0].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:44`; AST `6fcf09602bfaf2d81d1b13eff320fcc2ce643fdf397c2e956741a7dbdebc89a3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, host. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[14].body[6].body[1].body[0].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::read_download_policy::root.body[14].body[7]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:45`; AST `f38e8c7b49f49258700f63ece88446824ff7772f42414fe8c7662760c8476f35`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[14].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:48`; AST `c06dc1136bff7edbbd104a0d05a7362ef49c88db3ff3ba6b6eef906c473ce615`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _host, any, dict, entry, isinstance, len, list, policy, provider, require, source, sources. Outputs/bindings: provider, source, sources.
Calls/effect boundaries: _host, any, entry.get, isinstance, len, policy['providers'].get, require, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:49`; AST `718314200a720caf6740f9645eacea1620dd192d1f9bfd95be8ce9d5f223f674`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: sources.
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:49`; AST `066e55cbebd1524b32cfe7fcb07e9145df196ca13edceba4a16854bb3631a9a9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:50`; AST `c73de0c215324e4e30693cb10e5345ce691366e4c17916c816bdd8f79a18b040`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: isinstance, len, list, policy, require, sources. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:50`; AST `9b2ef5d67d7e29b21249cbdab133a83c25eae1822f2c7b67a2802a205a099e72`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, len, list, policy, require, sources. Outputs/bindings: (none).
Calls/effect boundaries: isinstance, len, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[1].value.args[0].values[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:50`; AST `edcedc4cf1234a959421819db5ae0a3258be23bd0cfd352054910c365c98c33b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: isinstance, list, sources. Outputs/bindings: (none).
Calls/effect boundaries: isinstance.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.args[0].values[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[1].value.args[0].values[1].comparators[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:50`; AST `e7bfad623b25d8d6f9b7382fe4bb3b4328c859b82faa67ca008d709c287d6534`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, sources. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[1].value.args[0].values[1].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `448422764586c9e0c420bacfc4ce34a7e41c9193891d9b6f0ea4983be823f29e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, require, source, sources. Outputs/bindings: source.
Calls/effect boundaries: len, require, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `624776c9c4e06b70f9cfa34d568a0d51d97ab756305eccde6aa7eca3700127dc`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, require, source, sources. Outputs/bindings: source.
Calls/effect boundaries: len, require, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `81846136bd1cbaee2e4d462737d7d198cd2864c767f3f1c3955b32d355e7efa3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, source, sources. Outputs/bindings: source.
Calls/effect boundaries: len, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2].value.args[0].left.args[0]::SetComp

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `6e43ffe7917d62873dbb4fc7f2a60c41f1c5beb9517c08c4dfd84b8d8d246ad2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: source, sources. Outputs/bindings: source.
Calls/effect boundaries: source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered SetComp evaluation at root.body[15].body[2].value.args[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2].value.args[0].left.args[0].elt::Call

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `dc5de0d7ec54d2d7298d41acb80a88e9323cd38a5e24165a587b08739ec49636`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.args[0].left.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[2].value.args[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:51`; AST `e7bfad623b25d8d6f9b7382fe4bb3b4328c859b82faa67ca008d709c287d6534`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, sources. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[2].value.args[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3]::For

Source: `infra/agentinfra/roadmap_mirrors.py:52`; AST `4484bd0785e8bc95fc5e432e889eca084c26d3b535ac4818121f1131d968e0af`.

Rust module: `infra::agentinfra::roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: _host, policy, provider, require, source, sources. Outputs/bindings: provider, source.
Calls/effect boundaries: _host, policy['providers'].get, require, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[15].body[3]; no call, error or mutation may be omitted. Iteration: source in sources
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:53`; AST `a6ff370f68f9823945d0e32a0decbd4ff41d8271510145d39a94a69dd843ab61`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, source. Outputs/bindings: provider.
Calls/effect boundaries: policy['providers'].get, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[15].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:53`; AST `74b61e9d6f398534e3b499077df2465998846a81e834a2a341e90ae196efd3b3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: policy, source. Outputs/bindings: (none).
Calls/effect boundaries: policy['providers'].get, source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:53`; AST `35109a930a0fd9c3c435277f32d6d0ff461c1611cf07a3df59966bfb44c5ad29`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source. Outputs/bindings: (none).
Calls/effect boundaries: source.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:54`; AST `f5aebe6a7291f80be08716b3b345a0dfb97efdebabaf5868d009c83d63fa1ad3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, provider, require, source. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:54`; AST `96463f20de4cc95457f44ec8035876212d81bcf9958143ffaded57c7662f3da1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, provider, require, source. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[3].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:54`; AST `601362324d5d185560a1b3a10dd3702c40e84af6c5acf5b187dbadaea8e1a326`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, source. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[3].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:55`; AST `afa31b1e23acf8d98f4947ae43452621949a1d609e30275e474c1da4486dec5a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: any, entry, require, source, sources. Outputs/bindings: source.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[15].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:55`; AST `bca74104a5c9e4657acd634adfed2bfc07c27b85980f6dc8bf01be8323f85a58`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, entry, require, source, sources. Outputs/bindings: source.
Calls/effect boundaries: any, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:55`; AST `54206bc218ca02350d16bde6ff5b8fb25eec898f87d1a1339f1448e3bd7cfe94`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: any, entry, source, sources. Outputs/bindings: source.
Calls/effect boundaries: any.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[15].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[4].value.args[0].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_mirrors.py:55`; AST `3b715bd5d97988f1a15ee6649eb88be40872d59d99066153e5da15da74f713c0`.

Rust module: `infra::agentinfra::roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: entry, source, sources. Outputs/bindings: source.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[15].body[4].value.args[0].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_sources::root.body[15].body[5]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:56`; AST `2fcae3a8b5f3b7a174bae6a688ed37f07c31e449ecad7e34788b1824e9d25fee`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: sources. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[15].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::root.body[16]::ClassDef

Source: `infra/agentinfra/roadmap_mirrors.py:59`; AST `981b2c97a69303f26cf4c08042567dce1c575182d5ca6833bcf99ae9a1574f19`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: _ResolvedConnection, _host, connection, deadline, dict, events, float, host, hosts, kwargs, list, policy, request, require, self, ssl, str, super, urllib. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection, _host, require, self.do_open, ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:60`; AST `08c266cf606d9f275486e8d73b05592595d10420a4bc9fbd483ccdc3fb7fd125`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: deadline, dict, events, float, hosts, list, policy, require, self, ssl, str, super. Outputs/bindings: (none).
Calls/effect boundaries: require, ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:61`; AST `28c59d6d549686f850af338c1c0df4aba17498a1ecd2b3696494e658ba97d588`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ssl, super. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:61`; AST `673721f26c0c1041a7656b3d0c36005c08a29b723ccf5c1e32bc78c0cba53745`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ssl, super. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:61`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[0].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:61`; AST `f328760be460c9f8eeedf6a290722b001ee67018c6508a414b3e66a1412ca187`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ssl. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:62`; AST `9d015b531dbc882edb8f54de27ac493872accaa5cc83ba62f260ae6a079520d0`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:62`; AST `5f77e53692fd7a75418337baabaabe14fc87906b208cf3e48a27031e6ab1913d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::__init__::root.body[16].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:63`; AST `630be2352798e7af8bd401441be8dad543982659325a893d4ab49e8b8dabf56a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, events, hosts, policy, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:65`; AST `ff16e8612fe91606eecb59c797005ba1027d00d8335b7c91208d8148de3de4c0`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _ResolvedConnection, _host, connection, host, kwargs, request, require, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection, _host, require, self.do_open.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:66`; AST `0d9dc2542bf8ae3c8cb83ce4c972ebb4459fc6abb026f82f5ef98d3af75cde82`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, request, require, self. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:66`; AST `3bae09873de91b1666ea4939a29b10f7ce45b0cef6f928cdae8f5c9037b8a075`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, request, require, self. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:66`; AST `4f2b36bff326252dbbc41b539966a912a26de3ae6b34533f2bcb7f1066827fc1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, request. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::connection::root.body[16].body[1].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:67`; AST `07eceb0db4cc9e05968d37a825b5ae2eda39e389837a035b73d6f2cee3de05aa`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::connection::root.body[16].body[1].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:68`; AST `d1f69b928526359eb7e2143ca1cdeebda810e2e3721a4ed279174bdf29a1ce9e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[16].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::connection::root.body[16].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:68`; AST `0597c800a89988069df4386f204cd2a9ec82fae0e609aa04996d4709e74fa410`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1].body[2]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:70`; AST `3ef4c47c9cea2ba4aaf94dda7110b4dde6a142684c023074d74e2226875ec67d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: connection, request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.do_open.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[16].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorHTTPS::https_open::root.body[16].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:70`; AST `b6311b473e46ef3561a3cab09bc5196bc479194b3cd7167a7858b0680418d8e8`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: connection, request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.do_open.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::root.body[17]::ClassDef

Source: `infra/agentinfra/roadmap_mirrors.py:73`; AST `8e519f6668c862b218aee40977c3936abbb79610951442ac22163c37ccea2a73`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: _host, code, count, fp, getattr, headers, hosts, int, list, maximum, message, newurl, request, require, result, self, str, super, urllib. Outputs/bindings: count, result.
Calls/effect boundaries: _host, getattr, require, super, super().redirect_request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::__init__::root.body[17].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:74`; AST `24886cb7316a8835ddb769c2277676d1e75eab0f3be7dfab9e54853dff010b99`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: hosts, int, list, maximum, self, str. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::__init__::root.body[17].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:75`; AST `d61c06ac220b4c9f90b05d1ebc399925c86d469c2333d32fa6015e9df6678b6a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hosts, maximum, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:77`; AST `5b7da902a952e4524060b58a648e54cb410c515e3f415a4779557c34264dd036`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _host, code, count, fp, getattr, headers, message, newurl, request, require, result, self, super. Outputs/bindings: count, result.
Calls/effect boundaries: _host, getattr, require, super, super().redirect_request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:78`; AST `4511735b3229548a5d5e0c100bf457cec12dedec61a6cff91b610e561b071faa`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: getattr, request. Outputs/bindings: count.
Calls/effect boundaries: getattr.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[0].value.left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:78`; AST `9968d80d738fd3139036dabb97e3de9281e8ae64b1b4e14aeab6a7043dcc1b4e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: getattr, request. Outputs/bindings: (none).
Calls/effect boundaries: getattr.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[0].value.left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:79`; AST `140f797683f8b891b88bcea908906e5488d9137f15dab24cf1dfcc90b93c13aa`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, count, newurl, require, self. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:79`; AST `af6311073a2fd549181f66569c83b8f1191f7f33e63883073bb1b052225cc25d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, count, newurl, require, self. Outputs/bindings: (none).
Calls/effect boundaries: _host, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[1].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:79`; AST `c8e611368eb9aee1230e4b78187dd40046ca5ff160393305780a35669b70aec0`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, newurl. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[1].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:80`; AST `f062bf2e0680dc6a99539cdd504e10d7dcc58e3faa65e5111d3047c072a1a2f9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: code, fp, headers, message, newurl, request, super. Outputs/bindings: result.
Calls/effect boundaries: super, super().redirect_request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:80`; AST `c30f6cefe80f9727a8be9a2591b2b9122764859f6cdb8fc8b0965138e8ba0498`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: code, fp, headers, message, newurl, request, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().redirect_request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:80`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[3]::If

Source: `infra/agentinfra/roadmap_mirrors.py:81`; AST `0468fccf623e4678406de2a67d5099631ad320b0fcf4f358311f29436122b467`.

Rust module: `infra::agentinfra::roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: count, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[17].body[1].body[3]; no call, error or mutation may be omitted. Condition: result is not None
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[3].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:82`; AST `d927c1f51e6597ddc3be0ba8d188bd0e68de194d52f662c15b0469e1bc8e3389`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_MirrorRedirect::redirect_request::root.body[17].body[1].body[4]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:83`; AST `7b1d642d8354b03513d85ddd38bf4e4911c5b147b5b68f50fd12c2072903af3e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: result. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[17].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:86`; AST `a59319de29524b4a942c08329beacca7420385082e03c195f5540e155017da85`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Path, atomic_write_json, confined_path, dict, digest, directory, name, path, record, root, str. Outputs/bindings: path.
Calls/effect boundaries: atomic_write_json, confined_path, digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:87`; AST `417dd15754a40a0122e0a9d7403119aafa915f00aa7413efbc32501494e1a029`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, digest, directory, name, record, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:87`; AST `24e1a90778066efca36a63c6b8771320931bc339f81ca4ec1d91fe195854986d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, digest, directory, name, record, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18].body[0].value.args[1].right.left.right::Call

Source: `infra/agentinfra/roadmap_mirrors.py:87`; AST `459942b3b031c512f2c84b1ead1f069f2c56349cbb6bb8b33eba095d39132ca1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, record. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].value.args[1].right.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:88`; AST `d3ee4284259ef941c72453e8cb501ef3ec2d05a4c853482f268a0d8521272ff1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, path, record, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::_save::root.body[18].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:88`; AST `41590da26c325f336c9fe438b4801b88bd719ea2164bd09c6dfa9d4a24e3e2e3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, path, record, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19]::FunctionDef

Source: `infra/agentinfra/roadmap_mirrors.py:91`; AST `228419d70169a3b611c78e6aaf47c3ce1b96dc9923a60892a8373666d38aac27`.

Rust module: `infra::agentinfra::roadmap_mirrors`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, Exception, POLICY_PATH, Path, TRANSPORT, _MirrorHTTPS, _MirrorRedirect, _save, _sources, all, c, chunk, confined_path, count, created, deadline, dict, digest, directory, entry, enumerate, events, exc, file_binding, float, hashed, hashlib, int, len, min, name, opener, ordinal, output, partial, policy, provider, quarantine, raw, read_download_policy, record, request, require, response, results, root, source, source_deadline, sources, str, target, time, type, urllib. Outputs/bindings: c, chunk, count, created, directory, events, hashed, name, opener, ordinal, output, partial, policy, provider, quarantine, raw, record, request, response, results, source, source_deadline, sources, target.
Calls/effect boundaries: ContractError, Path, _MirrorHTTPS, _MirrorRedirect, _save, _sources, all, confined_path, digest, directory.mkdir, entry.get, enumerate, file_binding, hashed.hexdigest, hashed.update, hashlib.sha256, len, min, opener.open, output.write, partial.exists, partial.open, partial.read_bytes, partial.replace, partial.unlink, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, read_download_policy, record.update, require, response.read1, results.append, str, target.exists, target.read_bytes, target.relative_to, target.relative_to(root).as_posix, target.stat, time.monotonic, type, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:92`; AST `b8c698167f53cfcbb73b33dbc1dbcdb600318f8828f2a29f7c5134f24331cb52`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[1]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:93`; AST `98516a7de4138ab12872e217b2c4a2af08ad738c715304bc9790307e7d6f39d5`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: read_download_policy, root. Outputs/bindings: policy.
Calls/effect boundaries: read_download_policy.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:93`; AST `d98a9d8f02719fd4afc66431e19bae5e085c1a1947d40c1d0c9c099b5cc2ace2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: read_download_policy, root. Outputs/bindings: (none).
Calls/effect boundaries: read_download_policy.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[2]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:94`; AST `87726df907f5d9b9bf5214add959011842db6cf696f965943d614e00de5cf78c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _sources, entry, policy. Outputs/bindings: sources.
Calls/effect boundaries: _sources.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:94`; AST `1eb532fcf6677242b9d7c1b338bd30a19d58f6d262fd94263b69f4d0bbdc385f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _sources, entry, policy. Outputs/bindings: (none).
Calls/effect boundaries: _sources.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[3]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:95`; AST `d3e0463539b1ef9cfac4bec9f6bd6273d9fad504f4c0bdee22a51160debc0ba2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[3].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:95`; AST `aa776f971c22a60f51c5526e73c57c433bbdbc33b0e1922a81a6fc02b06515c9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:96`; AST `3a400253aadde423a42d9e21da0e9ba55a3fe64614ae692874cebc9a5aa91183`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:96`; AST `7f8492ad27b11def9f8bffa8aea0180c657a9152ccc4f6a4269a7601584575c2`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[5]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:97`; AST `19e0a0458a4fd373331a20d625c9a051a8d23cb65505a804f560158f0eebddbe`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: name.
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[5].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:97`; AST `17d52058ee440ee1c93717819decf0a775a22713e205dba2d545e8f7ea0a9a6f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[5].value.args[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:97`; AST `c8cf4beccb27bd62561b11a710c92c61ca7031556f3dfb4230194d3f554a1e74`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[5].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[6]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:98`; AST `f4e49dc0fb602cc8c7836e781f0f1977281482cba50f483bfb5e5f9222688481`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, name, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[6].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:98`; AST `7fe2ff1d1225e8aa147331d0b4b3e7c60f239ea7a4da8406bbaaa48c4b9779c1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, name, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[6].value.args[0].values[1].left.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:98`; AST `e0661b96e847fdc1e815fc151ea8a6312b949d1130816c8cc00ae7f50185573c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, name. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[6].value.args[0].values[1].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `bc7cea038c2b38cfbc61e1aa93d945b77571e32da46b1ab3fbe464e7e201a6fa`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: all, c, entry, int, len, require, type. Outputs/bindings: c.
Calls/effect boundaries: all, entry.get, len, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `2e6e5e1e82f4dbe05f444c1d1ed260966ccdd521911a81f782687aae3506ad8d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, entry, int, len, require, type. Outputs/bindings: c.
Calls/effect boundaries: all, entry.get, len, require, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `bedaf1a36d8d484f9c90d3866c47785b4b6d9aa4ca234478b88a1c8e8040e69d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, type. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `7d57584f29ddf6571676cbc58a8cd5e3f1b1b2209f643e126c57285ebf1b63d4`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `c3b87fba03a280865b38ce381eeb4aa4f9789270e0bc38562d9cd1b9440f1f79`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, len. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[2].left.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:99`; AST `cb40855f69a0668cd11f1f0837c9eaad256acf5cb05da79bc2282323392e24d3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.args[0].values[2].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:100`; AST `aafedf2f1b421a91361bb7e4e9052077da52098d6b80b5cb2a9f70446c17db78`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: all, c, entry. Outputs/bindings: c.
Calls/effect boundaries: all.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[7].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[7].value.args[0].values[3].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_mirrors.py:100`; AST `a0c27ac0ae702cc21787ad3ba0d528c68d5476c6d58755922de374538057e12a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: c, entry. Outputs/bindings: c.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[19].body[7].value.args[0].values[3].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[8]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:101`; AST `40bc463c209e8b5edceeab57427960be7bc2fd2dc6c3075373dd84c89e841c54`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, policy, require, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[8].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:101`; AST `923eb8871bd7296b5823482637c70720ee93c9c400e0dbcdd6b59e339a46e146`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, policy, require, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[8].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:101`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[8].value.args[0].values[1].left.right::Call

Source: `infra/agentinfra/roadmap_mirrors.py:101`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[8].value.args[0].values[1].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[9]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:103`; AST `402ce818e721be7dbd33a8a523cb2d5970b0efb3c7a0b5fcff2f9a5686fb3456`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, name, root. Outputs/bindings: target.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[9].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:103`; AST `cc071144396d66b7522cae0f953c524619cf3ab5e197a9630a22c22dff28195c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10]::If

Source: `infra/agentinfra/roadmap_mirrors.py:104`; AST `9c9ffc958ab7af4de0a12dd96996c0500333d8fb55202dada343c5314470d6ea`.

Rust module: `infra::agentinfra::roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: digest, entry, require, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, require, target.exists, target.read_bytes, target.stat.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[19].body[10]; no call, error or mutation may be omitted. Condition: target.exists()
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].test::Call

Source: `infra/agentinfra/roadmap_mirrors.py:104`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:105`; AST `425bbcc2d1bb5397bc2aed92187ef7564e09f108ce8ce05cd902dce4ec8c0a10`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, entry, require, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, require, target.read_bytes, target.stat.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[10].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:105`; AST `f4f5c089092c5ab4ff843f843e979ec2437397b74450219be3eaa42ebba829fb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, entry, require, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, require, target.read_bytes, target.stat.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[0].value.args[0].values[0].left.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:105`; AST `2ecd8b29f47d7764f5897ac99ba24c990a22d66fc85e0ba6eb5543c15258a865`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.stat.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].value.args[0].values[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:105`; AST `3ad3dee046217dc4ee3b2f99ccda41115ef05e1a3ddb207b6c8951280bee2830`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, target. Outputs/bindings: (none).
Calls/effect boundaries: digest, target.read_bytes.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[0].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:105`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[10].body[0].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[10].body[1]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:106`; AST `ba7aee57225013aa5eb8d1f77060c02dae8d2fd452a43950ecaf458982a136d7`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[19].body[10].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[11]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:107`; AST `22db4c1a505af52193564f42b387b3d0022747f08b16e68836ec99078f026c4d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: results.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12]::For

Source: `infra/agentinfra/roadmap_mirrors.py:108`; AST `4179c7e1fda4531b29bd4a4a308387fafc81e4994abe5e3dfd5e758a64405133`.

Rust module: `infra::agentinfra::roadmap_mirrors`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: Exception, POLICY_PATH, TRANSPORT, _MirrorHTTPS, _MirrorRedirect, _save, chunk, confined_path, count, created, deadline, digest, directory, entry, enumerate, events, exc, file_binding, hashed, hashlib, len, min, name, opener, ordinal, output, partial, policy, provider, quarantine, raw, record, request, require, response, results, root, source, source_deadline, sources, str, target, time, type, urllib. Outputs/bindings: chunk, count, created, events, hashed, opener, ordinal, output, partial, provider, quarantine, raw, record, request, response, source, source_deadline.
Calls/effect boundaries: _MirrorHTTPS, _MirrorRedirect, _save, confined_path, digest, enumerate, file_binding, hashed.hexdigest, hashed.update, hashlib.sha256, len, min, opener.open, output.write, partial.exists, partial.open, partial.read_bytes, partial.replace, partial.unlink, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update, require, response.read1, results.append, str, target.exists, target.relative_to, target.relative_to(root).as_posix, time.monotonic, type, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[19].body[12]; no call, error or mutation may be omitted. Iteration: (ordinal, source) in enumerate(sources)
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].iter::Call

Source: `infra/agentinfra/roadmap_mirrors.py:108`; AST `6b8837bd970594e7e14594e09a72de74d09e9a20ad0fcfcdab365788907ebc8e`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: enumerate, sources. Outputs/bindings: (none).
Calls/effect boundaries: enumerate.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:109`; AST `64bcf5e6da7598961c11297d6c3d1618e7f0319991f4149531616e34ec62d333`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, require, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:109`; AST `c62fd1da219a3d5844360e3f16f21ffbe45a5e7cf00f7892a8aa60abc24bcd65`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, require, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:109`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[1]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:110`; AST `9f66f5eaeb66b75aad0161e1078b309f21451afbef25325d95ab015a90e3137d`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: created, events.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[2]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:111`; AST `a60d4a5844a01034a7892a894958ffb6d7bd1c02eccc8416df6cfb1b04366881`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, name, ordinal, root, str. Outputs/bindings: partial.
Calls/effect boundaries: confined_path, str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:111`; AST `a58668d5c15fa6ccda0fca16fb63a097bb21cce98a5e2f7e8f65a1b2fe220cbd`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, name, ordinal, root, str. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[2].value.args[1].right.left.right::Call

Source: `infra/agentinfra/roadmap_mirrors.py:111`; AST `2849625895b97f7c392f3eac36a38d282e68d14f6af133e0c874bb5566e99e70`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ordinal, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[2].value.args[1].right.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[3]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:112`; AST `0082ba6fbf57774475d497fdea4187d4015af72767fa5e21eedf0d5cae562c4a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, require. Outputs/bindings: (none).
Calls/effect boundaries: partial.exists, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[3].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:112`; AST `286d2d2c70fe51e76cf5559cf65025cf1114eba5f7c9d44f3fbfd1ee91544a6f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, require. Outputs/bindings: (none).
Calls/effect boundaries: partial.exists, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[3].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_mirrors.py:112`; AST `8cbf3aead02eaa20e373f530b2eab77766a8dc73f76131e459dff4d11ed50f66`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[3].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[4]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:113`; AST `16e8c019d5e459d89498afd4369660d751142965c947f4055923c68d0a1f963a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, min, policy, time. Outputs/bindings: source_deadline.
Calls/effect boundaries: min, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:113`; AST `8bc421ed603dac52caa5c56bcd2b81e73024cef92bcecdf0048d082912edfb52`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: deadline, min, policy, time. Outputs/bindings: (none).
Calls/effect boundaries: min, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[4].value.args[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:113`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[4].value.args[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[5]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:114`; AST `55119e70ad0bca6497b6fa9dc080f6f6745c2f0fad8d9f3adffacdacf6bae427`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: policy, source. Outputs/bindings: provider.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[6]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:115`; AST `9551e6f4ed20d262f047bad58bfc96d2512ca4ae9295a97e405ae588cb8b9c0c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: POLICY_PATH, TRANSPORT, entry, events, file_binding, root, source. Outputs/bindings: record.
Calls/effect boundaries: file_binding.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[6].value.values[7]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:117`; AST `1a9ca2b5eb30c0a2bc5aa9be66def389cd27a25af016bbdf2c99077c8dd32a7f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: POLICY_PATH, file_binding, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[6].value.values[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7]::Try

Source: `infra/agentinfra/roadmap_mirrors.py:118`; AST `091cbdce1fee3a1c3979798327f40cbac5a1b6bed7341e117dae6407be568e39`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, _MirrorHTTPS, _MirrorRedirect, _save, chunk, confined_path, count, created, digest, directory, entry, events, exc, file_binding, hashed, hashlib, len, name, opener, output, partial, policy, provider, quarantine, raw, record, request, require, response, results, root, source, source_deadline, target, time, type, urllib. Outputs/bindings: chunk, count, created, hashed, opener, output, quarantine, raw, request, response.
Calls/effect boundaries: _MirrorHTTPS, _MirrorRedirect, _save, confined_path, digest, file_binding, hashed.hexdigest, hashed.update, hashlib.sha256, len, opener.open, output.write, partial.exists, partial.open, partial.read_bytes, partial.replace, partial.unlink, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update, require, response.read1, results.append, target.exists, target.relative_to, target.relative_to(root).as_posix, time.monotonic, type, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Try evaluation at root.body[19].body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:119`; AST `954b1a53d96e45df1069f56df40be765390ce9dfcc1d93c4bec9eb1a6bd36d1a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _MirrorHTTPS, _MirrorRedirect, events, policy, provider, source_deadline, urllib. Outputs/bindings: opener.
Calls/effect boundaries: _MirrorHTTPS, _MirrorRedirect, urllib.request.ProxyHandler, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:119`; AST `726f412446c78592adefc29b3a427689645531acccaa888feb368933bb5e3f8a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _MirrorHTTPS, _MirrorRedirect, events, policy, provider, source_deadline, urllib. Outputs/bindings: (none).
Calls/effect boundaries: _MirrorHTTPS, _MirrorRedirect, urllib.request.ProxyHandler, urllib.request.build_opener.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[0].value.args[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:119`; AST `0086d7b8075371bb1d7ec3a29ffaeaf0124a924b0d1be31466cd7dfc271e752c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.ProxyHandler.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:120`; AST `94cc48fe6f18457ccda5ba9bdb878a3b3b8bbc74c54c925d85f0b11ba0071450`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _MirrorHTTPS, events, policy, provider, source_deadline. Outputs/bindings: (none).
Calls/effect boundaries: _MirrorHTTPS.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[0].value.args[2]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:121`; AST `7d332dbb957c5e3425b77ca16bc0d92f8efae611873c704d2e45a4bc5eb8e787`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _MirrorRedirect, policy, provider. Outputs/bindings: (none).
Calls/effect boundaries: _MirrorRedirect.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[0].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[1]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:122`; AST `2f1e5f38af4f5950e98ea8c1e5ebd5a61e156e392052c83b2ca1c447e04de90b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: source, urllib. Outputs/bindings: request.
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:122`; AST `f3129863a963e279d6034f5459314dcfd5c7a3dbd5c907393121b28827cc63ba`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: source, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[2]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:124`; AST `5d2ae2540f7ccb509b7f248bacd05d5eaab58355b3108d9cc44bc1634a6dad48`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: hashlib. Outputs/bindings: count, hashed.
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[2].value.elts[0]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:124`; AST `46ef61fb8c7d09a7bf845569bbc8968c05c256379ed5433a5aca1ba6d226695f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashlib. Outputs/bindings: (none).
Calls/effect boundaries: hashlib.sha256.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[2].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3]::With

Source: `infra/agentinfra/roadmap_mirrors.py:125`; AST `3a4fd6359a85de5c6101096400ebfc6c7bb10c27d29e840c8db81773fe846441`.

Rust module: `infra::agentinfra::roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: chunk, count, entry, hashed, len, opener, output, partial, policy, request, require, response, source_deadline, time. Outputs/bindings: chunk, count, created, output, response.
Calls/effect boundaries: hashed.update, len, opener.open, output.write, partial.open, require, response.read1, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[19].body[12].body[7].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_mirrors.py:125`; AST `cd1fc77b5089853496bfee581bdf5cf466a2cb4ce43d70b74275045f6596da2a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, policy, request. Outputs/bindings: (none).
Calls/effect boundaries: opener.open.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0]::With

Source: `infra/agentinfra/roadmap_mirrors.py:126`; AST `f6ee4ec15d787f7ef41e4306e3d6dedea90179ea50713379762fbc10f29f5bfe`.

Rust module: `infra::agentinfra::roadmap_mirrors`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: chunk, count, entry, hashed, len, output, partial, require, response, source_deadline, time. Outputs/bindings: chunk, count, created, output.
Calls/effect boundaries: hashed.update, len, output.write, partial.open, require, response.read1, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[19].body[12].body[7].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_mirrors.py:126`; AST `92f388e9646ee4657b38dfa4bd0c9d93c0b1ad88a241b1b3eccdb08cabd90143`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.open.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:127`; AST `27117513a62fd2e6e15606dccb9ae27b498e76ce5b8557a3e46b99f4743f3a32`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: created.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1]::While

Source: `infra/agentinfra/roadmap_mirrors.py:128`; AST `26012b1315f70b596112d96318478e44f54d00f6fb8f06db9977e3fa8effe017`.

Rust module: `infra::agentinfra::roadmap_mirrors`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: chunk, count, entry, hashed, len, output, require, response, source_deadline, time. Outputs/bindings: chunk, count.
Calls/effect boundaries: hashed.update, len, output.write, require, response.read1, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered While evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1]; no call, error or mutation may be omitted. Condition: True
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:129`; AST `11ea19e13fe705d3e24dcab885dfb1d9645aa475ceb40e3bda2b7b2946cb2af1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, source_deadline, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:129`; AST `659a1aa1c926556b214aa77652fe9e5f1d12efde506a26fd5cdfdc38bbf8e4f7`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, source_deadline, time. Outputs/bindings: (none).
Calls/effect boundaries: require, time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:129`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:130`; AST `01388335d0cc65145945338a6dae4a4b7ca5656020ff5f50ad19b83c0cab23fc`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: response. Outputs/bindings: chunk.
Calls/effect boundaries: response.read1.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:130`; AST `486bfa5f84495dd85edcebcdd914f0d2e78f3ffd95ada51e13d859d268be2f09`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response.read1.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[2]::If

Source: `infra/agentinfra/roadmap_mirrors.py:131`; AST `f84dd423a781f5e574b9f7a1f7392884bd07a02891b07e8df1240c51081ed583`.

Rust module: `infra::agentinfra::roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: chunk. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[2]; no call, error or mutation may be omitted. Condition: not chunk
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[2].body[0]::Break

Source: `infra/agentinfra/roadmap_mirrors.py:132`; AST `c0d25d96e6146e7b648417b86bf6bbfedd0a458099247cf2cd469124da4c9fec`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Break evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[3]::AugAssign

Source: `infra/agentinfra/roadmap_mirrors.py:133`; AST `18bcba3de3adda48da4f4c2e4b2317f2e1615e978aee1fdcbef98e021a6f6c02`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, len. Outputs/bindings: count.
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered AugAssign evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:133`; AST `6f99d4ecb2708ba92e74d7c76fd9b2c1d7b1aa91d619b54799b549e649104fc3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:134`; AST `482e054dece6da57bb20b194d4852bbb1af8cb24fcdbbf240691cc45ea92430f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, hashed. Outputs/bindings: (none).
Calls/effect boundaries: hashed.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:134`; AST `b08f1da57fd70880d1d9f08f7e120e581e3ac0076c0166214a46dc8bf68427ae`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, hashed. Outputs/bindings: (none).
Calls/effect boundaries: hashed.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[5]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:135`; AST `9c802f4657e8e7d7607ed61235070098592ebe3b89265147793dd56aa51c617c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[5].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:135`; AST `190360950a5fd203e4c19531c04f75f94bc12254565043396c7251615d294d97`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[6]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:136`; AST `5b9720c9bee8347a04a755fb211d21ac07ec37d01120d4cb42081ec943b93f56`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[3].body[0].body[1].body[6].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:136`; AST `81d5d403d3ef72138e8f5cb3c1e11ce3b23c62358a2679395188a44e224025d9`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[3].body[0].body[1].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:137`; AST `b56fcb78707afdf25672f0dafbc5264c73a6fdc61bde6b133c8bb34361d61955`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, hashed, record. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest, record.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:137`; AST `ee6472b40716f31fa1cd282589b492cca51628d4f6b408e1482137d30651229c`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, hashed, record. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest, record.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[4].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:137`; AST `429bf1063cc0186d561b9173ea78e26b0f1ccbd888ae1bf86c8b10aabc247e50`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashed. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[4].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[5]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:138`; AST `5d53fe4a85757e3800edfcd901f60b177e68d405e949f48445264a06c38eaba8`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, entry, hashed, require. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[5].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:138`; AST `637765f0d422c2cbfac71cce0108d4b36304471eec056df007c5a19b7f159621`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, entry, hashed, require. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[5].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:138`; AST `429bf1063cc0186d561b9173ea78e26b0f1ccbd888ae1bf86c8b10aabc247e50`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: hashed. Outputs/bindings: (none).
Calls/effect boundaries: hashed.hexdigest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[5].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[6]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:139`; AST `0f9704ad9ec67c5268c5d9527db346f1499118ea918f504c0c86127338a1eefb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[6].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:139`; AST `d46f8d171cc48fc29a5e567eb00ffda6d4d879a3102092c328fa0a97aa0283f8`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[6].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_mirrors.py:139`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[6].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[7]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:140`; AST `2d0feac56e67f48b48fc455b246fa938a8ae899e415163b65008e14d20533a81`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, target. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[7].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:140`; AST `e34e3e3e47d4a1857d5e745199738f4cb8aede3e0fa513420b19bc2862d82a97`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, target. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[8]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:141`; AST `19384e8f806a54a07d528657743702544587dfd0ad8cc3bb40997ecc03cf1994`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: file_binding, record, root, target. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, record.update, target.relative_to, target.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[8].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:141`; AST `3c4b290a1f6a890ef712bd9f21dcb8a29f87af2c0e036cb59d11f6065ac3d268`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, record, root, target. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, record.update, target.relative_to, target.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[8].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:141`; AST `64a54a3ab4aace227b6fd10315b246f9dba3ff41222b2ad3f6d92034209f062b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, root, target. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, target.relative_to, target.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[8].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[8].value.keywords[1].value.args[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:141`; AST `06b516eecc61f6f21156d1e06f8de045cbf83c558d758b2898ec3d669ac263dd`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, target. Outputs/bindings: (none).
Calls/effect boundaries: target.relative_to, target.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[8].value.keywords[1].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[8].value.keywords[1].value.args[1].func.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:141`; AST `ea5d4c93f9f1daaf4c30b187da7e0bb28b312ed38010f08d4527034161e05516`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, target. Outputs/bindings: (none).
Calls/effect boundaries: target.relative_to.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[8].value.keywords[1].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[9]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:142`; AST `a06c067ce3eac7a02b7b06b17620888e2dacc402639ea2c15ce9d0bad1b82655`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _save, directory, name, record, root. Outputs/bindings: (none).
Calls/effect boundaries: _save.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[9].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:142`; AST `fed29693b66e7b4b35a43aa4d72d7f20089997c05e1db5b052e07f5a1658e356`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _save, directory, name, record, root. Outputs/bindings: (none).
Calls/effect boundaries: _save.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].body[10]::Return

Source: `infra/agentinfra/roadmap_mirrors.py:143`; AST `ba7aee57225013aa5eb8d1f77060c02dae8d2fd452a43950ecaf458982a136d7`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[19].body[12].body[7].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_mirrors.py:144`; AST `fdf73bc4c068989c4ab1f485b7e26d5d1ca222eae0235a08a0fe78ba4d0745bc`.

Rust module: `infra::agentinfra::roadmap_mirrors`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, _save, confined_path, created, digest, directory, exc, file_binding, len, name, partial, quarantine, raw, record, require, results, root, source, target, type. Outputs/bindings: quarantine, raw.
Calls/effect boundaries: _save, confined_path, digest, file_binding, len, partial.exists, partial.read_bytes, partial.replace, partial.unlink, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update, require, results.append, target.exists, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[19].body[12].body[7].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:145`; AST `24566649d9a123b7bd773713970772c04cf89d97325e5ba037299600bb55be98`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:145`; AST `ceef1f9a63ad0cb68e75cc9046d7a2e3691525f889240af9b1b8b18b92408a59`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, target. Outputs/bindings: (none).
Calls/effect boundaries: require, target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[0].value.args[0].operand::Call

Source: `infra/agentinfra/roadmap_mirrors.py:145`; AST `65a9b6c938dd41ce241a38e5ad89154925bfb2a60b6a4960ec27b7239156acdb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[0].value.args[0].operand; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:146`; AST `fc6d08dce645f552fab8afc51da38df9deb044aa560ee31fb4ab49178d3f4b15`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.update, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:146`; AST `4591afb4059728efbca715e27ee3cf4e6eaaa35327fcbc9f0d29cb8d79d74171`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, record, type. Outputs/bindings: (none).
Calls/effect boundaries: record.update, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[1].value.keywords[1].value.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:146`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[1].value.keywords[1].value.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2]::If

Source: `infra/agentinfra/roadmap_mirrors.py:147`; AST `dd5cf3afaf00c14f447cf21be974ecf628aa1644aa89929e48416ece555158b8`.

Rust module: `infra::agentinfra::roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: confined_path, created, digest, directory, file_binding, len, name, partial, quarantine, raw, record, require, root. Outputs/bindings: quarantine, raw.
Calls/effect boundaries: confined_path, digest, file_binding, len, partial.exists, partial.read_bytes, partial.replace, partial.unlink, quarantine.exists, quarantine.parent.mkdir, quarantine.read_bytes, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[19].body[12].body[7].handlers[0].body[2]; no call, error or mutation may be omitted. Condition: created and partial.exists()
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].test.values[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:147`; AST `8cbf3aead02eaa20e373f530b2eab77766a8dc73f76131e459dff4d11ed50f66`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].test.values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:148`; AST `acbc87b0f524295c1afd842c03763486fb8ff98841550d731d68f15064b46ae4`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial. Outputs/bindings: raw.
Calls/effect boundaries: partial.read_bytes.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:148`; AST `036cf7dddaf576ab4be59cf3ea4fc55cafb37cfe12cfe42e258ae18502a59d30`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[1]::Assign

Source: `infra/agentinfra/roadmap_mirrors.py:149`; AST `870bd4ba716c33c3ef7c2f2276bd7404665565bff2ce4af94a9ae33a1208a362`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, digest, directory, name, raw, root. Outputs/bindings: quarantine.
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:149`; AST `f4040b0e8a327b80c3a6d6508b6a177f0b250b913a1c0b8ebde9e4d831ea0d1a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, digest, directory, name, raw, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path, digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[1].value.args[1].right.left.right::Call

Source: `infra/agentinfra/roadmap_mirrors.py:149`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[1].value.args[1].right.left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[2]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:150`; AST `765eec377596dc8670de763dac626a3cf18d123d1e2f05cb7e10cb5c567ee814`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: quarantine. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.parent.mkdir.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:150`; AST `9f1fe334e26f590bf0b36f8f3aeb4332a21bd2d915ba70c9d5740a855969670a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.parent.mkdir.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3]::If

Source: `infra/agentinfra/roadmap_mirrors.py:151`; AST `996bb504f1882bc7df8c7c6bdc084928515db3e9c63d0fce2973e9f81dd1363b`.

Rust module: `infra::agentinfra::roadmap_mirrors`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: partial, quarantine, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace, partial.unlink, quarantine.exists, quarantine.read_bytes, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3]; no call, error or mutation may be omitted. Condition: quarantine.exists()
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].test::Call

Source: `infra/agentinfra/roadmap_mirrors.py:151`; AST `d7be5e17beb640ea1d6422e78cba5469834d711e2f02265640fe957b608aaa96`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.exists.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:152`; AST `1d19ce09c3c1290a17887a516b7593575f336b267f464e7443fad9f5698154f1`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: quarantine, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.read_bytes, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:152`; AST `51b3944840505a14ef675d9f03d5237f3a283d37c115dd362105f0b5f75db373`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.read_bytes, require.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_mirrors.py:152`; AST `a02e4701a421dc1db710d069758021c383ec7d6dd14267ecd096618dc2e55c55`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.read_bytes.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[0].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[1]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:153`; AST `22e4fb708920f4df472750b506bc8df9a1ac66993747ba5782d5eb79569ce212`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.unlink.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:153`; AST `e947d95510b1f238a23ed7803a95db47aec3ba739daa1be4f166bafcba87d82a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.unlink.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].orelse[0]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:155`; AST `c0efa4cdfa4569232c796513a11a0099fbb31e4fb3e4ded56d47268328ef1573`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, quarantine. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].orelse[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[3].orelse[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:155`; AST `3868641e497be0b187e2d71db599062b5c0c5cb60c9715987ed95e775a23203f`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, quarantine. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[3].orelse[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:156`; AST `05d6050fedc766c45eb0b713806f50e50a3d42e2073684e5839f25fbd6bdfccc`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, file_binding, len, quarantine, raw, record, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, file_binding, len, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:156`; AST `814df82164e130f70ae50afc3b97a22234205d986a6a05466e9eefd161c5b846`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, file_binding, len, quarantine, raw, record, root. Outputs/bindings: (none).
Calls/effect boundaries: digest, file_binding, len, quarantine.relative_to, quarantine.relative_to(root).as_posix, record.update.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:156`; AST `a984e60fdf094e8e9ca9096c40df3ba1c810c65d3cf6c87b4fe3122a9d32f492`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, quarantine, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, quarantine.relative_to, quarantine.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value.args[1]::Call

Source: `infra/agentinfra/roadmap_mirrors.py:156`; AST `2fe01ec8d376f86d221f148e9bd9e6a088cc6f4dde81042bc71f4254deb085f3`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine, root. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.relative_to, quarantine.relative_to(root).as_posix.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value.args[1].func.value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:156`; AST `de45c3fe276aba87c195aa25c623d19f94e52d4d8600c058c78e1f025428164a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: quarantine, root. Outputs/bindings: (none).
Calls/effect boundaries: quarantine.relative_to.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[0].value.args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:157`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[2].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:157`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[2].body[4].value.keywords[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[3]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:158`; AST `a06c067ce3eac7a02b7b06b17620888e2dacc402639ea2c15ce9d0bad1b82655`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _save, directory, name, record, root. Outputs/bindings: (none).
Calls/effect boundaries: _save.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[3].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:158`; AST `fed29693b66e7b4b35a43aa4d72d7f20089997c05e1db5b052e07f5a1658e356`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _save, directory, name, record, root. Outputs/bindings: (none).
Calls/effect boundaries: _save.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[4]::Expr

Source: `infra/agentinfra/roadmap_mirrors.py:159`; AST `ef3fa73e8ee0737e3ef22e65bee786334d48158f36a8ada478545ee56ba040eb`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc, results, source, type. Outputs/bindings: (none).
Calls/effect boundaries: results.append, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[12].body[7].handlers[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[4].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:159`; AST `86e072d7b6c3968149882b434faa22d0558f8905a047899d00c4f1309d7593e4`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, results, source, type. Outputs/bindings: (none).
Calls/effect boundaries: results.append, type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[12].body[7].handlers[0].body[4].value.args[0].values[1].value::Call

Source: `infra/agentinfra/roadmap_mirrors.py:159`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[12].body[7].handlers[0].body[4].value.args[0].values[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[13]::Raise

Source: `infra/agentinfra/roadmap_mirrors.py:160`; AST `24e883ee0f23a9ae0630352835e682a8482914547097a8cb87f0169be6b26e17`.

Rust module: `infra::agentinfra::roadmap_mirrors`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ContractError, results, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Raise evaluation at root.body[19].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[13].exc::Call

Source: `infra/agentinfra/roadmap_mirrors.py:160`; AST `72b289d90b843c059bf7f8b6feda79139169c0cc0b28401fa9322e1f2c5a0a35`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, results, str. Outputs/bindings: (none).
Calls/effect boundaries: ContractError, str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].exc; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_mirrors.py::module::download_with_mirrors::root.body[19].body[13].exc.args[0].right::Call

Source: `infra/agentinfra/roadmap_mirrors.py:160`; AST `e2ef4e3295facda7605e6db852f395cc5b790449a961fdf0580a30db32d959ee`.

Rust module: `infra::agentinfra::roadmap_mirrors`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: results, str. Outputs/bindings: (none).
Calls/effect boundaries: str.
Dependencies: __future__, atomic, hashlib, pathlib, roadmap_download, roadmap_records, security, ssl, time, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[13].exc.args[0].right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; sha2; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
