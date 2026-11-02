# Python to Rust behavioral correspondence

Generated from actual Python ASTs. Every entry is a migration proposal, not a completed Rust implementation or a proof.

Files: 1. Behavioral units: 202. Inventory digest: `26072537f2aaeabf2d52da460f314c708bf3d233b50f2715926499dbd5381f95`.

Line numbers are navigation only. AST routes and source hashes bind identities; an edit requires regeneration and review.

## infra/tests/test_roadmap_download.py::module::root::Module

Source: `infra/tests/test_roadmap_download.py:1`; AST `7c487bf099fa5d8cd89b835a2d8de6ca951f94014362a6f9a0fbae1a890eed90`.

Rust module: `infra::tests::test_roadmap_download`. Rust module; explicit initialization function for module-level effects; no hidden import-time mutation

Inputs: ContractError, FileExistsError, MagicMock, Path, _HTTPSHandler, _HTTPSRedirect, _ResolvedConnection, __name__, _addresses, base, build, cache, connect, connection, context, dict, digest, directory, download_pinned, events, first, handler, io, json, len, next, observation, opener, partial, patch, raw, root, second, self, sock, ssl, target, tempfile, unittest, update, url, wrapped. Outputs/bindings: base, build, cache, connect, connection, context, directory, events, first, handler, observation, opener, partial, raw, root, second, sock, target, update, url, wrapped.
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, (root / 'downloads/tool.whl.partial').exists, MagicMock, Path, _HTTPSHandler, _HTTPSRedirect, _HTTPSRedirect().redirect_request, _ResolvedConnection, _addresses, cache.glob, cache.mkdir, connect.assert_called_once_with, connection.connect, context.wrap_socket.assert_called_once_with, dict, digest, download_pinned, first.parent.glob, io.BytesIO, json.dumps, json.dumps(base).encode, json.dumps(dict(base, **update)).encode, json.loads, len, next, next(cache.glob('tool.whl.transport-*.json')).read_text, next(first.parent.glob('tool.whl.transport-*.json')).read_text, partial.read_bytes, partial.write_bytes, patch, self.assertEqual, self.assertFalse, self.assertRaises, self.assertTrue, self.entry, self.subTest, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory, unittest.main.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Module evaluation at root; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:1`; AST `12e62e0a3052f8c5e87483c4a395bcfa006f0e0dbb30e6a71ac76756c8df0ea7`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[1]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:2`; AST `890bede517510aea64e32258c9530f0172f5a6ea2fcbcb247fdadc40c714e8bf`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[2]::Import

Source: `infra/tests/test_roadmap_download.py:4`; AST `eb75a54c5d0d93fbb694f468951613f2f071166afbbe97a52903fa47a7cef914`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[3]::Import

Source: `infra/tests/test_roadmap_download.py:5`; AST `211ee42757705c7e350e70e36b762987a737f5e9c268f2a343e2dbfcb8fbea75`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[4]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:6`; AST `59051b17634cdcb5a576ceb58fdc0a4e5652ed3b60d66667e92ddefd931abeca`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[5]::Import

Source: `infra/tests/test_roadmap_download.py:7`; AST `d58f4a781306aa988c2a48663bae1b9c9f8057e04c8f1f102adaea8473a930a5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[6]::Import

Source: `infra/tests/test_roadmap_download.py:8`; AST `81dafa7a7cf16b83e7a7cafd7a6702e15f4b4d576a43463dc14beb05d48e72d0`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[7]::Import

Source: `infra/tests/test_roadmap_download.py:9`; AST `c2989ab60afe692e3752cff01ca6c5975c26cf4d65ed0ff66c3e1ddd0062fe42`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Import evaluation at root.body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[8]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:10`; AST `937f8a8f682ae07d815a1d46ccc17ac9444a6f3642280c2a6a8a97ce1d204407`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[9]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:12`; AST `ab25d1d7df7077b45a06a077e07627781b3fd05f8fbfcce536cdd24bdfac2978`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[10]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:14`; AST `5b90894d096758c9f19f8600da372bc7cd3d8c63d0642e575f9761c8cc9880e1`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[11]::ImportFrom

Source: `infra/tests/test_roadmap_download.py:15`; AST `4ebb9c04f674efba34eea0d94b98300ffce918cbc00172faaa57fabaa2093a52`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ImportFrom evaluation at root.body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::root.body[12]::ClassDef

Source: `infra/tests/test_roadmap_download.py:18`; AST `664ceb7cab990926e7314547d5c0821cd79abc3f763172f2ce61f6afcfd55d8d`.

Rust module: `infra::tests::test_roadmap_download`. Original-named struct/enum plus trait and impl group; explicit fields and source-owned methods

Inputs: ContractError, FileExistsError, MagicMock, Path, _HTTPSHandler, _HTTPSRedirect, _ResolvedConnection, _addresses, base, build, cache, connect, connection, context, dict, digest, directory, download_pinned, events, first, handler, io, json, len, next, observation, opener, partial, patch, raw, root, second, self, sock, ssl, target, tempfile, unittest, update, url, wrapped. Outputs/bindings: base, build, cache, connect, connection, context, directory, events, first, handler, observation, opener, partial, raw, root, second, sock, target, update, url, wrapped.
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, (root / 'downloads/tool.whl.partial').exists, MagicMock, Path, _HTTPSHandler, _HTTPSRedirect, _HTTPSRedirect().redirect_request, _ResolvedConnection, _addresses, cache.glob, cache.mkdir, connect.assert_called_once_with, connection.connect, context.wrap_socket.assert_called_once_with, dict, digest, download_pinned, first.parent.glob, io.BytesIO, json.dumps, json.dumps(base).encode, json.dumps(dict(base, **update)).encode, json.loads, len, next, next(cache.glob('tool.whl.transport-*.json')).read_text, next(first.parent.glob('tool.whl.transport-*.json')).read_text, partial.read_bytes, partial.write_bytes, patch, self.assertEqual, self.assertFalse, self.assertRaises, self.assertTrue, self.entry, self.subTest, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered ClassDef evaluation at root.body[12]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::entry::root.body[12].body[0]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:19`; AST `cf10b359e34eae77778e6463aa6b97274848ca9c86f918e907b3741f793b23e1`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: digest, len, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::entry::root.body[12].body[0].body[0]::Return

Source: `infra/tests/test_roadmap_download.py:20`; AST `af44eead1bba0f0d82268f4e406982e8276ccea0acf6fd9595646e8e25eaa23f`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, len, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest, len.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Return evaluation at root.body[12].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::entry::root.body[12].body[0].body[0].value.values[2]::Call

Source: `infra/tests/test_roadmap_download.py:21`; AST `14381ee198b233fab86e0cefdac3169f8ede2b4f94479d019dcd9cc290015a66`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: len, raw. Outputs/bindings: (none).
Calls/effect boundaries: len.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value.values[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::entry::root.body[12].body[0].body[0].value.values[3]::Call

Source: `infra/tests/test_roadmap_download.py:21`; AST `5bdb5d1eee130dbed52cd02b55d2bae0a08474ef4a3589a2f763913acb5ea48a`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, raw. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[0].body[0].value.values[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:23`; AST `440a88c39d7a56032fbe3a2d08e01c0791c47159485dd18d2c22bf10f7cd3c47`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: MagicMock, _ResolvedConnection, connect, connection, context, digest, events, patch, self, sock, wrapped. Outputs/bindings: connect, connection, context, events, sock, wrapped.
Calls/effect boundaries: MagicMock, _ResolvedConnection, connect.assert_called_once_with, connection.connect, context.wrap_socket.assert_called_once_with, digest, patch, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:24`; AST `454ad447a37ec76ba263331cf0d7dd34013422512337e372faec0726bdd1ec99`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MagicMock. Outputs/bindings: context, sock, wrapped.
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[0].value.elts[0]::Call

Source: `infra/tests/test_roadmap_download.py:24`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value.elts[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[0].value.elts[1]::Call

Source: `infra/tests/test_roadmap_download.py:24`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value.elts[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[0].value.elts[2]::Call

Source: `infra/tests/test_roadmap_download.py:24`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[0].value.elts[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:25`; AST `125b305d728e0de18b7d6758848a674aa0db8665fcef063518a48a0ebd81bacf`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, wrapped. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[2]::Assign

Source: `infra/tests/test_roadmap_download.py:26`; AST `bb67865fd1ebce537ce65072f4a521d603845ae7f40a747f773eb3bc639571c5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: wrapped. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[3]::Assign

Source: `infra/tests/test_roadmap_download.py:27`; AST `1b562acb2224eb377208f6ca3e0c5a8ac85aca093c484088a60e5b675901f33a`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: wrapped. Outputs/bindings: (none).
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[4]::Assign

Source: `infra/tests/test_roadmap_download.py:28`; AST `3dfda99c274ceff9a44741d7d253e73edaec04eca0b4b7f37a2405d605721baa`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: events.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[5]::Assign

Source: `infra/tests/test_roadmap_download.py:29`; AST `eac573d97fe087f4d6fa82494e8a0e03effbaae74d019eee23018d2dc5b7ac2e`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _ResolvedConnection, context, events. Outputs/bindings: connection.
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[1].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[5].value::Call

Source: `infra/tests/test_roadmap_download.py:29`; AST `c7f44720cd42baab1daf3bfe662b896eb19f9a213c22772f1ae13c96f4c8fc0f`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _ResolvedConnection, context, events. Outputs/bindings: (none).
Calls/effect boundaries: _ResolvedConnection.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[6]::With

Source: `infra/tests/test_roadmap_download.py:30`; AST `3da5925c3b3380f88ffd278a5210cc0cc3a79320ca10cee49a97447d97c31a0d`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: connection, patch, sock. Outputs/bindings: connect.
Calls/effect boundaries: connection.connect, patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[1].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[6].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:30`; AST `498b97f1887a344e16ee1150fd3f8e5921822485d5a386d2095362ae666562a4`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[6].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[6].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:30`; AST `4f32b8aee8681835ca38d93af499549dd33954c2805a03666336a9db792d5f96`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: patch, sock. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[6].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[6].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:31`; AST `93ca944a1d091469a570e82cdf46f1eb4bfe7d7acbe112efac23be09a94627a5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: connection. Outputs/bindings: (none).
Calls/effect boundaries: connection.connect.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[6].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:31`; AST `52e57fce3a7885ad6244c9adbdfa3eea50a74b02bcfa161890f4f83337299dad`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: connection. Outputs/bindings: (none).
Calls/effect boundaries: connection.connect.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[6].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[7]::Expr

Source: `infra/tests/test_roadmap_download.py:32`; AST `a16748ee650b83dcb1889806feb56f96be9d6d2807b7dcb354325dc7cc854ef0`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: connect. Outputs/bindings: (none).
Calls/effect boundaries: connect.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[7].value::Call

Source: `infra/tests/test_roadmap_download.py:32`; AST `0c96ad3f654120233fa31dc4884302ef68b7331b3a7319b90020fd038a1deedc`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: connect. Outputs/bindings: (none).
Calls/effect boundaries: connect.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[8]::Expr

Source: `infra/tests/test_roadmap_download.py:33`; AST `7a9048d17c2112e6674ed4a4b1bd251d2ec62d9fcf1914af24bf78f49c2b9f3e`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: context, sock. Outputs/bindings: (none).
Calls/effect boundaries: context.wrap_socket.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[8].value::Call

Source: `infra/tests/test_roadmap_download.py:33`; AST `e95e4435de2a09171c663e4932d2f3f7e7b69beb60ff233e820573ae163ca90e`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: context, sock. Outputs/bindings: (none).
Calls/effect boundaries: context.wrap_socket.assert_called_once_with.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[9]::Expr

Source: `infra/tests/test_roadmap_download.py:34`; AST `aee40fd76440c53f477df6b7a423e4faf3a22c43f7ab301605f33c18dec07529`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: connection, self, wrapped. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[9].value::Call

Source: `infra/tests/test_roadmap_download.py:34`; AST `1343e1f5641805f37a0ed2d1f67d65b83dd6e552b9fe50cb76220bf68db21f79`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: connection, self, wrapped. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[10]::Expr

Source: `infra/tests/test_roadmap_download.py:35`; AST `b9ef53b633d5d1ba6abb45cbb2c0878a3aa8f08f23120aef7f93523eb7d941a5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: digest, events, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[10].value::Call

Source: `infra/tests/test_roadmap_download.py:35`; AST `bd28b6f4efd7a39ed0ea97ddbb8093777440eaab1bf02bc5a7a05b41201ecf1a`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest, events, self. Outputs/bindings: (none).
Calls/effect boundaries: digest, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[10].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:35`; AST `819905aaa3fbab54d8649123e11e568f527cc2528fca4ec176695697bed79b93`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: digest. Outputs/bindings: (none).
Calls/effect boundaries: digest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[10].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[11]::Expr

Source: `infra/tests/test_roadmap_download.py:36`; AST `4fb7ea5e5c5ca1a57812f56b359b6ec2afdb794f8ff859b64b27a521bfc3f6c2`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: events, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[1].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_selected_ip_preserves_original_tls_hostname_and_certificate_observation::root.body[12].body[1].body[11].value::Call

Source: `infra/tests/test_roadmap_download.py:36`; AST `bb4b9446121aca34c067148d6613bf5b61f83d9b0d0ad8a891e49555151bf251`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: events, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[1].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:38`; AST `4838dc6761ffe2668f55864f0f23d5dc4e56a3f0de6be6757c2f16a7da48144c`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: _HTTPSHandler, handler, self, ssl. Outputs/bindings: handler.
Calls/effect boundaries: _HTTPSHandler, self.assertEqual, self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:39`; AST `208c1e92370be1ceb65d352a83dbef0a59af52abafef210ebe8b3b3b6c98cc18`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _HTTPSHandler. Outputs/bindings: handler.
Calls/effect boundaries: _HTTPSHandler.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[2].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:39`; AST `305c07eeaf4ce515ccd4193bc4faca28ca95f39ce2370bd908b3b2bbd49ddb1a`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSHandler. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSHandler.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[1]::Expr

Source: `infra/tests/test_roadmap_download.py:40`; AST `ac748a18dd34512a29014521b8e58046ec9e9ce2725e1c2d0b1532bd18d9e2c2`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: handler, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[1].value::Call

Source: `infra/tests/test_roadmap_download.py:40`; AST `fc29c1afb6acd80d7a8116bd9089e05c42623302b85c491f81cf021a1cd7e4d6`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handler, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[2]::Expr

Source: `infra/tests/test_roadmap_download.py:41`; AST `e6d064928d9d5f99585b36cd6ce3be19ce1bb4c9f7a163465a2dca1154ed143f`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: handler, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[2].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tls_handler_requires_default_certificate_and_hostname_verification::root.body[12].body[2].body[2].value::Call

Source: `infra/tests/test_roadmap_download.py:41`; AST `4c17562878ee548879e6aa8e0649d6f48f802a3b301f1ad9fa97167c15321c71`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: handler, self, ssl. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[2].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:43`; AST `5f20ab10b8f3e8daa9bcb05d05a5896fdfa879dc5760a5b85d30f85a32459086`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, _addresses, base, dict, events, io, json, patch, self, update. Outputs/bindings: base, events, update.
Calls/effect boundaries: _addresses, dict, io.BytesIO, json.dumps, json.dumps(base).encode, json.dumps(dict(base, **update)).encode, patch, self.assertEqual, self.assertRaises, self.assertTrue, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:44`; AST `9a72b6cf048410d0f12d9f03fd322602698ce0fd8455354f9b6b0bb028e9b128`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: base.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1]::For

Source: `infra/tests/test_roadmap_download.py:46`; AST `8a205cefa045499684bd860e3842a07d42b69a64002391f22863309b2002403d`.

Rust module: `infra::tests::test_roadmap_download`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, _addresses, base, dict, io, json, patch, self, update. Outputs/bindings: update.
Calls/effect boundaries: _addresses, dict, io.BytesIO, json.dumps, json.dumps(dict(base, **update)).encode, patch, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[3].body[1]; no call, error or mutation may be omitted. Iteration: update in ({'Status': False}, {'TC': True}, {'CD': True}, {'Question': [{'name': 'other.example', 'type': 1}]}, {'Answer': []}, {'Answer': [{'type': 1, 'data': '127.0.0.1'}]})
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0]::With

Source: `infra/tests/test_roadmap_download.py:48`; AST `95e85fa2956bbcb5a9e2c822b056c0945fd0aa80867f836882e874c2300bc4dd`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, _addresses, base, dict, io, json, patch, self, update. Outputs/bindings: (none).
Calls/effect boundaries: _addresses, dict, io.BytesIO, json.dumps, json.dumps(dict(base, **update)).encode, patch, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[1].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `89799ee3b9235393b3b4cb9a263a1f1550412f66a0ad747fbd4e0c88d7fd6569`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, update. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `e430671223cf0c1ca78a40b017aedb54247d8c4f2ed6b63c07a2090144474b63`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, io, json, patch, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, io.BytesIO, json.dumps, json.dumps(dict(base, **update)).encode, patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `4a8e8950e4ecfe883e1b43bc0f86e420de6dccbb9ffa0192808c73da6fa6be97`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, io, json, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, io.BytesIO, json.dumps, json.dumps(dict(base, **update)).encode.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `7d5fa2830191a207a35c3a03a1eb843c82587c4b097869197e38bed31f1a3292`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, json, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, json.dumps, json.dumps(dict(base, **update)).encode.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `2409e7220d37769fc4ff768dca3678b59976508123b577a26125a9bbe7a1911c`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, json, update. Outputs/bindings: (none).
Calls/effect boundaries: dict, json.dumps.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0].func.value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:48`; AST `648aabe9eec3a7113d8aeea09ab1c0d48488d84604d574421a3cd30879b7a3a0`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, dict, update. Outputs/bindings: (none).
Calls/effect boundaries: dict.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].items[1].context_expr.keywords[0].value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].body[0]::With

Source: `infra/tests/test_roadmap_download.py:49`; AST `832b7a7d110b7e4018a03e6846b4826404002a1a8a09600caa6bf5208304bb94`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, _addresses, self. Outputs/bindings: (none).
Calls/effect boundaries: _addresses, self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[1].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:49`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:50`; AST `32ac406f6371ca4d274d7238ac27c8f9b0e32763211ee6b80fd6afd2c794e059`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _addresses. Outputs/bindings: (none).
Calls/effect boundaries: _addresses.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[1].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[1].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:50`; AST `2e533100778e7af5566d159846311ec3c7cfdd5e6da649db1920952f5c304bf3`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _addresses. Outputs/bindings: (none).
Calls/effect boundaries: _addresses.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[1].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[2]::Assign

Source: `infra/tests/test_roadmap_download.py:51`; AST `3dfda99c274ceff9a44741d7d253e73edaec04eca0b4b7f37a2405d605721baa`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: (none). Outputs/bindings: events.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[3].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3]::With

Source: `infra/tests/test_roadmap_download.py:52`; AST `4c29548af10f488e22b02edd4b0a468b433a04908516edad3dd8e9bbff70e04e`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: _addresses, base, events, io, json, patch, self. Outputs/bindings: (none).
Calls/effect boundaries: _addresses, io.BytesIO, json.dumps, json.dumps(base).encode, patch, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[3].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:52`; AST `03d7c2621dea2bc9bc050bfb14fdbae5447bad4fe8e1863558602f371d054915`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, io, json, patch. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, json.dumps, json.dumps(base).encode, patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value::Call

Source: `infra/tests/test_roadmap_download.py:52`; AST `ae90b6cba314b3720b94831a3c812b953a612b1b989bb5211fdd4840e625f4e6`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, io, json. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO, json.dumps, json.dumps(base).encode.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:52`; AST `bd634cef26dff7ed96a870d2d65e6662860d722e5142437701a2cf052e199a9f`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps, json.dumps(base).encode.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_download.py:52`; AST `ea9f9c3bd6dc46c7219b7d57a8098359c6ccde7b92b2fc650703d3772ad69872`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: base, json. Outputs/bindings: (none).
Calls/effect boundaries: json.dumps.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].items[0].context_expr.keywords[0].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:53`; AST `b37e32e622e163368babb2463d6f5f282a6178efa38426c848b46ddc1df28d3c`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _addresses, events, self. Outputs/bindings: (none).
Calls/effect boundaries: _addresses, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:53`; AST `b12bbe93b32a75204b7aa72ed9160429b4c7b2a9f6d77cfc53bb3606c39528bd`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _addresses, events, self. Outputs/bindings: (none).
Calls/effect boundaries: _addresses, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[3].body[0].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:53`; AST `45c84b4bb7a0513c11a13b915ee647a997090dd37b46f35d525d00cc60ca89d5`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _addresses, events. Outputs/bindings: (none).
Calls/effect boundaries: _addresses.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[3].body[0].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[4]::Expr

Source: `infra/tests/test_roadmap_download.py:54`; AST `15d0ed57e57ad9f849f282d6c7a68d46f18a2896fca873d3062b4975f8ba2c47`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: events, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[3].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_dns_wrong_question_truncation_disabled_validation_and_private_addresses_rejected::root.body[12].body[3].body[4].value::Call

Source: `infra/tests/test_roadmap_download.py:54`; AST `33500522ce57cf61ceab187f2d4d44910994d766b23a3389a46c3520ec267182`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: events, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertTrue.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[3].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:56`; AST `0257f1671bffbc8d47c545bbf9d5b00a6c132fdcf3e55cb62dd8733915c7da1b`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, MagicMock, Path, directory, download_pinned, io, opener, patch, raw, root, self, tempfile. Outputs/bindings: directory, opener, raw, root.
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, (root / 'downloads/tool.whl.partial').exists, MagicMock, Path, download_pinned, io.BytesIO, patch, self.assertFalse, self.assertRaises, self.entry, self.subTest, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0]::For

Source: `infra/tests/test_roadmap_download.py:57`; AST `fb5e44af64849d46cec1b144755380a588e1497566c12b39bea16907127d0fcd`.

Rust module: `infra::tests::test_roadmap_download`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, MagicMock, Path, directory, download_pinned, io, opener, patch, raw, root, self, tempfile. Outputs/bindings: directory, opener, raw, root.
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, (root / 'downloads/tool.whl.partial').exists, MagicMock, Path, download_pinned, io.BytesIO, patch, self.assertFalse, self.assertRaises, self.entry, self.subTest, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[4].body[0]; no call, error or mutation may be omitted. Iteration: raw in (b'wrong! wheel', b'pinned wheel with extra bytes')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0]::With

Source: `infra/tests/test_roadmap_download.py:58`; AST `afd73596eab4ad0b6d200b9811242b647cc4d5877379978d64ae77e91e195db1`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, MagicMock, Path, directory, download_pinned, io, opener, patch, raw, root, self, tempfile. Outputs/bindings: directory, opener, root.
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, (root / 'downloads/tool.whl.partial').exists, MagicMock, Path, download_pinned, io.BytesIO, patch, self.assertFalse, self.assertRaises, self.entry, self.subTest, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:58`; AST `9ec7834d458356e9ad81919c483b4510e66a6d95b9f2534fce0adf54de26b542`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: raw, self. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:58`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:59`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:59`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:60`; AST `85e0b1445612482f3bbf76f916286f957e1180fc06c67b00eec552cbe599c6fa`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MagicMock. Outputs/bindings: opener.
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_download.py:60`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_download.py:61`; AST `976d3a3a92b2033507bf10c5e883831c91826e8dfacefa28b0963a911b5cf9b9`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: io, opener, raw. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[4].body[0].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_download.py:61`; AST `03e041299d1332fc2f3d4cabb085f5cdc8bea1b3ca994e3db0027953277495f3`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io, raw. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3]::With

Source: `infra/tests/test_roadmap_download.py:62`; AST `d366e23e5ab8c347321458519be0f5fa5f6d091bd09f8ca2065c6491293b34ff`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, download_pinned, opener, patch, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, patch, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[0].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:62`; AST `cd79fc685515e859fba314c061795bd4e5ec5c4240d98095fe7b7055339e5231`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].body[0]::With

Source: `infra/tests/test_roadmap_download.py:63`; AST `fd22623b3bdcc52448e7a7b9b5e8e9b3d3653a52b614ab962b7e4fec76b8ba04`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[4].body[0].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:63`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[3].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:64`; AST `d9c7b78b2bb520381609d61604f0138150584bffa055ee54edb24db91bd75130`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[0].body[3].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:64`; AST `1d48e3e086934595192e7927e090c6bec61ccfcc9d16324d0dec1fbe2fd25b43`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[3].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[3].body[0].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:64`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[3].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_download.py:65`; AST `98a833e62d3899fbc6ab5a4f4111186b0f54fac63ca681cb00aeeb787d57747c`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_download.py:65`; AST `311c6406bfbe10fc90d455ad5d319b6c013be1a4bfa8a45b90771c06d90694fc`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[4].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:65`; AST `3819ba26fcc6658bf40c062653d49a77a175df1f0d58556eef9152dea5d8db6b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl').exists.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[4].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_download.py:66`; AST `6bc9ec5505ae1e0a83f9239666ca3864353ad39ef1c44b5bf6e3813b7de1beff`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl.partial').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[4].body[0].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_download.py:66`; AST `7ceec1e01459620be4ea44e2cfd0636f64aea08e8eba260be684127727c40136`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root, self. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl.partial').exists, self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_wrong_or_oversized_blob_is_never_promoted_and_partial_is_removed::root.body[12].body[4].body[0].body[0].body[5].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:66`; AST `242c458df31c33c40d8622e7723814d4c4cbb50c6c571f9204ca35ae8852aac2`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: root. Outputs/bindings: (none).
Calls/effect boundaries: (root / 'downloads/tool.whl.partial').exists.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[4].body[0].body[0].body[5].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:68`; AST `278d09097a5a3f119db3f387c046faf27271b4ac1031b549abba6df58d3c2108`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: MagicMock, Path, build, directory, download_pinned, first, io, json, next, observation, opener, patch, root, second, self, tempfile. Outputs/bindings: build, directory, first, observation, opener, root, second.
Calls/effect boundaries: MagicMock, Path, download_pinned, first.parent.glob, io.BytesIO, json.loads, next, next(first.parent.glob('tool.whl.transport-*.json')).read_text, patch, self.assertEqual, self.assertFalse, self.entry, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0]::With

Source: `infra/tests/test_roadmap_download.py:69`; AST `5c4c1f39abb8caa121438bd2dd2ab7751d3e2c46bb0d72d2130eecff32a1eeb1`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: MagicMock, Path, build, directory, download_pinned, first, io, json, next, observation, opener, patch, root, second, self, tempfile. Outputs/bindings: build, directory, first, observation, opener, root, second.
Calls/effect boundaries: MagicMock, Path, download_pinned, first.parent.glob, io.BytesIO, json.loads, next, next(first.parent.glob('tool.whl.transport-*.json')).read_text, patch, self.assertEqual, self.assertFalse, self.entry, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:69`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:70`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:70`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:71`; AST `85e0b1445612482f3bbf76f916286f957e1180fc06c67b00eec552cbe599c6fa`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MagicMock. Outputs/bindings: opener.
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[1].value::Call

Source: `infra/tests/test_roadmap_download.py:71`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[2]::Assign

Source: `infra/tests/test_roadmap_download.py:72`; AST `f435185e99b8f6490256b27492eef825e6a7ceba6e7a41667885992e86fe7efd`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: io, opener. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_download.py:72`; AST `67fba617a630dc27f549770dfe0d5d10c2992b59c02f537298fd92b7373b9d89`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3]::With

Source: `infra/tests/test_roadmap_download.py:73`; AST `90f7e6218de66987057dff5f4f5085c66eb6c470154741240f1699a3d8db9e89`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: download_pinned, opener, patch, root, self. Outputs/bindings: build, first, second.
Calls/effect boundaries: download_pinned, patch, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[5].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:73`; AST `cd79fc685515e859fba314c061795bd4e5ec5c4240d98095fe7b7055339e5231`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[3].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:74`; AST `97ad77e1b46170734a6716e155e7b2439287afca8973d1dc36a31e45460bf4da`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: download_pinned, root, self. Outputs/bindings: first.
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[3].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:74`; AST `1d48e3e086934595192e7927e090c6bec61ccfcc9d16324d0dec1fbe2fd25b43`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[3].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:74`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[3].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:75`; AST `988072f5daaf0965c6c869c54ae74f7cf6999947faa1099c751a07765a41983e`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: download_pinned, root, self. Outputs/bindings: second.
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[3].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[1].value::Call

Source: `infra/tests/test_roadmap_download.py:75`; AST `1d48e3e086934595192e7927e090c6bec61ccfcc9d16324d0dec1fbe2fd25b43`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[3].body[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[3].body[1].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:75`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[3].body[1].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_download.py:76`; AST `da9bd068ad06b387c70c98bc183249a7f1092bafbc9504da5101e82312a2c54b`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_download.py:76`; AST `4547e07b5ae6faef9b2873386f89cd351cafde8543f8c60a119f98fbcba2a23e`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, second, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[5]::Expr

Source: `infra/tests/test_roadmap_download.py:77`; AST `b58f13409eb90a7a810a7027764e48ee911782027e468aea8aa3d35f4e018912`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: build, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_download.py:77`; AST `abe18e1c935847448c80f3ee60884efce23b11370d55cc16e2b49b810d4695e6`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: build, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_download.py:78`; AST `79664d75afd64839efa2b1711b45aaedee6cab13c0e4b8701b319af0f25a814e`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: first, json, next. Outputs/bindings: observation.
Calls/effect boundaries: first.parent.glob, json.loads, next, next(first.parent.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[5].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_download.py:78`; AST `00695b19b4faf5de8afef41238e307a2931b6a485a67574e03976a802bd054f4`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, json, next. Outputs/bindings: (none).
Calls/effect boundaries: first.parent.glob, json.loads, next, next(first.parent.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:78`; AST `63d42517d3603b53db177d94feee2ddaba62c658241b7971db535cc3aca4eaa1`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, next. Outputs/bindings: (none).
Calls/effect boundaries: first.parent.glob, next, next(first.parent.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[6].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_download.py:78`; AST `bb3876363789e43c20da97213b26f188372d9ac789c0b0b790b3586d20d79a37`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first, next. Outputs/bindings: (none).
Calls/effect boundaries: first.parent.glob, next.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[6].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[6].value.args[0].func.value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:78`; AST `6f7028e5bcef883d9b772e255c6abfbf4d0169d63df6d6ed88ede2bc7edf15de`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: first. Outputs/bindings: (none).
Calls/effect boundaries: first.parent.glob.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[6].value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[7]::Expr

Source: `infra/tests/test_roadmap_download.py:79`; AST `c8356269f8654dbd81870ae2ce8f525b6c6143dcf160105bca0c461e260ca621`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[7].value::Call

Source: `infra/tests/test_roadmap_download.py:79`; AST `7d91a6f910cbd12aea271bb6d970d8becfc0b104e59ffeff2cd3b2f93d23e66c`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[7].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[7].value.args[1].value::Call

Source: `infra/tests/test_roadmap_download.py:79`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[7].value.args[1].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_download.py:80`; AST `98c97115c84644e1c6f3ea033504b8e634f23a76d75faff7ab224d07189db0d1`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[5].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_exact_blob_reuses_immutable_pin_without_another_network_request::root.body[12].body[5].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_download.py:80`; AST `89923cfc408001941df9631a5d3593730b8522e237e6c7c3039d0ffc1c10946b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertFalse.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[5].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:82`; AST `72cd69a7cdc6d333f9a8745fa945f8233c58b15795bdb2a47a97b935c8f197a1`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, Path, cache, dict, directory, download_pinned, root, self, target, tempfile. Outputs/bindings: cache, directory, root, target.
Calls/effect boundaries: Path, cache.mkdir, dict, download_pinned, self.assertEqual, self.assertRaises, self.entry, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0]::With

Source: `infra/tests/test_roadmap_download.py:83`; AST `ec786c69ac5d31be38b301c19ad10bddfd1b7c80a474d330228969903f6a2a9c`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, Path, cache, dict, directory, download_pinned, root, self, target, tempfile. Outputs/bindings: cache, directory, root, target.
Calls/effect boundaries: Path, cache.mkdir, dict, download_pinned, self.assertEqual, self.assertRaises, self.entry, target.read_bytes, target.write_bytes, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[6].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:83`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:84`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:84`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:85`; AST `f9ee5734fffa6827abae1b91631523afbba18a307d2a9fbb9cd14c635a11dd52`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: cache.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_download.py:86`; AST `f8e2eb057a2aa7cd871568cb5763159e3fc8f6ed674e0563c4249b87c8a752c5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache. Outputs/bindings: (none).
Calls/effect boundaries: cache.mkdir.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_download.py:86`; AST `9724b6b0123d9d46caaceafee60d8ee3e82a3b05252cfafff522d4d8d14af988`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache. Outputs/bindings: (none).
Calls/effect boundaries: cache.mkdir.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_download.py:87`; AST `219dde00ded2a8fcdd0c9d53599cd1e22197a271ee727240c3bceefa25c2f3fc`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache. Outputs/bindings: target.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[6].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_download.py:88`; AST `233abf20c390283ab01dd6d52f1fc6ce86e419e6a5df475575ae230115b036e1`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_download.py:88`; AST `eaee69b872200a866ec03cbfa531dfb709a6a91d98194206f21e76c4f9e94eaf`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.write_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[5]::With

Source: `infra/tests/test_roadmap_download.py:89`; AST `d1bb8cb9b53e2397aa3ef7a5c114745869c88731b6c22614710266d43cb4dd1e`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[6].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[5].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:89`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[5].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[5].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:90`; AST `139ab89d1e79ab80a9f4dcc199df693547757e7fca999827f2c58baa74c37046`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0].body[5].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[5].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:90`; AST `256f0fe3123e67253cf2651d53f9146b03cbdd4853922cc6237e289bb52938f2`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[5].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[5].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:90`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[5].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[6]::Expr

Source: `infra/tests/test_roadmap_download.py:91`; AST `2a7365d0861ddccba6281bc582a48e53b8a787d4f2f6e8f2a27c593d6c7e3e66`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_download.py:91`; AST `38792c24c1c743f100f299c57c73798ab58ec7ab3b6823118d8ba6d01ba2de60`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, target. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual, target.read_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[6].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:91`; AST `aa896c2be567c54cf2da0cf24792da33575188def3c5d95fda4745ed3de4fdaf`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: target. Outputs/bindings: (none).
Calls/effect boundaries: target.read_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[6].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7]::With

Source: `infra/tests/test_roadmap_download.py:92`; AST `522947b8664ee7d8a9cd7f97e6d0d055d6a980396baded9aa9d99295593ac78d`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, cache, dict, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, download_pinned, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[6].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:92`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[7].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:93`; AST `12f69007a622d01cef8396c6cd11f988186c4a63fac4ff547080b564b5843c49`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache, dict, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[6].body[0].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:93`; AST `a23137444844bc6585ed481dca8e0897b51801505f9e044cae72442a31539c0b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, dict, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[7].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:93`; AST `ff124af0062fc547849eb8dfc17992aa4393bb8cbfd584c0ef803b0220aa85d2`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: dict, self. Outputs/bindings: (none).
Calls/effect boundaries: dict, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[7].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_tampered_cache_and_escaping_filenames_are_preserved_and_rejected::root.body[12].body[6].body[0].body[7].body[0].value.args[1].args[0]::Call

Source: `infra/tests/test_roadmap_download.py:93`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[6].body[0].body[7].body[0].value.args[1].args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:95`; AST `41ef4d17e0cece75a042a9b85bf02b297c7fe81a1323d8245e26414f0f307dd6`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: FileExistsError, MagicMock, Path, cache, directory, download_pinned, io, json, next, observation, opener, partial, patch, root, self, tempfile. Outputs/bindings: cache, directory, observation, opener, partial, root.
Calls/effect boundaries: MagicMock, Path, cache.glob, cache.mkdir, download_pinned, io.BytesIO, json.loads, next, next(cache.glob('tool.whl.transport-*.json')).read_text, partial.read_bytes, partial.write_bytes, patch, self.assertEqual, self.assertRaises, self.entry, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0]::With

Source: `infra/tests/test_roadmap_download.py:96`; AST `6d720ba60807dff68144c3f7dba9a622ffb4b8ddd1d8a42c5f04180f0295cbbe`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileExistsError, MagicMock, Path, cache, directory, download_pinned, io, json, next, observation, opener, partial, patch, root, self, tempfile. Outputs/bindings: cache, directory, observation, opener, partial, root.
Calls/effect boundaries: MagicMock, Path, cache.glob, cache.mkdir, download_pinned, io.BytesIO, json.loads, next, next(cache.glob('tool.whl.transport-*.json')).read_text, partial.read_bytes, partial.write_bytes, patch, self.assertEqual, self.assertRaises, self.entry, tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:96`; AST `853963988ebadac09233dfa6af99fa22032f5b9464e7874df6572e6fd4837b04`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: tempfile. Outputs/bindings: (none).
Calls/effect boundaries: tempfile.TemporaryDirectory.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[0]::Assign

Source: `infra/tests/test_roadmap_download.py:97`; AST `a6e1b92d21e6fd662480927ebfd56e7795390eaa0680063800f02ee100304fb3`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: Path, directory. Outputs/bindings: root.
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:97`; AST `067d86df3f244636215b26ba387c26d5575ed47cc6f8626f70a6e7c63f977271`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: Path, directory. Outputs/bindings: (none).
Calls/effect boundaries: Path.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[1]::Assign

Source: `infra/tests/test_roadmap_download.py:98`; AST `f9ee5734fffa6827abae1b91631523afbba18a307d2a9fbb9cd14c635a11dd52`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: root. Outputs/bindings: cache.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[2]::Expr

Source: `infra/tests/test_roadmap_download.py:99`; AST `f8e2eb057a2aa7cd871568cb5763159e3fc8f6ed674e0563c4249b87c8a752c5`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache. Outputs/bindings: (none).
Calls/effect boundaries: cache.mkdir.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[2]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[2].value::Call

Source: `infra/tests/test_roadmap_download.py:99`; AST `9724b6b0123d9d46caaceafee60d8ee3e82a3b05252cfafff522d4d8d14af988`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache. Outputs/bindings: (none).
Calls/effect boundaries: cache.mkdir.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[2].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[3]::Assign

Source: `infra/tests/test_roadmap_download.py:100`; AST `e191ecd97c906624d1e14a50b80d0331af8e7238712d3359bd2d0fd25fcc8a74`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache. Outputs/bindings: partial.
Calls/effect boundaries: (none).
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[3]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[4]::Expr

Source: `infra/tests/test_roadmap_download.py:101`; AST `0dcb2aa74f3e11594a5c4cbdccb19d63c94da1039e99677ba5199fdb5fee5d9f`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.write_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[4]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[4].value::Call

Source: `infra/tests/test_roadmap_download.py:101`; AST `98c58a6b8eada47d40ae5383d3d11b4c7b647e50e0eaf1c45644ac64a097681c`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.write_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[4].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[5]::Assign

Source: `infra/tests/test_roadmap_download.py:102`; AST `85e0b1445612482f3bbf76f916286f957e1180fc06c67b00eec552cbe599c6fa`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: MagicMock. Outputs/bindings: opener.
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[5]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[5].value::Call

Source: `infra/tests/test_roadmap_download.py:102`; AST `650da9a8289781be1ec063f6f241a89b23d34af897a804c155c93a952022a0c9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: MagicMock. Outputs/bindings: (none).
Calls/effect boundaries: MagicMock.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[5].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[6]::Assign

Source: `infra/tests/test_roadmap_download.py:103`; AST `f435185e99b8f6490256b27492eef825e6a7ceba6e7a41667885992e86fe7efd`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: io, opener. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[6]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[6].value::Call

Source: `infra/tests/test_roadmap_download.py:103`; AST `67fba617a630dc27f549770dfe0d5d10c2992b59c02f537298fd92b7373b9d89`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: io. Outputs/bindings: (none).
Calls/effect boundaries: io.BytesIO.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[6].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7]::With

Source: `infra/tests/test_roadmap_download.py:104`; AST `9a7cf388b5424ec3dc15c813d175bbcf73d8ef66933125eea7871f557c2d4e9b`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileExistsError, cache, download_pinned, opener, patch, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, patch, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[0].body[7]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:104`; AST `cd79fc685515e859fba314c061795bd4e5ec5c4240d98095fe7b7055339e5231`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: opener, patch. Outputs/bindings: (none).
Calls/effect boundaries: patch.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[7].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].body[0]::With

Source: `infra/tests/test_roadmap_download.py:105`; AST `c95b6a01e6fc4269f57f8fa2dd2986b195acbb4a66ae19f62d3d881c111e56b2`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: FileExistsError, cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.assertRaises, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[7].body[0].body[7].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:105`; AST `5df3aae3e32718444d80e49c3eb5dbb9143bc93ca30d64b77041a5ff21a0ebb5`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: FileExistsError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[7].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:106`; AST `139ab89d1e79ab80a9f4dcc199df693547757e7fca999827f2c58baa74c37046`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[7].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:106`; AST `256f0fe3123e67253cf2651d53f9146b03cbdd4853922cc6237e289bb52938f2`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, download_pinned, root, self. Outputs/bindings: (none).
Calls/effect boundaries: download_pinned, self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[7].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[7].body[0].body[0].value.args[1]::Call

Source: `infra/tests/test_roadmap_download.py:106`; AST `3e5a4eafadc765689a4365cd02ff9e7ffd8caaba25ada392959fb6292c831714`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self. Outputs/bindings: (none).
Calls/effect boundaries: self.entry.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[7].body[0].body[0].value.args[1]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[8]::Expr

Source: `infra/tests/test_roadmap_download.py:107`; AST `df4351a700e0b59127735e7fea8f6f47cb6f89d4807ca6255c353c966596ed94`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: partial, self. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[8].value::Call

Source: `infra/tests/test_roadmap_download.py:107`; AST `6e814c8b06edd6db5b6aa78ec9efd0e0fd75ae70ad328d01f289eddd6873d860`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial, self. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes, self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[8].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[8].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:107`; AST `036cf7dddaf576ab4be59cf3ea4fc55cafb37cfe12cfe42e258ae18502a59d30`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: partial. Outputs/bindings: (none).
Calls/effect boundaries: partial.read_bytes.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[8].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[9]::Assign

Source: `infra/tests/test_roadmap_download.py:108`; AST `3c0302b54eeb9ea9d5ac97f80891275c4dbc0c429b6114f5a49fdcee829b39f8`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: cache, json, next. Outputs/bindings: observation.
Calls/effect boundaries: cache.glob, json.loads, next, next(cache.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Assign evaluation at root.body[12].body[7].body[0].body[9]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[9].value::Call

Source: `infra/tests/test_roadmap_download.py:108`; AST `35d65619711784aa6cb1358fa18439dce0be8d87ae351631ba0b9ab0b65665b0`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, json, next. Outputs/bindings: (none).
Calls/effect boundaries: cache.glob, json.loads, next, next(cache.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[9].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[9].value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:108`; AST `5fd3ea0841459be06404b918e6323d13a3596e358cfa5a29eab2da964553a8de`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, next. Outputs/bindings: (none).
Calls/effect boundaries: cache.glob, next, next(cache.glob('tool.whl.transport-*.json')).read_text.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[9].value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[9].value.args[0].func.value::Call

Source: `infra/tests/test_roadmap_download.py:108`; AST `7e45ab9843af816f5e32a4454f43cb2fe6be08dbd5645e94ec1cd2a82ab943c4`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache, next. Outputs/bindings: (none).
Calls/effect boundaries: cache.glob, next.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[9].value.args[0].func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[9].value.args[0].func.value.args[0]::Call

Source: `infra/tests/test_roadmap_download.py:108`; AST `1ed975c219c719c0c92c9a0900aa53d9a14ba5ad45c84045d15b7e041808bd74`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: cache. Outputs/bindings: (none).
Calls/effect boundaries: cache.glob.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[9].value.args[0].func.value.args[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[10]::Expr

Source: `infra/tests/test_roadmap_download.py:109`; AST `1e501b0d56c7942d22a68cab6eb9fd13b31e7b51b3c0d93e72ee9ff04239050a`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[10]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[10].value::Call

Source: `infra/tests/test_roadmap_download.py:109`; AST `351f98b5c18e4a07bafdfee298f6635ad5cbc9985fd642051385cee86c91000a`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[10].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[11]::Expr

Source: `infra/tests/test_roadmap_download.py:110`; AST `71505489dc6cef63428c96682ee98cc04605d6795bba148b4b374f6a2964c0b4`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[7].body[0].body[11]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_preexisting_partial_is_preserved_and_failure_observation_retained::root.body[12].body[7].body[0].body[11].value::Call

Source: `infra/tests/test_roadmap_download.py:110`; AST `d0a8257eb7b4ca4bbf8e0baddb786a73d8ad6bd4a13e3f8c5d89c94e9e3a9bf9`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: observation, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertEqual.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[7].body[0].body[11].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8]::FunctionDef

Source: `infra/tests/test_roadmap_download.py:112`; AST `91b89ca8e617b9dd7543e7b6c090ff12999c57d5d9f41ab491ce5495b0fe39a8`.

Rust module: `infra::tests::test_roadmap_download`. fn with explicit inputs and Result<T, SourceError>; preserve defaults, argument binding and validation order

Inputs: ContractError, _HTTPSRedirect, self, url. Outputs/bindings: url.
Calls/effect boundaries: _HTTPSRedirect, _HTTPSRedirect().redirect_request, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered FunctionDef evaluation at root.body[12].body[8]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0]::For

Source: `infra/tests/test_roadmap_download.py:113`; AST `882b37a1e53bb6f5efe6a1345ef6294be91424a920598ad1e01745e82255dd35`.

Rust module: `infra::tests::test_roadmap_download`. for over a source-compatible iterator; preserve mutation/iteration and else-on-normal-exhaustion semantics

Inputs: ContractError, _HTTPSRedirect, self, url. Outputs/bindings: url.
Calls/effect boundaries: _HTTPSRedirect, _HTTPSRedirect().redirect_request, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered For evaluation at root.body[12].body[8].body[0]; no call, error or mutation may be omitted. Iteration: url in ('http://files.pythonhosted.org/tool.whl', 'file:///tmp/tool.whl', 'https://user:password@example.com/tool.whl')
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0]::With

Source: `infra/tests/test_roadmap_download.py:114`; AST `3b4eeb0fcfee85a0abc505d6df459f1786416456121889adb70b547939926252`.

Rust module: `infra::tests::test_roadmap_download`. scoped resource guard plus explicit enter/exit and exception-suppression result

Inputs: ContractError, _HTTPSRedirect, self, url. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSRedirect, _HTTPSRedirect().redirect_request, self.assertRaises, self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered With evaluation at root.body[12].body[8].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0].items[0].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:114`; AST `00ed505af5f5993a537b027a3818c9154350efb8b8f127b5ae16b3bee747953c`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: self, url. Outputs/bindings: (none).
Calls/effect boundaries: self.subTest.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].body[0].items[0].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0].items[1].context_expr::Call

Source: `infra/tests/test_roadmap_download.py:114`; AST `f22c3550e685d381d1b5fe55b9d7964f1ac07f74f6c883169df6b2576369c26b`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: ContractError, self. Outputs/bindings: (none).
Calls/effect boundaries: self.assertRaises.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].body[0].items[1].context_expr; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:115`; AST `7c1818b69abddc5674b25d6155fe7f8d0bf218c2b25629a25f71ea8e778fc4db`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: _HTTPSRedirect, url. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSRedirect, _HTTPSRedirect().redirect_request.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[12].body[8].body[0].body[0].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:115`; AST `4f3952ccc4c388c10ffc934b828209ec20d5d0601d59291979f5297b1ce5a74a`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSRedirect, url. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSRedirect, _HTTPSRedirect().redirect_request.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].body[0].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::PinnedDownloadTests::test_redirect_cannot_downgrade_https::root.body[12].body[8].body[0].body[0].body[0].value.func.value::Call

Source: `infra/tests/test_roadmap_download.py:115`; AST `852721db4df1179ed4639cf5a496d7d4151de242aca1946ec35125dfa2852d28`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: _HTTPSRedirect. Outputs/bindings: (none).
Calls/effect boundaries: _HTTPSRedirect.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[12].body[8].body[0].body[0].body[0].value.func.value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[13]::If

Source: `infra/tests/test_roadmap_download.py:118`; AST `444eddf8b0e49cc0b0fec1a7214dc0d852a2ac320c4e5f4e792895ff744a0420`.

Rust module: `infra::tests::test_roadmap_download`. if/else with explicit Python truth-value conversion and unchanged branch order

Inputs: __name__, unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered If evaluation at root.body[13]; no call, error or mutation may be omitted. Condition: __name__ == '__main__'
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[13].body[0]::Expr

Source: `infra/tests/test_roadmap_download.py:119`; AST `e3f46e52e394d08e7a8ca90189846b5a457c749aaad3fdd3e55c87f818ee9348`.

Rust module: `infra::tests::test_roadmap_download`. Preserve this statement's evaluation order in its enclosing Rust function; use explicit Result/error and ownership effects

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Expr evaluation at root.body[13].body[0]; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.

## infra/tests/test_roadmap_download.py::module::root.body[13].body[0].value::Call

Source: `infra/tests/test_roadmap_download.py:119`; AST `49933cabf8762a41003acd318d5b2772c3505bf9a54b4e87d99e9fc1f53a73db`.

Rust module: `infra::tests::test_roadmap_download`. typed Rust call or trait boundary; preserve argument evaluation, keyword/default binding, effects and errors

Inputs: unittest. Outputs/bindings: (none).
Calls/effect boundaries: unittest.main.
Dependencies: __future__, agentinfra.roadmap_download, agentinfra.roadmap_records, agentinfra.security, io, json, pathlib, ssl, tempfile, unittest, unittest.mock.

Invariants: Preserve ordered Call evaluation at root.body[13].body[0].value; no call, error or mutation may be omitted.
Rust library candidates: serde_json; std::fs / std::path::PathBuf
Unresolved: Infer concrete dynamic types, alias/lifetime constraints and external-call exception contracts from the bound production context before accepting a replacement

Python int -> num_bigint::BigInt unless a proved source bound permits fixed width; preserve bool/int distinctions, float bits and rounding
Classify actual aliases and mutations before choosing owned values, Arc/Weak or borrowing; preserve logical lifetime and callback phases
Preserve source exception classes, matching, validation order, cleanup and partial effects with a typed error enum

Required evidence: current Python tests; actual production Python proof where applicable; future Rust correspondence and affected test/proof replay.
