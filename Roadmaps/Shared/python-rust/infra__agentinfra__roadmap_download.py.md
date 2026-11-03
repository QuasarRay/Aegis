# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 224. Inventory digest: `538f6d7d76f9cc5d179d4ddcf22e2ef18adf3cd0014ce7e951ee939cb51219d0`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/agentinfra/roadmap_download.py::module::root::Module

Source: `infra/agentinfra/roadmap_download.py:1`; AST `25e9b24ccf7f7da9a1bd0461c78448946b09f18eee561160f0a8540dfdbd2479`.

Rust module: `infra::agentinfra::roadmap_download`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: DNS_ENDPOINT, Exception, OSError, Path, TRANSPORT, _HTTPSHandler, _HTTPSRedirect, _ResolvedConnection, _addresses, _host, address, addresses, all, answer, atomic_write_json, chunk, code, confined_path, connection, count, created_partial, deadline, dict, digest, directory, entry, exc, file_binding, float, fp, headers, host, http, int, ipaddress, kwargs, last_error, len, list, loads, max_addresses, message, min, name, newurl, observation, observations, opener, output, parsed, partial, path, query, questions, raw, remaining, request, require, response, root, row, self, sock, socket, sorted, ssl, str, super, time, type, url, urllib. Outputs/bindings: DNS_ENDPOINT, INTERFACE_VERSION, TRANSPORT, address, addresses, answer, chunk, count, created_partial, directory, last_error, name, observation, observations, opener, output, parsed, partial, path, query, questions, raw, remaining, request, response, row, sock.
Calls/effect boundaries: Path, _HTTPSHandler, _HTTPSRedirect, _ResolvedConnection, _addresses, _host, all, answer.get, atomic_write_json, confined_path, digest, directory.mkdir, entry.get, file_binding, ipaddress.IPv4Address, len, loads, min, observations.append, opener.open, output.write, parsed.hostname.encode, parsed.hostname.encode('idna').decode, parsed.hostname.encode('idna').decode('ascii').lower, parsed.hostname.encode('idna').decode('ascii').lower().rstrip, partial.open, partial.read_bytes, partial.replace, partial.stat, partial.unlink, path.exists, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, path.stat, path.with_name, questions[0].get, questions[0].get('name', '').lower, questions[0].get('name', '').lower().rstrip, raw.decode, require, response.read, row.get, self._context.wrap_socket, self.do_open, self.observations.append, self.sock.getpeercert, self.sock.version, sock.close, socket.create_connection, sorted, ssl.create_default_context, str, super, super().__init__, super().redirect_request, time.monotonic, type, urllib.parse.urlencode, urllib.parse.urlsplit, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener, urllib.request.urlopen.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:1`; AST `82747f9c427c3911f9d0d33224823f4ff248c1ec5e258994ec363b1d9fea0e82`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[1]::ImportFrom

Source: `infra/agentinfra/roadmap_download.py:7`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[2]::Import

Source: `infra/agentinfra/roadmap_download.py:9`; AST `6c915fe19718932a78b9e90621db8b29ea426769d6c73fa5ccf59a1cafd68f05`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[3]::Import

Source: `infra/agentinfra/roadmap_download.py:10`; AST `5b5689182bafdc06d85d3690ad6cdbd72ce5c9f2cb0293261fa0a51748f52f99`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[4]::ImportFrom

Source: `infra/agentinfra/roadmap_download.py:11`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[5]::Import

Source: `infra/agentinfra/roadmap_download.py:12`; AST `9df267ed6eef4f61eaaffaebdf9ac9fe93bcf6d1aab9647b1fd045430624c91e`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[6]::Import

Source: `infra/agentinfra/roadmap_download.py:13`; AST `d58f4a781306aa988c2a48663bae1b9c9f8057e04c8f1f102adaea8473a930a5`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[7]::Import

Source: `infra/agentinfra/roadmap_download.py:14`; AST `ff05bad0fd9a7212d3cd85fd2726055168be21bc8f6e0d93b29965794b0675d4`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[8]::Import

Source: `infra/agentinfra/roadmap_download.py:15`; AST `40d1040049769bdc52defb6cc883a6ad22596d986f6c1641c6fb0029792b5ab1`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[9]::Import

Source: `infra/agentinfra/roadmap_download.py:16`; AST `6e0f76526c6d4c47fb54fd80b1a9075af18e040d8abcba786757ca55a9676c61`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Import evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[10]::ImportFrom

Source: `infra/agentinfra/roadmap_download.py:18`; AST `1b8b71be5203ae66cf696ad7ae023750f023f11fd20fe2501f8e1d56817881e3`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[11]::ImportFrom

Source: `infra/agentinfra/roadmap_download.py:19`; AST `588add542be37531cef9945b58a3e9e9a9abb027274199a99a3fccf951b20b03`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[12]::ImportFrom

Source: `infra/agentinfra/roadmap_download.py:20`; AST `c77b99ce1220eaeadd24d0d2eb90624f8e6b280576577774ee57598a0f5eef8f`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ImportFrom evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[13]::Assign

Source: `infra/agentinfra/roadmap_download.py:23`; AST `450386d2b05707b77cb785f3c9c72b49c8717abae76f79b264237aee79ca0820`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: INTERFACE_VERSION.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[14]::Assign

Source: `infra/agentinfra/roadmap_download.py:24`; AST `f1132f8f1b716c3796f944c332caca0a011863fa4b0072136cf127982eddb324`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: DNS_ENDPOINT.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[14]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::root.body[15]::Assign

Source: `infra/agentinfra/roadmap_download.py:25`; AST `61ffaaf0e6d93b8ab56020382db9bf0c662ae216278bb5b9c32f04a942c0f778`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: TRANSPORT.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[15]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:28`; AST `5112592b809e9524271f0bca062ec194257e1edb3ca52953456f213cb2b040b0`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: parsed, require, str, url, urllib. Outputs/bindings: parsed.
Calls/effect boundaries: parsed.hostname.encode, parsed.hostname.encode('idna').decode, parsed.hostname.encode('idna').decode('ascii').lower, parsed.hostname.encode('idna').decode('ascii').lower().rstrip, require, urllib.parse.urlsplit.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[16]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:29`; AST `8d599cf5a075175bfb1ff48fb0172814da2f7dc118102fbfc43d0036046b15a6`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: url, urllib. Outputs/bindings: parsed.
Calls/effect boundaries: urllib.parse.urlsplit.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[16].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:29`; AST `b6a2bdd5504eb171554e6da24ea3cd5d18aaf93de2ff2f60a3ba08638c9cd64c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: url, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.parse.urlsplit.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:30`; AST `ea53f6057a6c691ac67a839c410d846f40e44a37aad0a24a53b30ab09d25aa41`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parsed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[16].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:30`; AST `29fc3c2a0b0bf9c37f6e571709c78edc95e975f90414bb9d9ecf1474270b78dd`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parsed, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[2]::Return

Source: `infra/agentinfra/roadmap_download.py:32`; AST `d55f105d58df408f30dd3dbc1863c71850ccbaa074e463b739f78c84afed6eec`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: parsed. Outputs/bindings: (none).
Calls/effect boundaries: parsed.hostname.encode, parsed.hostname.encode('idna').decode, parsed.hostname.encode('idna').decode('ascii').lower, parsed.hostname.encode('idna').decode('ascii').lower().rstrip.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[16].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:32`; AST `812d01970c186e4bbd82521cdb63fea2df8bced375eddf090ed81c6e2ca74e9d`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parsed. Outputs/bindings: (none).
Calls/effect boundaries: parsed.hostname.encode, parsed.hostname.encode('idna').decode, parsed.hostname.encode('idna').decode('ascii').lower, parsed.hostname.encode('idna').decode('ascii').lower().rstrip.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[2].value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:32`; AST `8d38c34a033314f8d5e1587af5155059b1556191b9452e06a961e46579a4bf58`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parsed. Outputs/bindings: (none).
Calls/effect boundaries: parsed.hostname.encode, parsed.hostname.encode('idna').decode, parsed.hostname.encode('idna').decode('ascii').lower.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[2].value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:32`; AST `36c9264c604a72e24813300a1df7c0608f8d5a683aa40f246ee2127d1bdd693e`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parsed. Outputs/bindings: (none).
Calls/effect boundaries: parsed.hostname.encode, parsed.hostname.encode('idna').decode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_host::root.body[16].body[2].value.func.value.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:32`; AST `7fb875a7a4d4bda3359f4dce0fd6b08a035b14f1a378a794e046d5a26c2e8197`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: parsed. Outputs/bindings: (none).
Calls/effect boundaries: parsed.hostname.encode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[16].body[2].value.func.value.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:35`; AST `3a20fb47dff4f5261007c6e2396368b7ba1c67e530b54564d43459bc445e1de5`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: DNS_ENDPOINT, address, addresses, all, answer, dict, digest, host, int, ipaddress, len, list, loads, observations, query, questions, raw, request, require, response, row, sorted, str, type, urllib. Outputs/bindings: address, addresses, answer, query, questions, raw, request, response, row.
Calls/effect boundaries: all, answer.get, digest, ipaddress.IPv4Address, len, loads, observations.append, questions[0].get, questions[0].get('name', '').lower, questions[0].get('name', '').lower().rstrip, raw.decode, require, response.read, row.get, sorted, str, type, urllib.parse.urlencode, urllib.request.Request, urllib.request.urlopen.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[17]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:36`; AST `41b7b7282cd03e218f473023792f506cbcce7293a8db6bac052bf01bf8b67509`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: DNS_ENDPOINT, host, urllib. Outputs/bindings: query.
Calls/effect boundaries: urllib.parse.urlencode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_download.py:36`; AST `ab1502bc5063a25f821ce2ca5239b8cfc2a503c58f1fe1bbd2fdab1fc378116c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: host, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.parse.urlencode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:37`; AST `8a1e77db694b0cf55b2179140a910d2001b348c351d6b482bb1b8344ac77c742`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: query, urllib. Outputs/bindings: request.
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:37`; AST `8bda3b98ad8b26cae8795caf7f32f1b83c92135683f70026c2603da36ab50b56`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: query, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[2]::With

Source: `infra/agentinfra/roadmap_download.py:40`; AST `6b0d8cb2bd49aac41aab2a8b3130b853343785da54a93cf0e6bc920c2a7aceba`.

Rust module: `infra::agentinfra::roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: request, response, urllib. Outputs/bindings: raw, response.
Calls/effect boundaries: response.read, urllib.request.urlopen.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[17].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[2].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_download.py:40`; AST `8ac2276f9ac125ee1b5b2f0d9d40dde77e0badde602c41b748d3dfc3e7234eda`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: request, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.urlopen.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:41`; AST `76d54ac191b494519fada4de5e1d2e95cb90ba6bb575e6bc47c4db84d9dc816b`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: response. Outputs/bindings: raw.
Calls/effect boundaries: response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:41`; AST `d984f25d1e96cb7df476c97a39327e6ad9e272043370facc2cbca8d9a6009e09`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[3]::Expr

Source: `infra/agentinfra/roadmap_download.py:42`; AST `c5f81608ba5871b3b525da74567881b077117a3c15fbc0aaaba8dec156918eec`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:42`; AST `8a46194b27d938662b032109776bdacbb87657b424fe0d49b25fd12fb17b08a5`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw, require. Outputs/bindings: (none).
Calls/effect boundaries: len, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[3].value.args[0].left::Call

Source: `infra/agentinfra/roadmap_download.py:42`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[3].value.args[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[4]::Assign

Source: `infra/agentinfra/roadmap_download.py:43`; AST `172a42c00daec7a47a6194a2a75f46239d56c1f0cc12049f3fe62319f463ed05`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: loads, raw. Outputs/bindings: answer.
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[4].value::Call

Source: `infra/agentinfra/roadmap_download.py:43`; AST `b0243dd0cab49c75a82285e7c5c4ed5b2a83240ca34a191103b1d12859a47166`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: loads, raw. Outputs/bindings: (none).
Calls/effect boundaries: loads, raw.decode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[4].value.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:43`; AST `245aa6e406d6efc480215a639e092703d5658ef44570968198988a49d0620cdd`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw. Outputs/bindings: (none).
Calls/effect boundaries: raw.decode.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[5]::Assign

Source: `infra/agentinfra/roadmap_download.py:44`; AST `aa14dfe2bbea782f4a5d3bdc2f3765f09302eb682822415fc44508acdacd63bb`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: answer. Outputs/bindings: questions.
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[5].value::Call

Source: `infra/agentinfra/roadmap_download.py:44`; AST `b0baca40242f4688e56224659455e46a7ae81a7c7d3ef383a76dc7a0779e88a9`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer. Outputs/bindings: (none).
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6]::Expr

Source: `infra/agentinfra/roadmap_download.py:45`; AST `4ab59553cde92ae1cba07d11299d7a112361f6a7fef8ae35448d29103f7f603d`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: answer, host, int, len, questions, require, type. Outputs/bindings: (none).
Calls/effect boundaries: answer.get, len, questions[0].get, questions[0].get('name', '').lower, questions[0].get('name', '').lower().rstrip, require, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value::Call

Source: `infra/agentinfra/roadmap_download.py:45`; AST `75e9afd3cc191323b4abab4223cd7c15a21079cb0cccc8d9819396ed4aa754c5`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer, host, int, len, questions, require, type. Outputs/bindings: (none).
Calls/effect boundaries: answer.get, len, questions[0].get, questions[0].get('name', '').lower, questions[0].get('name', '').lower().rstrip, require, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_download.py:45`; AST `5f6187c0617c8bd33972ea89ccbc8e8af3ad19f9b8e19abe3e1dc7f75aa69567`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer, type. Outputs/bindings: (none).
Calls/effect boundaries: answer.get, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:45`; AST `ace8583069d7b86756d6b4bafff5ea0d890f5ea366a87e5bf1269ee7be8a4205`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer. Outputs/bindings: (none).
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_download.py:45`; AST `bfe3ecd31f686d038f8031d736fcbee5c9f1324fe354c689e95f9a9125fbb0df`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer. Outputs/bindings: (none).
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[3].left::Call

Source: `infra/agentinfra/roadmap_download.py:46`; AST `8a361e5bfc95d7cb1619ca358fed0afe8e36425aa2a53433e69e8ef88c23bf08`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer. Outputs/bindings: (none).
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[3].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[4].left::Call

Source: `infra/agentinfra/roadmap_download.py:46`; AST `6ebb14d96451a1996088fabd58d658289ead087e73f0ed5881baf0600168159b`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, questions. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[4].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[5].left::Call

Source: `infra/agentinfra/roadmap_download.py:46`; AST `ea27c78db05790063db88a7dd3d4a4b797c92cc09112c1e70b04fbb9866d618d`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: questions. Outputs/bindings: (none).
Calls/effect boundaries: questions[0].get, questions[0].get('name', '').lower, questions[0].get('name', '').lower().rstrip.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[5].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[5].left.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:46`; AST `8782a5e0dad555a3cb2283d178e95f89151bb43f840131665d84cb21fee99e50`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: questions. Outputs/bindings: (none).
Calls/effect boundaries: questions[0].get, questions[0].get('name', '').lower.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[5].left.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[5].left.func.value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:46`; AST `359da1bae339b5d5ebfa0723f0be38eebea3be5958d137573f601f2ffdbc2cdf`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: questions. Outputs/bindings: (none).
Calls/effect boundaries: questions[0].get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[5].left.func.value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[6].left::Call

Source: `infra/agentinfra/roadmap_download.py:47`; AST `e4c7495db1eba074cb63bea630b2a63446546cba63115a7f2f9befaae333cc31`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: questions, type. Outputs/bindings: (none).
Calls/effect boundaries: questions[0].get, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[6].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[6].value.args[0].values[6].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:47`; AST `2b8fd4d9ec7d7e311391ceb1fcb13b3b4544aa22dbbdbffb4e0aeeb1b4443646`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: questions. Outputs/bindings: (none).
Calls/effect boundaries: questions[0].get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[6].value.args[0].values[6].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7]::Assign

Source: `infra/agentinfra/roadmap_download.py:49`; AST `3462fca6e8176e07dc72615c480fe5a234fe619132bf9aeebd1d2b8ced5dbb2f`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: answer, ipaddress, row, sorted, str. Outputs/bindings: addresses, row.
Calls/effect boundaries: answer.get, ipaddress.IPv4Address, row.get, sorted, str.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[17].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value::Call

Source: `infra/agentinfra/roadmap_download.py:49`; AST `4e01bf22b3bcf51120eab1b133564d42b5d410e7e25cd21439775f0b6f29d6ce`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer, ipaddress, row, sorted, str. Outputs/bindings: row.
Calls/effect boundaries: answer.get, ipaddress.IPv4Address, row.get, sorted, str.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value.args[0]::SetComp

Source: `infra/agentinfra/roadmap_download.py:49`; AST `00d269789058ecdf7a78f8556d7374acd4fbde5881c9b4d366c42f18a8407bed`.

Rust module: `infra::agentinfra::roadmap_download`. source-compatible ordered evaluation into a set; preserve equality/hash behavior

Inputs: answer, ipaddress, row, str. Outputs/bindings: row.
Calls/effect boundaries: answer.get, ipaddress.IPv4Address, row.get, str.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered SetComp evaluation at root.body[17].body[7].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value.args[0].elt::Call

Source: `infra/agentinfra/roadmap_download.py:49`; AST `f00a1a8dcfc5f0464abb5261d3b5513538d9031e87258227e9b3e05bb4ac8acc`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ipaddress, row, str. Outputs/bindings: (none).
Calls/effect boundaries: ipaddress.IPv4Address, str.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value.args[0].elt; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value.args[0].elt.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:49`; AST `2a707823ef2a91604aabab56fcef0c29fcda741c59c43b4c369eb7a2e10b7d58`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ipaddress, row. Outputs/bindings: (none).
Calls/effect boundaries: ipaddress.IPv4Address.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value.args[0].elt.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value.args[0].generators[0].iter::Call

Source: `infra/agentinfra/roadmap_download.py:49`; AST `1543b2697ecedd41e4963e6221b4f2b607a2778c4348aed1b270ea34876c1fa4`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: answer. Outputs/bindings: (none).
Calls/effect boundaries: answer.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value.args[0].generators[0].iter; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[7].value.args[0].generators[0].ifs[0].left::Call

Source: `infra/agentinfra/roadmap_download.py:49`; AST `19b7b5a576a4de3935d806d7bc76a957896c75e21ce7fe5c363f8b7acfa93b92`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: row. Outputs/bindings: (none).
Calls/effect boundaries: row.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[7].value.args[0].generators[0].ifs[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8]::Expr

Source: `infra/agentinfra/roadmap_download.py:50`; AST `9e0780b9a0df42b56d8588883990738fb002e14848fd2c708935e2471508e6b6`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: address, addresses, all, ipaddress, len, require. Outputs/bindings: address.
Calls/effect boundaries: all, ipaddress.IPv4Address, len, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[8]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8].value::Call

Source: `infra/agentinfra/roadmap_download.py:50`; AST `91240ff15cbc442193665521efdd4b0854cd71de1df774105fa7ff96cfdcb2d1`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, addresses, all, ipaddress, len, require. Outputs/bindings: address.
Calls/effect boundaries: all, ipaddress.IPv4Address, len, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8].value.args[0].values[0].comparators[0]::Call

Source: `infra/agentinfra/roadmap_download.py:50`; AST `4fa3e4ef1e9b727c555e271573b12409fc93b4130ee46da03e4eae031894e959`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: addresses, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value.args[0].values[0].comparators[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8].value.args[0].values[1]::Call

Source: `infra/agentinfra/roadmap_download.py:50`; AST `e425d0edfabf4072dc4bd5407d4141492c2f18872e3dfcdd74ab3fc9f219bcf0`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, addresses, all, ipaddress. Outputs/bindings: address.
Calls/effect boundaries: all, ipaddress.IPv4Address.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value.args[0].values[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8].value.args[0].values[1].args[0]::GeneratorExp

Source: `infra/agentinfra/roadmap_download.py:50`; AST `9f13269d3da28336ba6297a97d88a12834b79ca3438720dfb23ba35e96cec019`.

Rust module: `infra::agentinfra::roadmap_download`. lazy iterator with captured environment and explicit exhaustion/error lifetime

Inputs: address, addresses, ipaddress. Outputs/bindings: address.
Calls/effect boundaries: ipaddress.IPv4Address.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered GeneratorExp evaluation at root.body[17].body[8].value.args[0].values[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[8].value.args[0].values[1].args[0].elt.value::Call

Source: `infra/agentinfra/roadmap_download.py:50`; AST `310f713ec4f77ac065b4c77af6c9a07250d67247003970f9bb4c7f5372cf2467`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, ipaddress. Outputs/bindings: (none).
Calls/effect boundaries: ipaddress.IPv4Address.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[8].value.args[0].values[1].args[0].elt.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[9]::Expr

Source: `infra/agentinfra/roadmap_download.py:52`; AST `fbd157fefb31da325f89c8335924cf11c478f08cbd749df098726d6bc0412cd1`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: DNS_ENDPOINT, addresses, digest, host, observations, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest, observations.append.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[17].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[9].value::Call

Source: `infra/agentinfra/roadmap_download.py:52`; AST `afc9edbc3aa801167694b33971258e6292e8bf7ac553dd2795dc567239dab423`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: DNS_ENDPOINT, addresses, digest, host, observations, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest, observations.append.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[9].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_download.py:53`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[17].body[9].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_addresses::root.body[17].body[10]::Return

Source: `infra/agentinfra/roadmap_download.py:54`; AST `fa8cf5fddc0a92a239b60af7bb441cc461782ecf7f56c18267b343ffa9e7d5ec`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: addresses. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[17].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::root.body[18]::ClassDef

Source: `infra/agentinfra/roadmap_download.py:57`; AST `23fa62aaf0a56bc40288cc367c2c703ab57023cea6626fe584f41b04dca82ac1`.

Rust module: `infra::agentinfra::roadmap_download`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: OSError, _addresses, address, deadline, dict, digest, exc, float, host, http, int, kwargs, last_error, list, max_addresses, min, observations, remaining, require, self, sock, socket, str, super, time, type. Outputs/bindings: address, last_error, remaining, sock.
Calls/effect boundaries: _addresses, digest, min, require, self._context.wrap_socket, self.observations.append, self.sock.getpeercert, self.sock.version, sock.close, socket.create_connection, super, super().__init__, time.monotonic, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[18]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:58`; AST `07defa57232b387efb3bb5d86c50f21a793a02eae8cd0b4dc3cb13d6da4b129a`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: deadline, dict, float, host, int, kwargs, list, max_addresses, observations, self, str, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:60`; AST `b949e53dad45c17bfd822b9303fa3df29e7d2f6613b83061f83c9ee26c526dd4`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: host, kwargs, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:60`; AST `b59e80b60ccd64eae93b080d2e84607d1175c18af00229c08468837ef974e0e5`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: host, kwargs, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:60`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:61`; AST `f8f8bb76fc15de30e192edd88250ccad9bcd2c166b3f187d7f0d48dde5ad42f9`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observations, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_download.py:62`; AST `1df9d83f0be09b8d1144a6d40a828f54c7a85a8cda8706bede0eaab5cab8d7f4`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: deadline, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::__init__::root.body[18].body[0].body[3]::Assign

Source: `infra/agentinfra/roadmap_download.py:63`; AST `6b5e2718c524f277b363f7a1d24f46eb2c5ee2bc059fbf5b509119e965b74476`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: max_addresses, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:65`; AST `df6c3f17fd263cc05acccf5ea66f94950350a7e445cfa45d107e4fb319ac9c14`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: OSError, _addresses, address, digest, exc, last_error, min, remaining, require, self, sock, socket, time, type. Outputs/bindings: address, last_error, remaining, sock.
Calls/effect boundaries: _addresses, digest, min, require, self._context.wrap_socket, self.observations.append, self.sock.getpeercert, self.sock.version, sock.close, socket.create_connection, time.monotonic, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[18].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:66`; AST `7ea9b719d1a2dcc7a920056571b6763ff75c2a4dd7e960ee40cc02ae9dae39fc`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:66`; AST `27400dd66fa42a3720aa45ad7c4a8316b159c8ecbed16d534231aa2cd40b418f`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:67`; AST `c5039daca53505ecea0eef9b371a19d7f47f71bcc5eafecb2c3e23902b54eb4f`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2]::For

Source: `infra/agentinfra/roadmap_download.py:68`; AST `14dc4c4914f83e30a7eded606518285aa38f0071f09a7dbc20b48230aeccb960`.

Rust module: `infra::agentinfra::roadmap_download`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: OSError, _addresses, address, digest, exc, min, remaining, require, self, sock, socket, time, type. Outputs/bindings: address, last_error, remaining, sock.
Calls/effect boundaries: _addresses, digest, min, require, self._context.wrap_socket, self.observations.append, self.sock.getpeercert, self.sock.version, sock.close, socket.create_connection, time.monotonic, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered For evaluation at root.body[18].body[1].body[2]; no call, error or mutation may be omitted. Iteration: address in _addresses(self.host, self.observations)[:self.max_addresses]
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].iter.value::Call

Source: `infra/agentinfra/roadmap_download.py:68`; AST `f5a342e654900a555a7f3e1b8ad0c36dd97e3a4fcf23a25e8b7f6f3b523aab6e`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _addresses, self. Outputs/bindings: (none).
Calls/effect boundaries: _addresses.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].iter.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:69`; AST `eb919213cfc2921adc2d3382784f31a5593dccdcd501a10ad561a12ce24e3b6e`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: sock.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1]::Try

Source: `infra/agentinfra/roadmap_download.py:70`; AST `d89015523c1522018c850a06571211817fc2ca106f8eb4e9c23bbe057b977029`.

Rust module: `infra::agentinfra::roadmap_download`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: OSError, address, digest, exc, min, remaining, require, self, sock, socket, time, type. Outputs/bindings: last_error, remaining, sock.
Calls/effect boundaries: digest, min, require, self._context.wrap_socket, self.observations.append, self.sock.getpeercert, self.sock.version, sock.close, socket.create_connection, time.monotonic, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Try evaluation at root.body[18].body[1].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0]::If

Source: `infra/agentinfra/roadmap_download.py:71`; AST `bdd22a02d6aea9aba378c8fd80fc842816782e96885e7b2aa0bf027a5f9e9be0`.

Rust module: `infra::agentinfra::roadmap_download`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: min, remaining, require, self, time. Outputs/bindings: remaining.
Calls/effect boundaries: min, require, time.monotonic.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2].body[1].body[0]; no call, error or mutation may be omitted. Condition: self.deadline is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:72`; AST `1c6c3d9c41f79ddd67b7e18f233ea9b3b8966cd47080721568299b430d683ae8`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, time. Outputs/bindings: remaining.
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[0].value.right::Call

Source: `infra/agentinfra/roadmap_download.py:72`; AST `1518ec519851d0a5084168b533bc641ad5d2ce5a406bada9f9d7d919d82e5b92`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: time. Outputs/bindings: (none).
Calls/effect boundaries: time.monotonic.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[0].body[0].value.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:73`; AST `16fa5e5686c89325e2899cd443dc1e95ac48e71340cdd9ae995316e55b717ef3`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[2].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:73`; AST `f73987b393b548555772f09dcd857b82b0da6774bf7135e13f7cbb44a7ddc5d2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: remaining, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_download.py:74`; AST `da9a1924ab7cd930b5f4d8cb076499a6757f43a299f305f01425d43ee279f1ea`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: min, remaining, self. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[1].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[0].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:74`; AST `07d90ea4f67f6e9cd26909a1a6c55659c58ce7372f4bd2fbad3162105b19a68b`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: min, remaining, self. Outputs/bindings: (none).
Calls/effect boundaries: min.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:75`; AST `2e99d03629e83d624c43a3090bd4866be4f69e37cd3304082fc25343a4a6a116`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: address, self, socket. Outputs/bindings: sock.
Calls/effect boundaries: socket.create_connection.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:75`; AST `ba146571de2b502e8e11d5a0a98ffd6ca90fd7a6a1e1482b70dc2e162397e5d5`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, self, socket. Outputs/bindings: (none).
Calls/effect boundaries: socket.create_connection.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[2]::Assign

Source: `infra/agentinfra/roadmap_download.py:76`; AST `57ff752469710a1475ffabd523f4d72f796e5b141a28c7708c1a8fd3f37b9517`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, sock. Outputs/bindings: (none).
Calls/effect boundaries: self._context.wrap_socket.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:76`; AST `47482dd7407bd48d4d9ec990268b555e6c088bf466d71ac83679c0756cafa4f4`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, sock. Outputs/bindings: (none).
Calls/effect boundaries: self._context.wrap_socket.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_download.py:77`; AST `edcdb723e026a04c08cf8601a05146c0d05a9321ccccb78c0c91dc699a463d05`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: address, digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.observations.append, self.sock.getpeercert, self.sock.version.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[2].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:77`; AST `44a0165e286bed32c0ed8615020215261d741bc2fc64ed87ffa0f40b398a7255`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.observations.append, self.sock.getpeercert, self.sock.version.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[3]::Call

Source: `infra/agentinfra/roadmap_download.py:78`; AST `a12dae16b9b056c72e1d40258b243b9630da73b8f03f626e60acff786f40fc00`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.sock.version.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[4]::Call

Source: `infra/agentinfra/roadmap_download.py:79`; AST `2c5c055345fee425c16dfeddf5fc30cf269c5edc2aa9e6c3e234c194807430a2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.sock.getpeercert.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[4].args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:79`; AST `a9e62f64ef9ccfb98c113ebb4bab671843960150d54ea57108494a420e606929`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.sock.getpeercert.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].body[3].value.args[0].values[4].args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].body[4]::Return

Source: `infra/agentinfra/roadmap_download.py:80`; AST `d3ec646650be52e3f5b5700447f19313b1bab9ed1bd27c2483960d5d0bcaf584`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[18].body[1].body[2].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_download.py:81`; AST `fe78cb3dad050e3aa42709104e1f09e1f66617a2fc90a962967081ca7fc8717b`.

Rust module: `infra::agentinfra::roadmap_download`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: OSError, address, exc, self, sock, type. Outputs/bindings: last_error.
Calls/effect boundaries: self.observations.append, sock.close, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[18].body[1].body[2].body[1].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[0]::If

Source: `infra/agentinfra/roadmap_download.py:82`; AST `00c56776c97d60eb6ceb0c4bfba5fd238a6117dbd9dce4352903ff4bcdaded74`.

Rust module: `infra::agentinfra::roadmap_download`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: sock. Outputs/bindings: (none).
Calls/effect boundaries: sock.close.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[0]; no call, error or mutation may be omitted. Condition: sock is not None
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:83`; AST `b7d533035a32746851284d108aca0290d678a2554844fcc604ff972215db1c29`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: sock. Outputs/bindings: (none).
Calls/effect boundaries: sock.close.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:83`; AST `dab830a542f0df5a85965434f009b0b36896495c0d4d525a244fe75145775b3e`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: sock. Outputs/bindings: (none).
Calls/effect boundaries: sock.close.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:84`; AST `67bcfd698d651620913500fc7e3e691e10f484d1de9e544983049c6051cb04ac`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: address, exc, self, type. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.append, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:84`; AST `bb5346ca1015d0a132f7c83c60ee4909420512ecaa118d89e7c36dc44430b2f2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: address, exc, self, type. Outputs/bindings: (none).
Calls/effect boundaries: self.observations.append, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[1].value.args[0].values[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:85`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[1].value.args[0].values[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[2].body[1].handlers[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_download.py:86`; AST `30f88c0a10ae6e7341ebad4d2c46ef4986c5e3ad095562ee388e9d491eeaf1f2`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: exc. Outputs/bindings: last_error.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[18].body[1].body[2].body[1].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[3]::Expr

Source: `infra/agentinfra/roadmap_download.py:87`; AST `484a2e644f7913309c97993f676ad83f99126e7b5874b3dabf9f945ac467ef19`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: last_error, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[18].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:87`; AST `bc5c829ac5d5c941b6cc813983fe777b13dd3cd308ddf301ec0b703b2bcc88bd`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: last_error, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[18].body[1].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_ResolvedConnection::connect::root.body[18].body[1].body[4]::Raise

Source: `infra/agentinfra/roadmap_download.py:88`; AST `80e99c0ea436dc3a4414f314b923c9e1f33b00695801feba40a503647dbda6f3`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: last_error. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Raise evaluation at root.body[18].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::root.body[19]::ClassDef

Source: `infra/agentinfra/roadmap_download.py:91`; AST `5529eed6c5767da2f40c80804d5ce9a79e1779241328b83e2e78c55fdc1bb78e`.

Rust module: `infra::agentinfra::roadmap_download`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: _ResolvedConnection, _host, connection, dict, host, kwargs, list, observations, request, require, self, ssl, super, urllib. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection, _host, require, self.do_open, ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[19]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:92`; AST `69ec923dfbfb21b5fff8dd23e3bb3e0e22474f84dcb8d384d97e3614ea8dea58`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: dict, list, observations, require, self, ssl, super. Outputs/bindings: (none).
Calls/effect boundaries: require, ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:93`; AST `28c59d6d549686f850af338c1c0df4aba17498a1ecd2b3696494e658ba97d588`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: ssl, super. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:93`; AST `673721f26c0c1041a7656b3d0c36005c08a29b723ccf5c1e32bc78c0cba53745`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ssl, super. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context, super, super().__init__.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[0].value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:93`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[0].value.keywords[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:93`; AST `f328760be460c9f8eeedf6a290722b001ee67018c6508a414b3e66a1412ca187`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ssl. Outputs/bindings: (none).
Calls/effect boundaries: ssl.create_default_context.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[0].value.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:94`; AST `87b47f031729cf56916f31c3b2a90fba8d4d9832ffde0001a50842191861862f`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: require, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:94`; AST `6266a340fe911ae55a22e6ae0db60b806b677474d984d7366be11239a7bd7502`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: require, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::__init__::root.body[19].body[0].body[2]::Assign

Source: `infra/agentinfra/roadmap_download.py:96`; AST `f8f8bb76fc15de30e192edd88250ccad9bcd2c166b3f187d7f0d48dde5ad42f9`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observations, self. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[19].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::root.body[19].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:98`; AST `2d440f4e2abe949a4291d398756da17152d80b4b4bba7208ecdea1ba13a3c15c`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _ResolvedConnection, _host, connection, host, kwargs, request, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection, _host, self.do_open.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::root.body[19].body[1].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:99`; AST `42faae0fa2501c6c064166cd97e0bf705e0d11f7dac8ea4e7adb7fae60dbf099`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, request. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[19].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::root.body[19].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:99`; AST `4f2b36bff326252dbbc41b539966a912a26de3ae6b34533f2bcb7f1066827fc1`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, request. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::connection::root.body[19].body[1].body[1]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:100`; AST `c5f537b8c82c9b0d82efe923830bd314353a82a6745b699bceda7738b6a2e1a1`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[19].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::connection::root.body[19].body[1].body[1].body[0]::Return

Source: `infra/agentinfra/roadmap_download.py:101`; AST `198eaaa9cabc2a0d146c6cadcae72d4942f15eed484f5e391677852428f44001`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::connection::root.body[19].body[1].body[1].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:101`; AST `73600a7883a2ae5a179b2fbc961ab6d5112cbc82c486195a7451ada3b97f2d2a`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _ResolvedConnection, host, kwargs, self. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[1].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::root.body[19].body[1].body[2]::Return

Source: `infra/agentinfra/roadmap_download.py:102`; AST `3ef4c47c9cea2ba4aaf94dda7110b4dde6a142684c023074d74e2226875ec67d`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: connection, request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.do_open.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[19].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSHandler::https_open::root.body[19].body[1].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:102`; AST `b6311b473e46ef3561a3cab09bc5196bc479194b3cd7167a7858b0680418d8e8`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: connection, request, self. Outputs/bindings: (none).
Calls/effect boundaries: self.do_open.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[19].body[1].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::root.body[20]::ClassDef

Source: `infra/agentinfra/roadmap_download.py:105`; AST `ce2af355f6039c54e60006ff0d6d915d86115f7c016082597d0932b1499d69bf`.

Rust module: `infra::agentinfra::roadmap_download`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: _host, code, fp, headers, message, newurl, request, super, urllib. Outputs/bindings: (none).
Calls/effect boundaries: _host, super, super().redirect_request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ClassDef evaluation at root.body[20]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:106`; AST `984a29bc98c4fcda307c83199bb0cd4b8ed41ec776c2695fb84858516c1f1b95`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _host, code, fp, headers, message, newurl, request, super. Outputs/bindings: (none).
Calls/effect boundaries: _host, super, super().redirect_request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[20].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:107`; AST `35a61b5d0e88feaffed63d57a40950bda8172a3b2e7a005bd1ea6ad699759acf`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, newurl. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[20].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:107`; AST `c8e611368eb9aee1230e4b78187dd40046ca5ff160393305780a35669b70aec0`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, newurl. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0].body[1]::Return

Source: `infra/agentinfra/roadmap_download.py:108`; AST `43bd2254bdb12b9f9cbe47010447f1731b8f8f5645827f632d68f89f99875d12`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: code, fp, headers, message, newurl, request, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().redirect_request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[20].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:108`; AST `c30f6cefe80f9727a8be9a2591b2b9122764859f6cdb8fc8b0965138e8ba0498`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: code, fp, headers, message, newurl, request, super. Outputs/bindings: (none).
Calls/effect boundaries: super, super().redirect_request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::_HTTPSRedirect::redirect_request::root.body[20].body[0].body[1].value.func.value::Call

Source: `infra/agentinfra/roadmap_download.py:108`; AST `29352a716af572cde18824794ed45cef0d41381b7241b8175f75da4aa39943e3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: super. Outputs/bindings: (none).
Calls/effect boundaries: super.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[20].body[0].body[1].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21]::FunctionDef

Source: `infra/agentinfra/roadmap_download.py:111`; AST `26d48b7e80e9ca2188416243f017863ae701668d32fff3ad7235ed0dca37667d`.

Rust module: `infra::agentinfra::roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: Exception, Path, TRANSPORT, _HTTPSHandler, _HTTPSRedirect, _host, atomic_write_json, chunk, confined_path, count, created_partial, dict, digest, directory, entry, exc, file_binding, int, len, name, observation, observations, opener, output, partial, path, request, require, response, root, type, urllib. Outputs/bindings: chunk, count, created_partial, directory, name, observation, observations, opener, output, partial, path, request, response.
Calls/effect boundaries: Path, _HTTPSHandler, _HTTPSRedirect, _host, atomic_write_json, confined_path, digest, directory.mkdir, entry.get, file_binding, len, opener.open, output.write, partial.open, partial.read_bytes, partial.replace, partial.stat, partial.unlink, path.exists, path.read_bytes, path.relative_to, path.relative_to(root).as_posix, path.stat, path.with_name, require, response.read, type, urllib.request.ProxyHandler, urllib.request.Request, urllib.request.build_opener.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered FunctionDef evaluation at root.body[21]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:112`; AST `b5341536ae42c6757aa53ef42e2450095d339c2a3d6a9574544eb4676f209d4b`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:113`; AST `d3e0463539b1ef9cfac4bec9f6bd6273d9fad504f4c0bdee22a51160debc0ba2`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, root. Outputs/bindings: directory.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:113`; AST `aa776f971c22a60f51c5526e73c57c433bbdbc33b0e1922a81a6fc02b06515c9`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[2]::Expr

Source: `infra/agentinfra/roadmap_download.py:114`; AST `3a400253aadde423a42d9e21da0e9ba55a3fe64614ae692874cebc9a5aa91183`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:114`; AST `7f8492ad27b11def9f8bffa8aea0180c657a9152ccc4f6a4269a7601584575c2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: directory. Outputs/bindings: (none).
Calls/effect boundaries: directory.mkdir.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[3]::Assign

Source: `infra/agentinfra/roadmap_download.py:115`; AST `19e0a0458a4fd373331a20d625c9a051a8d23cb65505a804f560158f0eebddbe`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry. Outputs/bindings: name.
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:115`; AST `17d52058ee440ee1c93717819decf0a775a22713e205dba2d545e8f7ea0a9a6f`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[3].value.args[1]::Call

Source: `infra/agentinfra/roadmap_download.py:115`; AST `c8cf4beccb27bd62561b11a710c92c61ca7031556f3dfb4230194d3f554a1e74`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[3].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[4]::Expr

Source: `infra/agentinfra/roadmap_download.py:116`; AST `f4e49dc0fb602cc8c7836e781f0f1977281482cba50f483bfb5e5f9222688481`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, name, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[4].value::Call

Source: `infra/agentinfra/roadmap_download.py:116`; AST `7fe2ff1d1225e8aa147331d0b4b3e7c60f239ea7a4da8406bbaaa48c4b9779c1`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, name, require. Outputs/bindings: (none).
Calls/effect boundaries: Path, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[4].value.args[0].values[1].left.value::Call

Source: `infra/agentinfra/roadmap_download.py:116`; AST `e0661b96e847fdc1e815fc151ea8a6312b949d1130816c8cc00ae7f50185573c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, name. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[4].value.args[0].values[1].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[5]::Assign

Source: `infra/agentinfra/roadmap_download.py:117`; AST `46f0c10cac17799892849d9a424ce31beb6e076a761d21e482f0468eec04b700`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, name, root. Outputs/bindings: path.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[5].value::Call

Source: `infra/agentinfra/roadmap_download.py:117`; AST `cc071144396d66b7522cae0f953c524619cf3ab5e197a9630a22c22dff28195c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6]::Expr

Source: `infra/agentinfra/roadmap_download.py:118`; AST `dcf34bd811024b5ffc2e530ebadec7e794be477128c6e1e9165d9114e56b5b34`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, int, len, require, type. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, len, require, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6].value::Call

Source: `infra/agentinfra/roadmap_download.py:118`; AST `f1b2e8201682338db17099970da4bbc119d528b24b3e3cea8f15f07028d8c756`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, int, len, require, type. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, len, require, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6].value.args[0].values[0].left::Call

Source: `infra/agentinfra/roadmap_download.py:118`; AST `bedaf1a36d8d484f9c90d3866c47785b4b6d9aa4ca234478b88a1c8e8040e69d`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, type. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value.args[0].values[0].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6].value.args[0].values[0].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:118`; AST `7d57584f29ddf6571676cbc58a8cd5e3f1b1b2209f643e126c57285ebf1b63d4`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value.args[0].values[0].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6].value.args[0].values[2].left::Call

Source: `infra/agentinfra/roadmap_download.py:118`; AST `c3b87fba03a280865b38ce381eeb4aa4f9789270e0bc38562d9cd1b9440f1f79`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, len. Outputs/bindings: (none).
Calls/effect boundaries: entry.get, len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value.args[0].values[2].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[6].value.args[0].values[2].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:118`; AST `cb40855f69a0668cd11f1f0837c9eaad256acf5cb05da79bc2282323392e24d3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry. Outputs/bindings: (none).
Calls/effect boundaries: entry.get.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[6].value.args[0].values[2].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[7]::Expr

Source: `infra/agentinfra/roadmap_download.py:120`; AST `23a950bc0c5444d1e338dde5dd78f2a811288e4f8b80eddb6d30951e3398144d`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _host, entry. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[7]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[7].value::Call

Source: `infra/agentinfra/roadmap_download.py:120`; AST `b7ddebea85036481e4dba097454dee4d8a8bf6eebf24574c45cfe52f4a6492eb`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _host, entry. Outputs/bindings: (none).
Calls/effect boundaries: _host.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8]::If

Source: `infra/agentinfra/roadmap_download.py:121`; AST `66ef3591d697f2716673344874cf74b5a58c13a5723b960aa7b8950071972262`.

Rust module: `infra::agentinfra::roadmap_download`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: digest, entry, path, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.exists, path.read_bytes, path.stat, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[21].body[8]; no call, error or mutation may be omitted. Condition: path.exists()
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].test::Call

Source: `infra/agentinfra/roadmap_download.py:121`; AST `2cac3ec82b344023c57b4bbfcae282698ef12842cbda26a14724eacbefb97016`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.exists.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].test; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:122`; AST `56f9ee17c7d99b85bf5e19679e7d59712585bbe405c605ef40d343ed9216cb1d`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, entry, path, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, path.stat, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[8].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:122`; AST `5996559e63837d530887d6a3280cc13278b2bf57cb326988f783804e2f0d693b`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, entry, path, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes, path.stat, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[0].value.args[0].values[0].left.value::Call

Source: `infra/agentinfra/roadmap_download.py:122`; AST `4ad13a92d4c0491c8737b8fcfacd38c225911ac2f24bdb5ec5c2f1fd76d4a178`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.stat.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value.args[0].values[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[0].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_download.py:122`; AST `151b0d9c74498c5db6945d2f21a20eb1cef9e3526483e1b6e5ed66c8ee0f1765`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.read_bytes.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[0].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:122`; AST `f35916bc21a833a57a0dd89398b2dab5479cd1f3ef04b46f456d03ce95b67eac`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: path.read_bytes.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[8].body[0].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[8].body[1]::Return

Source: `infra/agentinfra/roadmap_download.py:123`; AST `6a83e41742422cefd09401a733b9520de25fdaca4b583a6ac2a8659697bf9fee`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[21].body[8].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[9]::Assign

Source: `infra/agentinfra/roadmap_download.py:124`; AST `0f9c9c6b6a6f59b62a00e4c2d4de41b8cd716cfa22b9363afa6f4adb196753f5`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: confined_path, directory, name, root. Outputs/bindings: partial.
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[9]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[9].value::Call

Source: `infra/agentinfra/roadmap_download.py:124`; AST `3c577bb3208cf3ef5e0c7e14bed9a44de6a2db34c1d33bda60d21fa420dafde8`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: confined_path, directory, name, root. Outputs/bindings: (none).
Calls/effect boundaries: confined_path.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[10]::Assign

Source: `infra/agentinfra/roadmap_download.py:125`; AST `1ec989b9ad13a3b4622bd33d76ecc154e23808872fb34808422ca855a8f21843`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: observations.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[10]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[11]::Assign

Source: `infra/agentinfra/roadmap_download.py:126`; AST `dc997ecc6eecf021cae472d401abf27f3e7b4619b26860310b2e908ffd2f1d81`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _HTTPSHandler, _HTTPSRedirect, observations, urllib. Outputs/bindings: opener.
Calls/effect boundaries: _HTTPSHandler, _HTTPSRedirect, urllib.request.ProxyHandler, urllib.request.build_opener.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[11]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[11].value::Call

Source: `infra/agentinfra/roadmap_download.py:126`; AST `dfaef484409ea69ab21c3c9e27ea674dcd7cd2bc8a902db74b9b80fcbaa760a3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSHandler, _HTTPSRedirect, observations, urllib. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSHandler, _HTTPSRedirect, urllib.request.ProxyHandler, urllib.request.build_opener.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[11].value.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:126`; AST `0086d7b8075371bb1d7ec3a29ffaeaf0124a924b0d1be31466cd7dfc271e752c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.ProxyHandler.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[11].value.args[1]::Call

Source: `infra/agentinfra/roadmap_download.py:126`; AST `54febd1ac2be474215e29ca118c4dcd44c8616318e80d0e4d2a3fda9a1e4bf00`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSHandler, observations. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSHandler.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[11].value.args[2]::Call

Source: `infra/agentinfra/roadmap_download.py:126`; AST `852721db4df1179ed4639cf5a496d7d4151de242aca1946ec35125dfa2852d28`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSRedirect. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSRedirect.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[11].value.args[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[12]::Assign

Source: `infra/agentinfra/roadmap_download.py:127`; AST `083bb478b8e61d32ac2fe5be271ba2c3d0bbcb595c966d89bb51d17e1c2f827b`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: created_partial.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[12]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13]::Try

Source: `infra/agentinfra/roadmap_download.py:128`; AST `275f5dcf629a2abef848dc87700b546ad66ac52c8cf4d35a0d07d267c275133c`.

Rust module: `infra::agentinfra::roadmap_download`. Result propagation plus typed error matching; finally via explicit cleanup on success/error/return, not Drop alone

Inputs: Exception, TRANSPORT, atomic_write_json, chunk, count, created_partial, digest, entry, exc, file_binding, len, name, observation, observations, opener, output, partial, path, request, require, response, root, type, urllib. Outputs/bindings: chunk, count, created_partial, observation, output, request, response.
Calls/effect boundaries: atomic_write_json, digest, file_binding, len, opener.open, output.write, partial.open, partial.read_bytes, partial.replace, partial.stat, partial.unlink, path.relative_to, path.relative_to(root).as_posix, path.with_name, require, response.read, type, urllib.request.Request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Try evaluation at root.body[21].body[13]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:129`; AST `0adba3aa994a352cb06593c41f5982022c869010653d8945cab70bf70e84e3fa`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: entry, urllib. Outputs/bindings: request.
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:129`; AST `d2a2de71fe73b636d8cfe57b9b2ad55c9da699042c5a7c44a0bf00a1da4d30cb`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: entry, urllib. Outputs/bindings: (none).
Calls/effect boundaries: urllib.request.Request.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1]::With

Source: `infra/agentinfra/roadmap_download.py:130`; AST `8d741dc6d7dc5ced41cd20741dfb1622c1fe1ad96929c33ef8c1fd20c4f886ee`.

Rust module: `infra::agentinfra::roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: chunk, count, entry, len, opener, output, partial, request, require, response. Outputs/bindings: chunk, count, created_partial, output, response.
Calls/effect boundaries: len, opener.open, output.write, partial.open, require, response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[21].body[13].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_download.py:130`; AST `d69befc9e3a8260136447ac1cdc4f0cce2a7c0aa071b41f33ae4c915dfb1772c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, request. Outputs/bindings: (none).
Calls/effect boundaries: opener.open.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0]::With

Source: `infra/agentinfra/roadmap_download.py:131`; AST `c3342e98b40b710da831585f47cacc96d3bcc02ab544dc0610f2b430191f54ff`.

Rust module: `infra::agentinfra::roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: chunk, count, entry, len, output, partial, require, response. Outputs/bindings: chunk, count, created_partial, output.
Calls/effect boundaries: len, output.write, partial.open, require, response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered With evaluation at root.body[21].body[13].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].items[0].context_expr::Call

Source: `infra/agentinfra/roadmap_download.py:131`; AST `92f388e9646ee4657b38dfa4bd0c9d93c0b1ad88a241b1b3eccdb08cabd90143`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.open.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:132`; AST `da4559351b05a3acedcfb39b40091a66ecb826a6e5e1d0d9b94c3d769f61c431`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: created_partial.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[1]::Assign

Source: `infra/agentinfra/roadmap_download.py:133`; AST `9877e74e9138ca519b63cde50b3596d489a3e370eafa3e6631170511d7d0a668`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: count.
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13].body[1].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2]::While

Source: `infra/agentinfra/roadmap_download.py:134`; AST `713e35b00c18da0b899f45e6ad31b4795207a80c3cc50e4321ef3b71cac30d3f`.

Rust module: `infra::agentinfra::roadmap_download`. while with explicit truth conversion and a normal-exhaustion flag for loop else

Inputs: chunk, count, entry, len, output, require, response. Outputs/bindings: chunk, count.
Calls/effect boundaries: len, output.write, require, response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered While evaluation at root.body[21].body[13].body[1].body[0].body[2]; no call, error or mutation may be omitted. Condition: (chunk := response.read(262144))
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].test.value::Call

Source: `infra/agentinfra/roadmap_download.py:134`; AST `1cee9a653703d92d14b9fef8ddcd91dc0c6a9b64d2daeb61f5c51045c6d545f8`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: response. Outputs/bindings: (none).
Calls/effect boundaries: response.read.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].body[0].body[2].test.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[0]::AugAssign

Source: `infra/agentinfra/roadmap_download.py:135`; AST `18bcba3de3adda48da4f4c2e4b2317f2e1615e978aee1fdcbef98e021a6f6c02`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, len. Outputs/bindings: count.
Calls/effect boundaries: len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered AugAssign evaluation at root.body[21].body[13].body[1].body[0].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:135`; AST `6f99d4ecb2708ba92e74d7c76fd9b2c1d7b1aa91d619b54799b549e649104fc3`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, len. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].body[0].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:136`; AST `9d4c265b3541f5fbd887b0a86c4968c148f001beca0203ffc9568b70127dd219`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: count, entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].body[1].body[0].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:136`; AST `d3a3d82509d78cc9be1d798e7be59b2b2cc6f7ab7b176e339cf69d394de1ea53`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: count, entry, require. Outputs/bindings: (none).
Calls/effect boundaries: require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].body[0].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[2]::Expr

Source: `infra/agentinfra/roadmap_download.py:137`; AST `9c802f4657e8e7d7607ed61235070098592ebe3b89265147793dd56aa51c617c`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].body[1].body[0].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[1].body[0].body[2].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:137`; AST `190360950a5fd203e4c19531c04f75f94bc12254565043396c7251615d294d97`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: chunk, output. Outputs/bindings: (none).
Calls/effect boundaries: output.write.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[1].body[0].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[2]::Expr

Source: `infra/agentinfra/roadmap_download.py:138`; AST `cd557379ce708afe9198ae6296b3ef2a2c9a9eea90a9a2a5a0206aeeea0c1732`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, entry, partial, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, partial.read_bytes, partial.stat, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[2].value::Call

Source: `infra/agentinfra/roadmap_download.py:138`; AST `fd2f0f040b3d5fd7159962fcd6435decbce95afce68aa3824a74f9f78e6cf854`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, entry, partial, require. Outputs/bindings: (none).
Calls/effect boundaries: digest, partial.read_bytes, partial.stat, require.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[2].value.args[0].values[0].left.value::Call

Source: `infra/agentinfra/roadmap_download.py:138`; AST `d13f4f794eeeff55b0b6fac7ccfad14b159e7e5c6d65edb3367d19b03ddeabaf`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.stat.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[2].value.args[0].values[0].left.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[2].value.args[0].values[1].left::Call

Source: `infra/agentinfra/roadmap_download.py:138`; AST `14f5062f1adebde124aa5a8aad87c775fb14612e54a57f3dbef88eca27a8b91d`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, partial. Outputs/bindings: (none).
Calls/effect boundaries: digest, partial.read_bytes.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[2].value.args[0].values[1].left; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[2].value.args[0].values[1].left.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:138`; AST `036cf7dddaf576ab4be59cf3ea4fc55cafb37cfe12cfe42e258ae18502a59d30`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[2].value.args[0].values[1].left.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[3]::Expr

Source: `infra/agentinfra/roadmap_download.py:140`; AST `5ca73aad0a55c6122a07de6b0b096b238257f862e4288b3fb82784db52ee51ee`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, path. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].body[3]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[3].value::Call

Source: `infra/agentinfra/roadmap_download.py:140`; AST `defb26026241ff1786b5e36da425c850bc9b0e05b03bbb45519fea34f8f829b2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, path. Outputs/bindings: (none).
Calls/effect boundaries: partial.replace.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[3].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[4]::Assign

Source: `infra/agentinfra/roadmap_download.py:141`; AST `b0ecb9d22e23ae7381348eab581e12f669bc2f37d0edb7ec83e0945c325975c0`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TRANSPORT, entry, file_binding, observations, path, root. Outputs/bindings: observation.
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13].body[4]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[4].value.values[5]::Call

Source: `infra/agentinfra/roadmap_download.py:142`; AST `2c1d399eb4c612b95d094d3989bf013bade70bc9afc145ec6ca0de71d6073a62`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: file_binding, path, root. Outputs/bindings: (none).
Calls/effect boundaries: file_binding, path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[4].value.values[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[4].value.values[5].args[1]::Call

Source: `infra/agentinfra/roadmap_download.py:142`; AST `2f3ab1cd4435482e9deaec71c32560d3a214e14c3eec141863849b08b1adbff2`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to, path.relative_to(root).as_posix.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[4].value.values[5].args[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[4].value.values[5].args[1].func.value::Call

Source: `infra/agentinfra/roadmap_download.py:142`; AST `df824b5a113961d2610a343101ca8ee57ac38940291986e8747d493969d1955c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: path, root. Outputs/bindings: (none).
Calls/effect boundaries: path.relative_to.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[4].value.values[5].args[1].func.value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[5]::Expr

Source: `infra/agentinfra/roadmap_download.py:143`; AST `63ccf8a6fd0d680961fb9ba32b8ce02bc26f842e901690f92921176437513036`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, digest, name, observation, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].body[5]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[5].value::Call

Source: `infra/agentinfra/roadmap_download.py:143`; AST `766ad2b0a743b34c8fe4e374c72576a84c7a12f4730b580055d642894774943b`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, digest, name, observation, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[5].value.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:143`; AST `2b13342faaee51e26b639356a93dddc918ac3586cc6d1dc4b366d2d30b94dcf1`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, observation, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[5].value.args[0].args[0].left.right::Call

Source: `infra/agentinfra/roadmap_download.py:143`; AST `1af2dcd5f19d85a8db08951a0b972298a6efa0e6a519bf5bdfb56892001b494c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, observation. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].body[5].value.args[0].args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].body[6]::Return

Source: `infra/agentinfra/roadmap_download.py:144`; AST `6a83e41742422cefd09401a733b9520de25fdaca4b583a6ac2a8659697bf9fee`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: path. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Return evaluation at root.body[21].body[13].body[6]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0]::ExceptHandler

Source: `infra/agentinfra/roadmap_download.py:145`; AST `f0fa9a3a5d4c4b979d4985d796036e08b3c3913fc67e636a23e9f924b44d6eb7`.

Rust module: `infra::agentinfra::roadmap_download`. match on source error enum preserving exception subtype matching and binding cleanup

Inputs: Exception, TRANSPORT, atomic_write_json, digest, entry, exc, name, observation, observations, path, root, type. Outputs/bindings: observation.
Calls/effect boundaries: atomic_write_json, digest, path.with_name, type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered ExceptHandler evaluation at root.body[21].body[13].handlers[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[0]::Assign

Source: `infra/agentinfra/roadmap_download.py:146`; AST `b5827ce367b00d544216d264f938c91c45fab739b07684cbb51c292bdb1f8334`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: TRANSPORT, entry, exc, observations, type. Outputs/bindings: observation.
Calls/effect boundaries: type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Assign evaluation at root.body[21].body[13].handlers[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[0].value.values[5].value::Call

Source: `infra/agentinfra/roadmap_download.py:147`; AST `760fdaff1a05c24c8db8bb1ee0c475c11403d48d9ac9c89ec3c062a1494d5d01`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: exc, type. Outputs/bindings: (none).
Calls/effect boundaries: type.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].handlers[0].body[0].value.values[5].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[1]::Expr

Source: `infra/agentinfra/roadmap_download.py:148`; AST `63ccf8a6fd0d680961fb9ba32b8ce02bc26f842e901690f92921176437513036`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: atomic_write_json, digest, name, observation, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].handlers[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[1].value::Call

Source: `infra/agentinfra/roadmap_download.py:148`; AST `766ad2b0a743b34c8fe4e374c72576a84c7a12f4730b580055d642894774943b`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: atomic_write_json, digest, name, observation, path, root. Outputs/bindings: (none).
Calls/effect boundaries: atomic_write_json, digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].handlers[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[1].value.args[0]::Call

Source: `infra/agentinfra/roadmap_download.py:148`; AST `2b13342faaee51e26b639356a93dddc918ac3586cc6d1dc4b366d2d30b94dcf1`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, name, observation, path. Outputs/bindings: (none).
Calls/effect boundaries: digest, path.with_name.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].handlers[0].body[1].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[1].value.args[0].args[0].left.right::Call

Source: `infra/agentinfra/roadmap_download.py:148`; AST `1af2dcd5f19d85a8db08951a0b972298a6efa0e6a519bf5bdfb56892001b494c`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, observation. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].handlers[0].body[1].value.args[0].args[0].left.right; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].handlers[0].body[2]::Raise

Source: `infra/agentinfra/roadmap_download.py:149`; AST `ba28128c14dfbd0a9062c0dbab42ad6c52ecf0767df6b67576deb1dbbfdd038d`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Raise evaluation at root.body[21].body[13].handlers[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].finalbody[0]::If

Source: `infra/agentinfra/roadmap_download.py:151`; AST `7ac9e39d9ed89de45a4ebfecd7880078cf37cdc8a8772f728df0b7be67ceefce`.

Rust module: `infra::agentinfra::roadmap_download`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: created_partial, partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.unlink.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered If evaluation at root.body[21].body[13].finalbody[0]; no call, error or mutation may be omitted. Condition: created_partial
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].finalbody[0].body[0]::Expr

Source: `infra/agentinfra/roadmap_download.py:152`; AST `c8b1cc5c87404786a7b09c1b8a6ad3b9ae763d620ca5793178faeca3e984e41a`.

Rust module: `infra::agentinfra::roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.unlink.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Expr evaluation at root.body[21].body[13].finalbody[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/agentinfra/roadmap_download.py::module::download_pinned::root.body[21].body[13].finalbody[0].body[0].value::Call

Source: `infra/agentinfra/roadmap_download.py:152`; AST `b044bc7ceed7e45ffe94c8d921985ddc99621a5d560ae8c12bf6575232c56fce`.

Rust module: `infra::agentinfra::roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.unlink.
Dependencies: __future__, atomic, http.client, ipaddress, pathlib, roadmap_records, security, socket, ssl, time, urllib.parse, urllib.request.

Invariants: Preserve ordered Call evaluation at root.body[21].body[13].finalbody[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: std::fs / std::path::PathBuf; std::time::Instant / SystemTime
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
